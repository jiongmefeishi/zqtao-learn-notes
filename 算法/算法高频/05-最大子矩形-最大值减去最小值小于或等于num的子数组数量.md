**年轻即出发**...

**简书**：https://www.jianshu.com/u/7110a2ba6f9e

**知乎**：https://www.zhihu.com/people/zqtao23/posts

**GitHub源码**：https://github.com/zqtao2332

**个人网站**：http://www.zqtaotao.cn/  （停止维护更新内容）

**QQ交流群**：606939954

	    咆哮怪兽一枚...嗷嗷嗷...趁你现在还有时间，尽你自己最大的努力。努力做成你最想做的那件事，成为你最想成为的那种人，过着你最想过的那种生活。也许我们始终都只是一个小人物，但这并不妨碍我们选择用什么样的方式活下去，这个世界永远比你想的要更精彩。



最后：喜欢编程，对生活充满激情

------

------

**本节内容预告**

实例1：最大子矩形

实例2：最大值减去最小值小于或等于num的子数组数量

------

------

**实例1：最大子矩形**

给定一个整型矩阵map,其中的值只有0和1两种,求其中全是1的所有矩形区域中,最大的矩形区域为1的数量。

例如:1110其中,最大的矩形区域有3个1,所以返回3。

再如: 

1 0 1 1

1 1 1 1

1 1 1 0

其中,最大的矩形区域有6个1,所以返回6。



**思路：**

本题算法涉及到了两个知识点

1、数组压缩：将二维矩阵问题压缩为一维数组问题

2、单调栈

先理解一下这两个概念

**数组压缩**

通过合并矩阵中的数组的方式，将二维矩阵问题压缩为一维数组问题。

**单调栈**

栈的入栈顺序是递增或者递减的；两种状态可以很好的让我们求得一些特殊数据。

注意：传统单调栈针对的数据必须是不同的，所以当遇到相同数据时，使用单调栈需要进行简单处理。

**单调增**：快速得到任意元素左边最近比它小的数，右边最近比它小的数

如：3 4 5 2 1 6  可以快速得到 5左边最近比它小的数是4，右边最近比它小的数是2

单调减：同单调增相反。

**本题解题策略**

每次以第 i 行作为底，求当前构成的矩阵能得到的最大矩形。

1 0 1 1 

1 1 1 1

1 1 1 0

第一次以0行为底

```
当前构成的矩阵
1 0 1 1

最大矩形 1 1
```

第二次以1行为底

```
当前构成的矩阵
1 0 1 1 

1 1 1 1

最大矩形 
1 1
1 1
```

第三次以2行为底

```
当前构成的矩阵
1 0 1 1 

1 1 1 1

1 1 1 0

最大矩形
1 1 1
1 1 1
```

这里为了直观的理解最大矩形，可以将每一个1都看做是一个小矩形，例如1 0 1 1构成的直方图

![1_1_小矩形 .png](https://upload-images.jianshu.io/upload_images/18567339-9dc59d4e3e1de6c3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


进行数组压缩时，遇到1 则在原直方图对应位置增加一个小矩形，遇到0则消除原直方图对应位置的所有矩形。例如第三次以2为底时进行压缩构成的直方图。



![1_2_小矩形增减规则.png](https://upload-images.jianshu.io/upload_images/18567339-6ebdff23eaf9dc95.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


现在的问题就是给你一个数组，它代表一个直方图，求它的最大矩形面积。

对于任意的一个直方图，求解它的最大矩形，其实就是求解它的面积。

使用递增单调栈来找到两边比当前位置小的数，就可以直接来进行计算。

```
import java.util.Stack;

/**
 * @description: 最大矩形
 时间复杂度 O(N*M)
 * @version: 1.0
 */
public class Code_13_MaximalRectangle {

    public static int maxRecSize(int[][] map) {
        if (map == null || map.length == 0 || map[0].length == 0) {
            return 0;
        }

        int maxArea = 0; // 结果
        int[] height = new int[map[0].length]; // 数组压缩时的辅助数组，理解为矩形高度

        for (int i = 0; i < map.length; i++) {
            for (int j = 0; j < map[0].length; j++) { // 矩阵压缩
                height[j] = map[i][j] == 0 ? 0 : height[j] + 1; // 遇0，拆解当前位置所有的小矩形
            }

            // 求解当前行为底构成的直方图面积，即最大矩形
            maxArea = maxRecFromBottom(height);
        }
        return maxArea;
    }

    //
    public static int maxRecFromBottom(int[] height) {
        if (height == null || height.length == 0) {
            return 0;
        }
        int maxArea = 0;

        Stack<Integer> toBiggerStack = new Stack<>(); // 递增单调栈, 存储的是下标
        for (int i = 0; i < height.length; i++) {
            while (!toBiggerStack.isEmpty() && height[i] <= height[toBiggerStack.peek()]) {
                int index = toBiggerStack.pop();
                // 左边最近小于弹出的数的下标
                int leftSmallNumIndex = toBiggerStack.isEmpty() ? -1 : toBiggerStack.peek();
                int curArea = (i - leftSmallNumIndex - 1) * height[index]; // 关键i - leftSNI - 1
                maxArea = Math.max(maxArea, curArea);
            }
            toBiggerStack.push(i);
        }

        while (!toBiggerStack.isEmpty()) { // 单调栈中依然有元素未弹出
            int index = toBiggerStack.pop();
            int leftSmallNumIndex = toBiggerStack.isEmpty() ? -1 : toBiggerStack.peek();
            // 注意，此时可以肯定index后的元素一定都是大于等于height[index] 的
            // 所以本身加上后面的长度是height.length - leftSNI - 1
            // 如直方图全是递增数 4 5 6 7 ,单调栈剩余 4 5 ，弹出5时 ，左边最近比5 小的下标是0
            // 4 - 0 -1 = 3 就是 5 6 7 三列的宽度；
            int curArea = (height.length - leftSmallNumIndex - 1) * height[index];
            maxArea = Math.max(maxArea, curArea);
        }
        return maxArea;
    }

    public static void main(String[] args) {
        int[][] map = {{1, 0, 1, 1}, {1, 1, 1, 1}, {1, 1, 1, 0},};
        System.out.println(maxRecSize(map));
    }
}
```

**实例2：最大值减去最小值小于或等于num的子数组数量**

给定数组arr和整数num,共返回有多少个子数组满足如下情况:

max (arr[i.. j])-min (arr[i..j]) <= num



max(arr [i..j])  表示子数组arr[i..j]中的最大值, 

min (arr[i..j])   表示子数组arr[i..j]中的最小值。

**此题最优时间复杂度O(N)**

**滑动窗口**

L、R更新结构，R+1 进数，L+1,出数

**双端队列**

实质就是双链表。维护两个双端队列来**实时更新**滑动窗口的最大值和最小值。

如果全局最大和全局最小都满足，那么任意滑动窗口中的子数组也是满足的。

计算子数组时，每次只计算以滑动窗口的左边界为启点的子数组数量有多少，实际就是滑动窗口的长度。



```
import java.util.LinkedList;

/**
 * @description: 最大值减去最小值小于或等于num的子数组数量
 * 本题需要滑动窗口和两个双端队列配合
 * 维护两个双端队列来 实时 更新滑动窗口的最大值和最小值
 */
public class Code_14_AllLessNumSubArray {

    public static int getNum(int[] arr, int num) {
        if (arr == null || arr.length == 0) {
            return 0;
        }

        // 维护两个双端队列
        LinkedList<Integer> qmin = new LinkedList<>(); // 头小尾大
        LinkedList<Integer> qmax = new LinkedList<>(); // 头大尾小

        // 滑动窗口
        int L = 0;
        int R = 0;

        int res = 0;
        while (L < arr.length) {

            while (R < arr.length) {

                // 小值队列更新维护
                while (!qmin.isEmpty() && arr[qmin.peekLast()] >= arr[R]) {
                    qmin.pollLast(); // 小值双端队列更新，遇大则弹出队列中的元素，直到合适
                }
                qmin.push(R);

                // 大值队列更新维护
                while (!qmax.isEmpty() && arr[qmax.peekLast()] <= arr[R]){
                    qmax.pollLast();
                }
                qmax.push(R);

                if (arr[qmax.getFirst()] - arr[qmin.getFirst()] > num){
                    break; // 如果子数组的最大值-最小值都不满足条件，那么无论窗口怎样滑动都不可能满足题目要求，跳出
                }
                R++;
            }

            // 排除掉无效的下标，上一个循环 L 向右移动可能导致双端队列中的最大值和最小值失效
            if (qmin.peekFirst() == L) {
                qmin.pollFirst();
            }
            if (qmax.peekFirst() == L) {
                qmax.pollFirst();
            }

            // 滑动窗口如果是满足的 那么以 L为开头的子数组有 R-L个
            res += R - L;
            L++;
        }
        return res;
    }

    // for test
    public static int[] getRandomArray(int len) {
        if (len < 0) {
            return null;
        }
        int[] arr = new int[len];
        for (int i = 0; i < len; i++) {
            arr[i] = (int) (Math.random() * 10);
        }
        return arr;
    }

    // for test
    public static void printArray(int[] arr) {
        if (arr != null) {
            for (int i = 0; i < arr.length; i++) {
                System.out.print(arr[i] + " ");
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        int[] arr = getRandomArray(30);
        int num = 5;
        printArray(arr);
        System.out.println(getNum(arr, num));
    }
}
```