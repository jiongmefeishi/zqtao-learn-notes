# Java并发编程(五)-中断

## 什么是中断？

- 在Java中没有办法立即停止一条线程，然而停止线程却显得尤为重要，如取消一个耗时操作。因此，Java提供了一种用于停止线程的机制——中断。

- 中断只是一种协作机制，Java没有给中断增加任何语法，中断的过程完全需要程序员自己实现。若要中断一个线程，你需要手动调用该线程的interrupted方法，该方法也仅仅是将线程对象的中断标识设成true；接着你需要自己写代码不断地检测当前线程的标识位；如果为true，表示别的线程要求这条线程中断，此时究竟该做什么需要你自己写代码实现。
- 每个线程对象中都有一个标识，用于表示线程是否被中断；该标识位为true表示中断，为false表示未中断；
- 通过调用线程对象的interrupt方法将该线程的标识位设为true；可以在别的线程中调用，也可以在自己的线程中调用。



## 中断的相关方法

- public void interrupt() 
  将调用者线程的中断状态设为true。
- public boolean isInterrupted() 
  判断调用者线程的中断状态。
- public static boolean interrupted 
  只能通过Thread.interrupted()调用。 
  它会做两步操作：
  1. 返回**当前线程**的中断状态；
  2. 将当前线程的中断状态设为false；



## 暂停、继续、停止线程（已过时）

以下三个方法都是通过线程对象去调用。

- suspend() 
  暂停调用者线程，只释放CPU执行权，不释放锁。 
  由于在不释放资源的情况下进入睡眠状态，容易产生死锁。因此已过时！
- resume() 
  恢复调用者线程，让他处于就绪状态。
- stop() 
  调用stop后，并不会保证资源被正确地释放，它会使程序处于不正确的状态下。


PS：stop和interrupt的区别？



## 中断的使用

要使用中断，首先需要在可能会发生中断的线程中不断监听中断状态，一旦发生中断，就执行相应的中断处理代码。 
当需要中断线程时，调用该线程对象的interrupt函数即可。



## 设置中断监听

```
Thread t1 = new Thread( new Runnable(){
    public void run(){
        // 若未发生中断，就正常执行任务
        while(!Thread.currentThread.isInterrupted()){
            // 正常任务代码……
        }

        // 中断的处理代码……
        doSomething();
    }
} ).start();
```

正常的任务代码被封装在while循环中，每次执行完一遍任务代码就检查一下中断状态；一旦发生中断，则跳过while循环，直接执行后面的中断处理代码。



## 触发中断



```
t1.interrupt();
```

上述代码执行后会将t1对象的中断状态设为true，此时t1线程的正常任务代码执行完成后，进入下一次while循环前Thread.currentThread.isInterrupted()的结果为true，此时退出循环，执行循环后面的中断处理代码。



## 安全地停止线程

stop函数停止线程过于暴力，它会立即停止线程，不给任何资源释放的余地，下面介绍两种安全停止线程的方法。



## 循环标记变量

自定义一个共享的boolean类型变量，表示当前线程是否需要中断。

**中断标识**

```
volatile boolean interrupted = false;
```

**任务执行函数**

```
Thread t1 = new Thread( new Runnable(){
    public void run(){
        while(!interrupted){
            // 正常任务代码……
        }
        // 中断处理代码……
        // 可以在这里进行资源的释放等操作……
    }
} );
```

**中断函数**

```
Thread t2 = new Thread( new Runnable(){
    public void run(){
        interrupted = true;
    }
} );
```

### 循环中断状态

- 中断标识 
  由线程对象提供，无需自己定义。
- 任务执行函数



```
Thread t1 = new Thread( new Runnable(){
    public void run(){
        while(!Thread.currentThread.isInterrupted()){
            // 正常任务代码……
        }
        // 中断处理代码……
        // 可以在这里进行资源的释放等操作……
    }
} );
```

- 
  中断函数


```
t1.interrupt();
```



## 总结

上述两种方法本质一样，都是通过循环查看一个共享标记为来判断线程是否需要中断，他们的区别在于：第一种方法的标识位是我们自己设定的，而第二种方法的标识位是Java提供的。除此之外，他们的实现方法是一样的。

上述两种方法之所以较为安全，是因为一条线程发出终止信号后，接收线程并不会立即停止，而是将本次循环的任务执行完，再跳出循环停止线程。此外，程序员又可以在跳出循环后添加额外的代码进行收尾工作。



**处理中断**

上文都在介绍如何获取中断状态，那么当我们捕获到中断状态后，究竟如何处理呢？

- Java类库中提供的一些可能会发生阻塞的方法都会抛InterruptedException异常，如：BlockingQueue#put、BlockingQueue#take、Object#wait、Thread#sleep。
- 当你在某一条线程中调用这些方法时，这个方法可能会被阻塞很长时间，你可以在别的线程中调用当前线程对象的interrupt方法触发这些函数抛出InterruptedException异常。
- 当一个函数抛出InterruptedException异常时，表示这个方法阻塞的时间太久了，别人不想等它执行结束了。
- 当你的捕获到一个InterruptedException异常后，亦可以处理它，或者向上抛出。
- 抛出时要注意？？？：当你捕获到InterruptedException异常后，当前线程的中断状态已经被修改为false(表示线程未被中断)；此时你若能够处理中断，则不用理会该值；但如果你继续向上抛InterruptedException异常，你需要再次调用interrupt方法，将当前线程的中断状态设为true。
- 注意**：绝对不能“吞掉中断”！即捕获了InterruptedException而不作任何处理。这样违背了中断机制的规则，别人想让你线程中断，然而你自己不处理，也不将中断请求告诉调用者，调用者一直以为没有中断请求。



**QA**

为什么catch InterruptedException后会自动清除中断状态？