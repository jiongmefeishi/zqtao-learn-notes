# Java并发编程的艺术(六)——线程间的通信

多条线程之间有时需要数据交互，下面介绍五种线程间数据交互的方式，他们的使用场景各有不同。

# 1. volatile、synchronized关键字

PS：关于volatile的详细介绍请移步至：[Java并发编程的艺术(三)——volatile](http://blog.csdn.net/u010425776/article/details/54290526)

## 1.1 如何实现通信？

这两种方式都采用了同步机制实现多条线程间的数据通信。与其说是“通信”，倒不如说是“共享变量”来的恰当。当一个共享变量被volatile修饰 或 被同步块包裹后，他们的读写操作都会直接操作共享内存，从而各个线程都能看到共享变量最新的值，也就是实现了内存的可见性。

## 1.2 特点

- 这种方式本质上是“共享数据”，而非“传递数据”；只是从结果来看，数据好像是从写线程传递到了读线程；
- 这种通信方式无法指定特定的接收线程。当数据被修改后究竟哪条线程最先访问到，这由操作系统随机决定。
- 总的来说，这种方式并不是真正意义上的“通信”，而是“共享”。

## 1.3 使用场景

这种方式能“传递”变量。当需要传递一些公用的变量时就可以使用这种方式。如：传递boolean flag，用于表示状态、传递一个存储所有任务的队列等。

## 1.4 例子

> 用这种方式实现线程的开关控制。

```
// 用于控制线程当前的执行状态
private volatile boolean running = false;

// 开启一条线程
Thread thread = new Thread(new Runnable(){
    void run(){
        // 开关
        while(!running){
            Thread.sleep(1000);
        }
        // 执行线程任务
        doSometing();
    }
}).start();

// 开始执行
public void start(){
    running = true;
}
```

# 2. 等待/通知机制

## 2.1 如何实现？

等待/通知机制的实现由Java完成，我们只需调用Object类的几个方法即可。

- wait()：将当前线程的状态改为“等待态”，加入等待队列，释放锁；直到当前线程发生中断或调用了notify方法，这条线程才会被从等待队列转移到同步队列，此时可以开始竞争锁。
- wait(long)：和wait()功能一样，只不过多了个超时动作。一旦超时，就会继续执行wait之后的代码，它不会抛超时异常！
- notify()：将等待队列中的一条线程转移到同步队列中去。
- notifyAll()：将等待队列中的所有线程都转移到同步队列中去。

## 2.2 注意点

- 以上方法都必须放在同步块中；
- 并且以上方法都只能由所处同步块的锁对象调用；
- 锁对象A.notify()/notifyAll()只能唤醒由锁对象A wait的线程；
- 调用notify/notifyAll函数后仅仅是将线程从等待队列转移到阻塞队列，只有当该线程竞争到锁后，才能从wait方法中返回，继续执行接下来的代码；

## 2.3 QA

- 为什么wait必须放在同步块中调用？ 
  因为等待/通知机制需要和共享状态变量配合使用，一般是先检查状态，若状态为true则执行wait，即包含“先检查后执行”，因此需要把这一过程加锁，确保其原子执行。 
  举个例子：

```
// 共享的状态变量
boolean flag = false;

// 线程1
Thread t1 = new Thread(new Runnable(){
    public void run(){
        while(!flag){
            wait();
        }
    }
}).start();

// 线程2
Thread t2 = new Thread(new Runnable(){
    public void run(){
        flag = true;
        notifyAll();
    }
}).start();
```

上述例子thread1未加同步。当thread1执行到while那行后，判断其状态为true，此时若发生上下文切换，线程2开始执行，并一口气执行完了；此时flag已经是true，然而thread1继续执行，遇到wait后便进入等待态；但此时已经没有线程能唤醒它了，因此就一直等待下去。

- 为什么notify需要加锁？且必须和wait使用同一把锁？ 
  首先，加锁是为了保证共享变量的内存可见性，让它发生修改后能直接写入共享内存，好让wait所处的线程立即看见。 
  其次，和wait使用同一把锁是为了确保wait、notify之间的互斥，即：同一时刻，只能有其中一条线程执行。
- 为什么必须使用同步块的锁对象调用wait函数？ 
  首先，由于wait会释放锁，因此通过锁对象调用wait就是告诉wait释放哪个锁。 
  其次，告诉线程，你是在哪个锁对象上等待的，只有当该锁对象调用notify时你才能被唤醒。
- 为什么必须使用同步块的锁对象调用notify函数？ 
  告诉notify，只唤醒在该锁对象上等待的线程。

## 2.4 代码实现

等待/通知机制用于实现生产者和消费者模式。

- 生产者

```
synchronized(锁A){
    flag = true;// 或者：list.add(xx);
    锁A.notify();
}
1234
```

- 消费者

```
synchronized(锁A){
    // 不满足条件
    while(!flag){ // 或者：list.isEmpty()
        锁A.wait();
    }

    // doSometing……
}
```

## 2.5 超时等待模式

在之前的生产者-消费者模式中，如果生产者没有发出通知，那么消费者将永远等待下去。为了避免这种情况，我们可以给消费者增加超时等待功能。该功能依托于wait(long)方法，只需在wait前的检查条件中增加超时标识位，实现如下：

```
public void get(long mills){
    synchronized( list ){
        // 不加超时功能
        if ( mills <= 0 ) {
            while( list.isEmpty() ){
                list.wait();
            }
        }

        // 添加超时功能
        else {
            boolean isTimeout = false;
            while(list.isEmpty() && isTimeout){
                list.wait(mills);
                isTimeout = true;
            }

            // doSometing……
        }
    }
}
```

# 3. 管道流

## 3.1 作用

管道流用于在两个线程之间进行字节流或字符流的传递。

## 3.2 特点

- 管道流的实现依靠PipedOutputStream、PipedInputStream、PipedWriter、PipedReader。分别对应字节流和字符流。
- 他们与IO流的区别是：IO流是在硬盘、内存、Socket之间流动，而管道流仅在内存中的两条线程间流动。

## 3.3 实现

步骤如下： 
1. 在一条线程中分别创建输入流和输出流； 
2. 将输入流和输出流连接起来； 
3. 将输入流和输出流分别传递给两条线程； 
4. 调用read和write方法就可以实现线程间通信。

```
// 创建输入流与输出流对象
PipedWriter out = new PipedWriter();
PipedReader in = new PipedReader();

// 连接输入输出流
out.connect(in);

// 创建写线程
class WriteThread extends Thread{
    private PipedWriter out;

    public WriteThread(PipedWriter out){
        this.out = out;
    }

    public void run(){
        out.write("hello concurrent world!");
    }
}

// 创建读线程
class ReaderThread extends Thread{
    private PipedReader in;

    public ReaderThread(PipedReader in){
        this.in = in;
    }

    public void run(){
        in.read();
    }
}

```

# 4. join

## 4.1 作用

- join能将并发执行的多条线程串行执行；
- join函数属于Thread类，通过一个thread对象调用。当在线程B中执行threadA.join()时，线程B将会被阻塞(底层调用wait方法)，等到threadA线程运行结束后才会返回join方法。
- 被等待的那条线程可能会执行很长时间，因此join函数会抛出InterruptedException。当调用threadA.interrupt()后，join函数就会抛出该异常。

## 4.2 实现

```
public static void main(String[] args){

    // 开启一条线程
    Thread t = new Thread(new Runnable(){
        public void run(){
            // doSometing
        }
    }).start();

    // 调用join，等待t线程执行完毕
    try{
        t.join();
    }catch(InterruptedException e){
        // 中断处理……
    }

}
```