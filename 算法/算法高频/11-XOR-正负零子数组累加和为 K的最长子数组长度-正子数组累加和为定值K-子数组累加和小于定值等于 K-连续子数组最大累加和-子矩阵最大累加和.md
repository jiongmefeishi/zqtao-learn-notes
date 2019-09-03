**年轻即出发**...

**简书**：https://www.jianshu.com/u/7110a2ba6f9e

**知乎**：https://www.zhihu.com/people/zqtao23/posts

**GitHub源码**：https://github.com/zqtao2332

**个人网站**：http://www.zqtaotao.cn/  （停止维护更新内容）

**QQ交流群**：606939954

​	    咆哮怪兽一枚...嗷嗷嗷...趁你现在还有时间，尽你自己最大的努力。努力做成你最想做的那件事，成为你最想成为的那种人，过着你最想过的那种生活。也许我们始终都只是一个小人物，但这并不妨碍我们选择用什么样的方式活下去，这个世界永远比你想的要更精彩。



最后：喜欢编程，对生活充满激情

------

------

**本节内容预告**

实例1：XOR

实例2：正负零子数组累加和为 K的最长子数组长度

实例3：正子数组累加和为定值K

实例4：子数组累加和小于定值等于 K

实例5：连续子数组最大累加和

实例6：子矩阵最大累加和

------

------

**实例1：XOR**

给出n个数字a_1..... an,问最多有多少不重叠的非空区间,使得每个区间内数字的xor都等于0.

输入描述:第一行一个整数n; 第二行n个整数 a.1..... an;对于 30%的数据, n<=20; 对于100%的数据, n<=100000 a_i<=100000;

输出描述:一个整数表示最多的区间个数;

示例1输入

4 

3 0 2 2 输出 2

```
维护一个map和xor 变量
xor: 0~i 异或结果
map：KEY --> 存储 0~i 异或结果(xor)     VALUE --> 记录结果所在的位置（实时更新）

每一次 0~i 上得到 xor 都向 map 中查询上一次出现 xor 结果的位置 j，那么 j+1~i 构成一个结果区域（异或为0）
```



```
import java.util.HashMap;

/**
 * @description: XOR
 * 给出n个数字a_1..... an,问最多有多少不重叠的非空区间,使得每个区间内数字的xor都等于0.
 *
 * 输入描述:第一行一个整数n; 第二行n个整数 a.1..... an;对于 30%的数据, n<=20; 对于100%的数据, n<=100000 a_i<=100000;
 *
 * 输出描述:一个整数表示最多的区间个数;
 *
 * 示例1输入
 *
 * 4
 *
 * 3 0 2 2 输出 2
 * @version: 1.0
 */
public class Code_39_XOR {

    /**
     * 思路：
     * 维护一个map和xor 变量
     *
     * xor: 0~i 异或结果
     * map：KEY --> 存储 0~i 异或结果(xor)     VALUE --> 记录结果所在的位置（实时更新）
     *
     * 每一次 0~i 上得到 xor 都向 map 中查询上一次出现 xor 结果的位置 j，那么 j+1~i 构成一个结果区域（异或为0）
     */
    public static int mostXORs0(int[] arr) {
        if (arr == null || arr.length == 0) return 0;

        int ans = Integer.MIN_VALUE;
        int xor = 0;
        int[] mosts = new int[arr.length]; // 记录0~i 位置上能够得到的最多的区域是多少？
        HashMap<Integer, Integer> map = new HashMap<>();
        map.put(0, -1);// 初始化map，应对第一次出现xor=0 的情况，表示0~i 位置第一次xor=0时，结果mosts[i]=0

        for (int i = 0; i < arr.length; i++) {
            xor ^= arr[i];
            if (map.containsKey(xor)){ // 之前存在xor
                int j = map.get(xor);
                mosts[i] = j == -1 ? 1 : mosts[j] + 1;
            }

            mosts[i] = i == 0 ? mosts[i] : Math.max(mosts[i], mosts[i - 1]); // 之前不存在或者是现在所划分的没有i-1 位置划分的区域多
            map.put(xor, i);
            ans = Math.max(ans, mosts[i]);
        }
        return ans;
    }

    public static void main(String[] args) {
        int[] arr = {3,2,2,0,2,2};
        System.out.println(mostXORs0(arr));
    }
}
```

**实例2：正负零子数组累加和为 K的最长子数组长度**

```
import java.util.HashMap;

/**
 * @description: 正负零子数组累加和为 K的最长子数组长度
 * @version: 1.0
 */
public class Code_40_LongestSumKSubArrayLength {


    /**
     * 此题和Code_39_XOR 思路基本类似
     *
     * 思路：
     * 维护一个 sum 和一个 maxLen
     * 寻找么一个以 i 位置结尾 累加和为K 的最长子数组长度
     *
     * 0~i 位置累加和是 sum ，那么只需要找到第一次出现 sum-K 的位置 j，就能知道 j+1~i 位置累加和一定是 K
     * 如： K=200    0~i ：sum=1000， sum-K=800 ---> j  那么j+1~i 一定能累加出 K=200，记录长度 i-j+1
     * @param arr
     * @return
     */
    public static int subArrSumK(int[] arr, int K) {
        if (arr == null || arr.length == 0) {
            return 0;
        }
        HashMap<Integer, Integer> map = new HashMap<>();
        map.put(0, -1); // sum-k=0 第一次出现的情况，表示0~i 位置，就是当前最长i-(-1)+1
        int maxLen = 0;
        int sum = 0;
        for (int i = 0; i < arr.length; i++) {
            sum += arr[i];
            if (map.containsKey(sum- K)){
                int j = map.get(sum - K); // 第一次出现 sum-K 的位置
                maxLen = Math.max(i-j, maxLen);
            }
            if (!map.containsKey(sum)) {
                map.put(sum, i);
            }
        }
        return maxLen;
    }

    public static void main(String[] args) {
        int[] arr = {1,1,1,1,1,5,1,2,3};
        System.out.println(subArrSumK(arr, 5));
    }
}

```

**实例3：正子数组累加和为定值K**

思路：双指针滑动窗口

```
/**
 * @description: 正子数组累加和为定值K
 * @version: 1.0
 */
public class Code_41_SubArrSumK {

    /**
     * 滑动窗口
     * 维护一个sum变量记录窗口内元素累加和
     * 当sum < K, 窗口扩容 R++
     * 当sum > K，窗口缩减 L++
     * 当sum = K，记录子数组长度（窗口长度），同时缩减窗口容量 L++
     */
    public static int maxSumK(int[] arr, int K) {
        if (arr == null || arr.length == 0) return 0;

        int L = 0;
        int R = 0;
        int sum = arr[R];
        int len = 0;
        while (R < arr.length){
            if (sum == K) {
                len =  Math.max(R - L + 1, len);
                sum -= arr[L++];
            } else if (sum < K){
                R++;
                if (R == arr.length) break;
                sum += arr[R];
            } else {
                sum -= arr[L++];
            }
        }
        return len;
    }

    public static void main(String[] args) {
        int[] arr = {1,2,1,1,1,4,2,1,1,1,1,1,1};
        System.out.println(maxSumK(arr, 6));
    }
}
```

**实例4：子数组累加和小于定值等于 K**

```
import java.util.HashMap;

/**
 * @description: 子数组累加和小于定值等于 K
 * @version: 1.0
 */
public class Code_42_LongestSubArrayLessSum {

    /**
     * 时间复杂度 O(N)
     * 思路：
     * 第一步：1、获取以i 位置开始 i~N-1 能够累加出的最小和
     *        2、记录最小和累加的右边界
     * 第二步：滑动窗口求取最大长度
     * 其中的加速过程是：不需要每一个 i 位置都进行向后累加，可以借助前一次累加的最大结果 - (i-1)位置的结果
     * 得到的就是 i~(i-1)所达到的最大值
     *
     * 如下面范围内都是第一步得到的最小累加和的区域
     * 0~6  7~9   10~17   18~23   24~28
     * 
     * 0位置开始窗口扩容，直到 10~17 位置内累加和都是小于 K 的， 累加18~23区域会大于 K，那么0~17范围累加和为 sum
     * 此时开始从 1 位置遍历，不需要从新从 1~6 .... 10~17 依次累加，只需要 sum-arr[0] 即可得到新 sum 这就是加速过程
     * 
     */
    public static int maxLengthSumLessK(int[] arr, int K) {
        if (arr == null || arr.length == 0) return 0;

        int[] sums = new int[arr.length]; // 以i 位置开始 i~N-1 能够累加出的最小和
        HashMap<Integer, Integer> ends = new HashMap<>(); // 记录最小累加和的右边界

        sums[arr.length - 1] = arr[arr.length - 1];// 最后一个数累加最小和就是自己
        ends.put(arr.length - 1, arr.length - 1);
        for (int i = arr.length - 2; i >= 0; i--) { // 倒遍历
            if (sums[i+1] < 0) {
                sums[i] = arr[i] + sums[i+1];
                ends.put(i, ends.get(i + 1));// 填充的是 i+1 的右边界
            } else { // >=0 自己本身就是最小和
                sums[i] = arr[i];
                ends.put(i, i);
            }
        }

        // 遍历完毕，采用滑动窗口求最大长度
        int end = 0;
        int sum = 0;
        int res = 0;

        for (int i = 0; i < arr.length; i++) {
            while (end < arr.length && sum + sums[end] <= K){
                sum += sums[end];
                end = ends.get(end) + 1;
            }

            sum -= end > i ? arr[i] : 0;
            res = Math.max(res, end - i);
            end = Math.max(end, i + 1); // 更新滑动窗口边界
        }

        return res;
    }

    public static void main(String[] args) {
        int[] arr = {7,5,-1,-2,-2,0,0,0};
        System.out.println(maxLengthSumLessK(arr, 3));
    }
}
```

**实例5：连续子数组最大累加和**

```
/**
 * @description: 连续子数组最大和
 * 给定无序整数序列,求连续子数组最大和,例如1-23 17-7 11-21 34),
 * 子串为17,-7,111,最大和为21输入描述:输入为整数序列,数字用空格分隔,
 * 如:-23 17-7 11-2 1-34输出描述:输出为子序列的最大和: 21
 * 示例1输入-23 17 -7 11 -2 1 -34输出21
 * @version: 1.0
 */
public class Code_43_MaxSumSubArr {

    /**
     * 策略
     * 维护两个变量 cur 和 max
     * cur 向右扩展累加，过程中只要cur 不是小于 0 的，都继续进行累加过程；小于0 cur归 0
     * max 更新记录累加出来的最大和
     *
     *
     * 一个含有正负零的数组中存在最大的子数组
     * 那么这个最大的子数组一定不是以 负数开始的，即子数组的任意前缀一定不是负数
     *
     * 如果数组中都是负数，也不会错过那个最大的负数
     */
    public static int maxSum(int[] arr) {
        if (arr == null || arr.length == 0) return 0;
        int cur = 0;
        int max = Integer.MIN_VALUE;
        for (int i = 0; i < arr.length; i++) {
            cur += arr[i];
            max = Math.max(max, cur);
            cur = cur < 0 ? 0 : cur;
        }
        return max;
    }

    public static void main(String[] args) {
        int[] arr = {-1,-2,-3, 1};
        System.out.println(maxSum(arr));
    }
}
```

**实例6：子矩阵最大累加和**

```
/**
 * @description: 子矩阵最大累加和
 * N*M 矩阵
 * 时间复杂度可以达到 O(N*N*M)
 * @version: 1.0
 */
public class Code_44_MaxSumSubMatrix {

    public static int maxSubMatrix(int[][] matrix) {
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
            return 0;
        }

        int max = Integer.MIN_VALUE;
        int cur = 0;
        int[] arr = null;
        for (int i = 0; i < matrix.length; i++) { // 控制需要以仅包含 i 层数组开始，求最大累加和
            arr = new int[matrix[0].length];
            for (int j = i; j < matrix.length; j++) { // 控制 i~N-1 层逐次降维
                cur = 0;
                for (int k = 0; k < arr.length; k++) { // 降维后，求一位数组的最大累加和
                    arr[k] += matrix[j][k];
                    cur += arr[k];
                    max = Math.max(max, cur);
                    cur = cur < 0 ? 0 : cur;
                }
            }
        }
        return max;
    }

    public static void main(String[] args) {
        int[][] matrix = { { -90, 48, 78 }, { 64, -40, 64 }, { -81, -7, 66 } };
        System.out.println(maxSubMatrix(matrix));
    }
}
```

