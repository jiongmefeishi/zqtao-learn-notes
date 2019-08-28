**年轻即出发**...

**简书**：https://www.jianshu.com/u/7110a2ba6f9e

**知乎**：https://www.zhihu.com/people/zqtao23/posts

**GitHub源码**：https://github.com/zqtao2332

**个人网站**：http://www.zqtaotao.cn/  （停止维护更新内容）

**QQ交流群**：606939954

​    咆哮怪兽一枚...嗷嗷嗷...趁你现在还有时间，尽你自己最大的努力。努力做成你最想做的那件事，成为你最想成为的那种人，过着你最想过的那种生活。也许我们始终都只是一个小人物，但这并不妨碍我们选择用什么样的方式活下去，这个世界永远比你想的要更精彩。



最后：喜欢编程，对生活充满激情

------

------

**本节内容预告**

实例1：最长递增子序列

实例2：俄罗斯信封

实例3：出现次数的TOP K问题

实例4：TOPK问题进阶-TopKRecord结构

实例5：两个有序数组相加和的topK问题

实例6：正数数组的最小不可组成和

------

------

**实例1：最长递增子序列**

月光宝盒的密码
时间限制：C/C++语言 1000MS；其他语言 3000MS
内存限制：C/C++语言 131072KB；其他语言 655360KB
题目描述：
小希偶然得到了传说中的月光宝盒,然而打开月光宝盒需要一串密码。
虽然小希并不知道密码具体是什么，但是月光宝盒的说明书上有着一个
长度为 n (2 <= N <= 50000)的序列 a (-10^9 <= a[i] <= 10^9)的范围内。
下面写着一段话：密码是这个序列的最长的严格上升子序列的长度
(严格上升子序列是指，子序列的元素是严格递增的，

例如: [5,1,6,2,4]的最长严格上升子序列为[1,2,4])，请你帮小希找到这个密码。

输入
第1行：1个数N，N为序列的长度(2<=N<=50000)

第2到 N+1行：每行1个数，对应序列的元素(-10^9 <= a[i] <= 10^9)

输出
一个正整数表示严格最长上升子序列的长度

样例输入
8
5
1
6
8
2
4
5 
10
样例输出
5

**扩展：具体的递增子序列**

```
import java.util.Arrays;

/**
 * @description: 最长递增子序列
 * 题目描述：
 * 小希偶然得到了传说中的月光宝盒,然而打开月光宝盒需要一串密码。
 * 虽然小希并不知道密码具体是什么，但是月光宝盒的说明书上有着一个
 * 长度为 n (2 <= N <= 50000)的序列 a (-10^9 <= a[i] <= 10^9)的范围内。
 * 下面写着一段话：密码是这个序列的最长的严格上升子序列的长度
 * (严格上升子序列是指，子序列的元素是严格递增的，
 *
 * 例如: [5,1,6,2,4]的最长严格上升子序列为[1,2,4])，请你帮小希找到这个密码。
 *
 *
 * 输入
 * 第1行：1个数N，N为序列的长度(2<=N<=50000)
 *
 * 第2到 N+1行：每行1个数，对应序列的元素(-10^9 <= a[i] <= 10^9)
 *
 * 输出
 * 一个正整数表示严格最长上升子序列的长度
 */
public class Code_28_LongestIncreasingSubsequences {

    /**
     * 最长递增子序列 长度
     *
     * 碰到子序列，子数组等问题，最先想到的是状态化
     * 1、以某元素开头怎么怎么样
     * 2、以某元素结尾怎么怎么样
     *
     * 例如此题：以每一个元素结尾得到都最长子序列是多少
     *
     * 思路1、经典解法辅助数组，存储以每一个元素结尾获得的最长子序列长度
     * arr          3 1 2 5 4 6 7
     * helpLen      1 1 2 3 3 4 5
     *
     * return 5
     */
    public static int getMaxNum(int[] arr) {
        int[] helpLen = new int[arr.length];

        int maxLen = Integer.MIN_VALUE;// 记录最长子序列的长度
        for (int i = 0; i < arr.length; i++) {
            helpLen[i] = 1; // 无论之前数据怎样，自己都构成一个最长子序列，长度为1
            for (int j = 0; j < i; j++) {
                if (arr[i] > arr[j]){
                    helpLen[i] = Math.max(helpLen[i], helpLen[j] + 1);
                }
            }
            maxLen = Math.max(maxLen, helpLen[i]);
        }
        return maxLen;
    }

    /**
     * 扩展求出递增的具体序列
     *
     * 最长递增子序列 序列
     *
     * 思路1、经典解法辅助数组，存储以每一个元素结尾获得的最长子序列长度
     * arr           3 1 2 5 4 6 7
     * helpLen       1 1 2 3 3 4 5
     *
     * return 1 2 5 6 7
     */
    public static int[] getMaxList(int[] arr) {

        int[] helpLen = new int[arr.length];
        for (int i = 0; i < arr.length; i++) {
            helpLen[i] = 1; // 无论之前数据怎样，自己都构成一个最长子序列，长度为1
            for (int j = 0; j < i; j++) {
                if (arr[i] > arr[j]){
                    helpLen[i] = Math.max(helpLen[i], helpLen[j] + 1);
                }
            }
        }

        // 由辅助数组得到序列
        int index = 0; // 记录最长子序列中最大的下标
        int maxLen = Integer.MIN_VALUE;// 记录最长子序列的长度
        for (int i = 0; i < helpLen.length; i++) {
            if (maxLen < helpLen[i]) {
                maxLen = helpLen[i];
                index = i;
            }
        }

        // 反推序列
        int[] ans = new int[maxLen];
        ans[--maxLen] = arr[index]; // 填入结尾数
        for (int i = index; i >= 0; i--) {
            if (arr[i] < arr[index] && helpLen[i] == helpLen[index] - 1){
                ans[--maxLen] = arr[i];
                index = i;
            }
        }
        return ans;
    }

    /**
     * 优化：上面算法时间复杂度 O(N^2)
     * 为了加速第一步求 helpLen[] 数组
     * 再增加一个辅助数组 ends[]
     * ends[i] 含义: 长度为 i+1 的所有递增子序列的最小结尾
     *
     * arr   3 1 2 4 3
     *
     * ends[i] 更新，遍历arr数组，每一个arr[i] 都二分法在ends中寻找第一个 >= arr[i] 的数，更新
     * ends
     *       3 0 0 0 0
     *       1 0 0 0 0
     *       1 2 0 0 0
     *       1 2 4 0 0
     *       1 2 3 0 0
     */
    public static int[] getMaxList3(int[] arr){
        int[] helpLen = new int[arr.length];
        int[] ends = new int[arr.length];

        helpLen[0] = 1;
        ends[0] = arr[0];

        int L = 0;
        int R = 0;

        int right = 0; // ends右边界
        for (int i = 1; i < arr.length; i++) {
            L = 0;
            R = right;
            while (L <= R) { // 二分法在ends中寻找第一个 >= arr[i] 的数，更新
                int mid = L + (R - L) / 2;
                if (ends[mid] >= arr[i]) {
                    R = mid - 1;
                } else {
                    L = mid + 1;
                }
            }
            right = Math.max(right, L); // 没有找到的情况下 L > 边界
            ends[L] = arr[i];
            helpLen[i] = L + 1;
        }
        return generateLIS(arr, helpLen);
    }

    public static int[] getMaxList2(int[] arr){

        int[] helpLen = new int[arr.length];
        int[] ends = new int[arr.length];

        ends[0] = arr[0];
        helpLen[0] = 1;

        int right = 0; // ends右边界下标
        for (int i = 1; i < arr.length; i++) {
            int R = right;
            // 二分法查找第一个 >= arr[i] 的数的下标
            int index = getIndex(ends, 0, R, arr[i]);
            right = Math.max(right, index);
            ends[index] = arr[i];
            helpLen[i] = index + 1;
        }
        return generateLIS(arr,helpLen);
    }

    // 二分法找到第一个 >= k 的数的下标 , 没有找到就返回 +1
    // arr: 1 3 4 4   k=5  return 4
    public static int getIndex(int[] arr, int L, int R, int k){
        while (L <= R) {
            int mid = L + (R-L) / 2;
            if (arr[mid] >= k){
                R = mid - 1;
            } else {
                L = mid + 1;
            }
        }
        return L;
    }

    public static int[] generateLIS(int[] arr, int[] helpLen) {
        int len = 0;
        int index = 0;
        for (int i = 0; i < helpLen.length; i++) {
            if (helpLen[i] > len) {
                len = helpLen[i];
                index = i;
            }
        }
        int[] ans = new int[len];
        ans[--len] = arr[index];
        for (int i = index; i >= 0; i--) {
            if (arr[i] < arr[index] && helpLen[i] == helpLen[index] - 1) {
                ans[--len] = arr[i];
                index = i;
            }
        }
        return ans;
    }

    public static void main(String[] args) {
        int[] arr = {3,1,2,5,4,6,7,1};
        int[] arr2 = {1,2,4,4,4,4,4};

        System.out.println(Arrays.toString(getMaxList(arr)));
        System.out.println(Arrays.toString(getMaxList3(arr)));
        System.out.println(Arrays.toString(getMaxList2(arr)));

        System.out.println(Arrays.toString(getMaxList(arr2)));
        System.out.println(Arrays.toString(getMaxList3(arr2)));
    }
}
```

**实例2：俄罗斯信封**

见过俄罗斯套娃吗？如图所示，大的娃娃可以套在小的外面，这样就可以把多个娃娃套在一起。

![2_1_俄罗斯套娃.jpg](https://upload-images.jianshu.io/upload_images/18567339-96c8f90ff9f60775.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


现在有很多信封，每个信封有宽度和高度[w,h]，只有宽度和高度都比其他信封大的时候才能够套在别的信封的外面。那么最多多少个信封可以像俄罗斯套娃那样套在一起？

给你信封
envelopes = [[5, 4], [6, 4], [6, 7], [2, 3]],
则最多可以向俄罗斯套娃那样套在一起的信封数为3。([2, 3] => [5, 4] => [6, 7]).

```
- w无重复值（即信封的宽度每个信封都不一样）
- w可以重复（即信封的宽度存在一样的）
```

**w无重复值**

```
无重复值
按照w 进行排序，信封按照宽度从小到大进行排序，可以转化为另一个问题：给定数组，求它的最长递增子序列，就是求解的答案。
```

w有重复值

```
信封先按照宽度从小到大排序，如果等w ，h按照从大到小排序，最终求解最长递增子序列
```



```
import java.util.Arrays;
import java.util.Comparator;

/**
 * @auther: zqtao
 * @description: 俄罗斯信封（俄罗斯套娃）
 * @version: 1.0
 */
public class Code_29_RussianDollEnvelopes {

    public static class Dot{
        public int w;
        public int h;

        public Dot(int w, int h) {
            this.w = w;
            this.h = h;
        }

        @Override
        public String toString() {
            return "Dot{" +
                    "w=" + w +
                    ", h=" + h +
                    '}';
        }
    }

    public static class DotComparator implements Comparator<Dot> {
        @Override
        public int compare(Dot o1, Dot o2) {
            if (o1.w != o2.w){
                return o1.w - o2.w;
            } else {
                return o2.h - o1.h;
            }
        }
    }

    public static int maxEnvelopes(int[][] es) {
        if (es == null || es.length == 0 || es[0] == null || es[0].length != 2) {
            return 0;
        }
        Dot[] dots = new Dot[es.length];
        for (int i = 0; i < es.length; i++) {
            dots[i] = new Dot(es[i][0], es[i][1]);
        }

        Arrays.sort(dots, new DotComparator());
        System.out.println(Arrays.toString(dots));

        int[] ends = new int[es.length]; // ends[i] 含义：长度为 i+1 的所有递增子序列的最小结尾
        ends[0] = dots[0].h;
        int L = 0;
        int R = 0;
        int mid = 0;
        int right = 0; // ends 边界

        for (int i = 1; i < dots.length; i++) {
            L = 0;
            R = right;
            while (L <= R) { // 二分法求取第一个大于等于 dots[i] 大的数
                mid = L + (R - L) / 2;
                if (ends[mid] < dots[L].h){
                    L = mid + 1;
                } else {
                    R = mid - 1;
                }

                right = Math.max(right, L);
                ends[L] = dots[i].h;
            }
        }
        return right + 1;
    }

    public static void main(String[] args) {
        int[][] test = { { 4, 3 }, { 1, 2 }, { 5, 7 }, { 5, 3 }, { 1, 1 }, { 4, 9 } };
        int[][] test2 = {
                {2,3},
                {1,4},
                {1,2},
                {2,6},
                {1,3}
        };
//        System.out.println(maxEnvelopes(test));
        System.out.println(maxEnvelopes(test2));
    }
}
```

**实例3：出现次数的TOP K问题**

出现次数的TOP K问题目给定String类型的数组strArr,再给定整数k,请严格按照排名顺序打印出现次数前k名的字符串。

【进阶】设计并实现TopkRecord结构,可以不断地向其中加入字符串,并且可以根据字符串出现的情况随时打印加入次数最多前k个字符串,

具体为:

1. k在TopKRecord实例生成时指定,并且不再变化(k是构造函数的参数) 。
2. 含有add (String str)方法,即向TopKRecord中加入字符串。
3. 含有pr intTopK ()方法,即打印加入次数最多的前k个字符串,打印有哪些字符串和对应的次数即可,不要求严格按排名顺序打印。

【要求】

1,在任何时刻, add方法的时间复杂度不超过0(logk)。

2,在任何时刻, printTopK方法的时间复杂度不超过0(k)。

```
维护两个结构
1、哈希表：统计每一个str出现的次数，只需要遍历一遍数组，时间复杂度O(N)
2、小根堆：数组模拟小根堆，维护 K 个元素，依次让哈希表中统计的str进入

小根堆更新规则，堆顶次数小于新元素次数，弹出，替换；大于，不更新
```

```
import java.util.Comparator;
import java.util.HashMap;
import java.util.Map;

/**
 * @description: topK问题
 * 如果N个元素，时间复杂度可以达到O(NlogK)
 */
public class Code_30_TopKTimes_1 {

    public static class Node {
        public String str;
        public int times;

        public Node(String str, int times) {
            this.str = str;
            this.times = times;
        }
    }

    public static class StrTimesComparator implements Comparator<Node> {
        @Override
        public int compare(Node o1, Node o2) {
            return o1.times - o2.times;
        }
    }

    /**
     * 给定String类型数组arr， 给定整数 topK ,请严格按照排名顺序打印出现次数 前 topK名的字符串
     * <p>
     * 1、哈希表统计每一个Str出现的次数，只需要遍历一遍数组，时间复杂度 O(N),因为哈希表存取都是O(1)
     * 2、小根堆存 topK 个，依次让哈希表中统计的Str进入
     * 小根堆更新规则，堆顶次数小于新元素次数，弹出，替换；大于，不更新。
     */
    public static void printStrTopKTimes(String[] arr, int topK) {
        if (arr == null || topK < 1) {
            return;
        }

        HashMap<String, Integer> map = new HashMap<>();
        for (int i = 0; i < arr.length; i++) {
            String cur = arr[i];
            if (!map.containsKey(cur)) {
                map.put(cur, 1);
            } else {
                map.put(cur, map.get(cur) + 1);
            }
        }

        Node[] minHeap = new Node[topK]; // 数组模拟小根堆
        int index = 0;

        for (Map.Entry<String, Integer> entry : map.entrySet()) {
            String str = entry.getKey();
            int times = entry.getValue();

            Node node = new Node(str, times);
            if (index != topK) { // 堆未满
                minHeap[index] = node;
                heapInsert(minHeap, index++);
            } else { // 堆已满
                // 堆已满，比较堆顶元素次数和新来元素次数
                if (minHeap[0].times < node.times) {
                    minHeap[0] = node;
                    heapify(minHeap, 0, topK);
                }
            }
        }

        // 将小根堆排序，结果是大到小
        int heapSize = minHeap.length;
        swap(minHeap, 0, --heapSize);
        while (heapSize > 0) {
            heapify(minHeap, 0, heapSize);
            swap(minHeap, 0, --heapSize);
        }

        for (int i = 0; i < minHeap.length; i++) {
            System.out.println(minHeap[i].str + " : " + minHeap[i].times);
        }

    }

    /**
     * 调整更新元素后的小根堆
     *
     * @param heap     小根堆
     * @param index    更新位置
     * @param heapSize 堆容量
     */
    public static void heapify(Node[] heap, int index, int heapSize) {
        // 对于数组模拟堆结构，任意一个节点的左右子节点的位置都可以通过下标变换得到
        int left = 2 * index + 1;
        int right = left + 1; // 等同 2*index + 2
        int smallest = index; // 标记最小

        while (left < heapSize) {
            if (heap[left].times < heap[index].times) {
                smallest = left;
            }

            if (right < heapSize && heap[right].times < heap[smallest].times) {
                smallest = right;
            }

            if (smallest != index) {
                swap(heap, smallest, index);
            } else {
                break;// 自己就是最小，不用调整
            }
            index = smallest;
            left = index * 2 + 1;
            right = index * 2 + 2;
        }
    }

    public static void heapInsert(Node[] heap, int index) {
        while (index != 0) {
            int parent = (index - 1) / 2;
            if (heap[parent].times > heap[index].times) { // 新增元素的次数小于父节点次数
                swap(heap, parent, index);
                index = parent;
            } else {
                break;
            }
        }
    }

    public static void swap(Node[] heap, int index1, int index2) {
        Node tmp = heap[index1];
        heap[index1] = heap[index2];
        heap[index2] = tmp;
    }

    public static void main(String[] args) {
        String[] str = {"0","6","4","8","4","9","1","5","5","5","0","7","10","4","1","1","9","0","0","9","8","5","4","8","10","0","3","9","9","3","8","2","8","9","5","5","3","3","3","1","4","4","1","2","6","2","5","10","1","8"};
        printStrTopKTimes(str, 3);
    }
}
```

**实例4：TOPK问题进阶-TopKRecord结构**

进阶
设计并实现TopKRecord 结构，可以不断的向其中加入字符串
并且可以根据字符串出现的情况随时打印加入次数最多的前 K 个字符串，
具体为：
1、K在TopKRecord 实力生成时指定，并且不再变化（K是构造参数）
2、含有add(String str) 方法，含有printTopK(),打印加入次数最多的前 K 个字符串
不需要严格按照排名顺序打印

```
【要求】
1、在任何时刻，add方法的时间复杂度不超过 O(logK)
2、在任何时刻，printTopK方法的时间复杂度不超过 O(K)
```



```
TopKRecord 结构设计思路：
维护三个结构
小根堆：存储 K 个目的元素
词频统计map：维护元素的词频统计
堆位置map：维护元素在heap 上的状态

```

```
import java.util.HashMap;

/**
 * @description: topK问题
 * 进阶
 * 设计并实现TopKRecord 结构，可以不断的向其中加入字符串
 * 并且可以根据字符串出现的情况随时打印加入次数最多的前 K 个字符串，
 * 具体为：
 * 1、K在TopKRecord 实力生成时指定，并且不再变化（K是构造参数）
 * 2、含有add(String str) 方法，含有printTopK(),打印加入次数最多的前 K 个字符串
 * 不需要严格按照排名顺序打印
 * <p>
 * 【要求】
 * 1、在任何时刻，add方法的时间复杂度不超过 O(logK)
 * 2、在任何时刻，printTopK方法的时间复杂度不超过 O(K)
 */
public class Code_31_TopKTimes_2 {

    public static class Node {
        public String str;
        public int times;

        public Node(String s, int t) {
            str = s;
            times = t;
        }
    }

    /**
     * TopKRecord 结构
     * 维护三个结构
     * 小根堆：存储 K 个目的元素
     * 词频统计map：维护元素的词频统计
     * 堆位置map：维护元素在heap 上的状态
     */
    public static class TopKRecord {
        private Node[] heap;
        private int size; // heap size
        // 词频统计 str 对应的 node 可以看做str对应node.times
        private HashMap<String, Node> strCountNodeMap;
        // node 对应在heap 上的位置，是否在上面 -1 不在，其他代表在heap 上所处的位置
        private HashMap<Node, Integer> nodeIndexMap;

        public TopKRecord(int size) {
            heap = new Node[size]; // topK 固定
            this.size = 0;
            strCountNodeMap = new HashMap<>();
            nodeIndexMap = new HashMap<>();
        }

        public void add(String str) {
            Node curNode = null; // 维护新进的元素
            int preIndex = -1; // 维护新进的元素在heap 中的位置

            if (!strCountNodeMap.containsKey(str)) {// 如果没有这个str
                curNode = new Node(str, 1);// 临时新建记录
                strCountNodeMap.put(str, curNode);
                nodeIndexMap.put(curNode, -1);// 两个map 同时新增，默认暂时不在堆上
            } else {// 已经存在，更新
                curNode = strCountNodeMap.get(str); // 得到代表str的node节点
                curNode.times++;// 次数++
                preIndex = nodeIndexMap.get(curNode);// 同时获得在heap上的位置状态
            }

            // heap 结构的更新
            if (preIndex == -1) {
                if (size == heap.length) { // 堆满
                    if (heap[0].times < curNode.times) {
                        nodeIndexMap.put(heap[0], -1);
                        nodeIndexMap.put(curNode, 0);
                        heap[0] = curNode;
                        heapify(0, size);
                    }
                } else {
                    nodeIndexMap.put(curNode, size);
                    heap[size] = curNode;
                    heapInsert(size++);
                }
            } else {
                heapify(preIndex, size);
            }
        }

        public void printTopK() {
            System.out.println("TOP: ");
            for (int i = 0; i != heap.length; i++) {
                if (heap[i] == null) {
                    break;
                }
                System.out.print("Str: " + heap[i].str);
                System.out.println(" Times: " + heap[i].times);
            }
        }

        private void heapInsert(int index) {
            while (index != 0) {
                int parent = (index - 1) / 2;
                if (heap[index].times < heap[parent].times) {
                    swap(parent, index);
                    index = parent;
                } else {
                    break;
                }
            }
        }

        private void heapify(int index, int heapSize) {
            int l = index * 2 + 1;
            int r = index * 2 + 2;
            int smallest = index;
            while (l < heapSize) {
                if (heap[l].times < heap[index].times) {
                    smallest = l;
                }
                if (r < heapSize && heap[r].times < heap[smallest].times) {
                    smallest = r;
                }
                if (smallest != index) {
                    swap(smallest, index);
                } else {
                    break;
                }
                index = smallest;
                l = index * 2 + 1;
                r = index * 2 + 2;
            }
        }

        private void swap(int index1, int index2) {
            nodeIndexMap.put(heap[index1], index2);
            nodeIndexMap.put(heap[index2], index1);
            Node tmp = heap[index1];
            heap[index1] = heap[index2];
            heap[index2] = tmp;
        }
    }

    public static void printArray(String[] arr) {
        for (int i = 0; i != arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        TopKRecord record = new TopKRecord(2);
        record.add("zuo");
        record.printTopK();
        record.add("cheng");
        record.add("cheng");
        record.printTopK();
        record.add("Yun");
        record.add("Yun");
        record.printTopK();

    }
}

```

**实例5：两个有序数组相加和的topK问题**

【题目】给定两个有序数组arr1和arr2,再给定一个整数k,返回来自 arr1和arr2的两个数相加和最大的前k个,两个数必须分别来自两个数组。

【举例】arr1=[1, 2,3, 4, 5], arr2=[3, 5, 7, 9, 11], k=4返回数组[16, 15, 14, 14]。

***堆问题***

```
对两个数组进行排序
维护一个大根堆和一个map
两个数组看做一个矩阵
大根堆：上来将最大的值入堆，每次弹出的就是当前最大的数，同时将相邻的上一个元素和左边有一个元素入堆
map：作用是去重，防止有重复的值进入大根堆

```

```
import java.lang.reflect.Array;
import java.util.*;

/**
 * @description: 两个有序数组间相加和的 TOP K 问题
 * 堆问题
 *
 * 对两个数组进行排序
 * 维护一个大根堆和一个map
 * 两个数组看做一个矩阵
 * 大根堆：上来将最大的值入堆，每次弹出的就是当前最大的数，同时将相邻的上一个元素和左边有一个元素入堆
 * map：作用是去重，防止有重复的值进入大根堆
 *
 */
public class Code_32_TopKSumCrossTwoArrays {

    public static class HeapNode{
        public int row;
        public int col;
        public int val;

        public HeapNode(int row, int col, int val) {
            this.row = row;
            this.col = col;
            this.val = val;
        }
    }

    public static int[] topKSum(int[] a1 , int[] a2, int topK) {
        if (a1 == null || a2 == null || topK < 1) {
            return null;
        }

        topK = Math.min(topK, a1.length * a2.length);// 防止topK 超过节点个数
        HeapNode[] maxHeap = new HeapNode[topK + 1]; // 数组模拟大根堆
        int heapSize = 0; // 堆内节点个数

        int headR = a1.length - 1;
        int headC = a2.length - 1;

        int uR = -1; // 上节点左标
        int uC = -1;
        int lR = -1; // 下节点坐标
        int lC = -1;

        // 上来先入最大值进大根堆
        heapInsert(maxHeap, heapSize++, headR, headC, a1[headR] + a2[headC]);
        HashSet<String> positionSet = new HashSet<>(); // 标注是否已经入过堆

        int[] res = new int[topK];
        int resIndex = 0;

        while (resIndex != topK) {
            HeapNode headNode = popHeapHead(maxHeap, heapSize--);
            res[resIndex++] = headNode.val;

            headR = headNode.row;
            headC = headNode.col;

            // 找到上一个节点
            uR = headR - 1;
            uC = headC;
            if (headR != 0 && !isContains(uR, uC, positionSet)){ // 上一个节点是存在的，并且之前未曾入过堆
                heapInsert(maxHeap, heapSize++, uR, uC, a1[uR] + a2[uC]);
                addPositionToSet(uR, uC, positionSet);
            }

            // 找到左边节点
            lR = headR;
            lC = headC - 1;
            if (headC != 0 && !isContains(lR, lC, positionSet)) {
                heapInsert(maxHeap, heapSize++, lR, lC, a1[lR] + a2[lC]);
                addPositionToSet(lR, lC, positionSet);
            }
        }
        return res;
    }

    /**
     * 判断(r,c) 点是否已经入过堆
     */
    private static boolean isContains(int row, int col, HashSet<String> positionSet) {
        return positionSet.contains(String.valueOf(row + "_" + col));
    }

    private static void addPositionToSet(int row, int col, HashSet<String> positionSet) {
        positionSet.add(String.valueOf(row + "_" + col));
    }

    /**
     * 弹出大根堆头结点
     */
    private static HeapNode popHeapHead(HeapNode[] heap, int heapSize) {
        HeapNode pop = heap[0];
        swap(heap, 0, heapSize - 1);
        heap[--heapSize] = null;
        heapIfy(heap, 0, heapSize);
        return pop;
    }

    /**
     * 找到父节点，比较大小，交换，直到适合位置
     * @param heap 要插入的大根堆
     * @param index 要插入的位置（数组模拟大根堆，即数组中的位置）
     * @param row 插入点--行
     * @param col 插入点--列
     * @param val 插入点--值
     */
    public static void heapInsert(HeapNode[] heap, int index, int row, int col, int val){
        heap[index] = new HeapNode(row, col, val);
        int parentNodeIndex = (index - 1) / 2;
        while (index != 0) {
            if(heap[index].val > heap[parentNodeIndex].val){
                swap(heap, index, parentNodeIndex);
                index = parentNodeIndex;
                parentNodeIndex = (index - 1) / 2;
            } else {
                break;
            }
        }
    }

    public static void swap(HeapNode[] heap, int a, int b){
        HeapNode tmp = heap[a];
        heap[a] = heap[b];
        heap[b] = tmp;
    }

    /**
     * @param heap 大根堆
     * @param index 从index 这个位置开始进行调整
     * @param heapSize heap size
     */
    public static void heapIfy(HeapNode[] heap, int index, int heapSize) {
        // 数组模拟大根堆，左右子孩子的下标变换
        int left = index * 2 + 1;
        int right = index * 2 + 2;

        int largest = index;
        while (left < heapSize) { // 左孩子必须存在
            if (heap[left].val > heap[index].val){ // 左孩子更大
                largest = left;
            }

            if (right < heapSize && heap[right].val > heap[largest].val){ // 右孩子更大
                largest = right;
            }

            if (index == largest) { // 自己最大
                break;
            } else {
                swap(heap, largest, index);
            }

            index = largest;
            left = index * 2 + 1;
            right = index * 2 + 2;
        }
    }

    public static void main(String[] args) {
        int[] arr1 = {1,3,2};
        int[] arr2 = {6,5,4};

        Arrays.sort(arr1);
        Arrays.sort(arr2);
        int[] ints = topKSum(arr1, arr2, 3);
        System.out.println(Arrays.toString(ints));
    }
}

```

**实例6：正数数组的最小不可组成和**

正数数组的最小不可组成和

【题目】给定一个正数数组arr,其中所有的值都为整数,以下是最小不可组成和的概念:

把arr每个子集内的所有元素加起来会出现很多值,其中最小的记为min,最大的记为max

在区间[min, max]上,如果有数不可以被arr某一个子集相加得到,那么其中最小的那个数是arr的最小不可组成和。

在区间[min, max]上,如果所有的数都可以被arr的某一个子集相加得到,那么max+1是arr的最小不可组成和。请写函数返回正数数组arr的最小不可组成和

【举例】arr=[3, 2, 5]。子集(2}相加产生2为min,子集[3,2,5]相加产生 10为max。在区间[2, 10]上, 4、6和9不能被任何子集相加得到,其中4是arr的最小不可组成和。arr=[1,2,4]。子集[11相加产生1为min,子集11,2,4)相加产生 7为max。在区间[1,7]上,任何数都可以被子集相加得到,所以 8是arr的最小不可组成和。

【进阶题目】如果已知正数数组arr中肯定有1这个数,是否能更快地得到最小不可组成和?

```
import java.util.Arrays;
import java.util.HashSet;

/**
 * @description: 正数数组求最小不可能和
 * @version: 1.0
 */
public class Code_33_SmallestUnFormedSum {

    // 纯暴力
    public static int unformedSum1(int[] arr) {
        if (arr == null || arr.length == 0)
            return 1;
        HashSet<Integer> set = new HashSet<>(); // 存储子数组的和
        process(arr, 0, 0, set);

        int min = Integer.MAX_VALUE;
        for (int i = 0; i < arr.length; i++) {
            min = Math.min(arr[i], min);
        }

        for (int i = min + 1; i != Integer.MIN_VALUE; i++) {
            if (!set.contains(i)) {
                return i;
            }
        }
        return 0;
    }

    /**
     * @param sum 上一个递归传递下来的 子数组和
     * @param i   当前所在位置
     * @param set 和集
     */
    public static void process(int[] arr, int i, int sum, HashSet<Integer> set) {
        if (i == arr.length) {
            set.add(sum);
            return;
        }
        process(arr, i + 1, sum + arr[i], set); // 要当前节点
        process(arr, i + 1, sum, set); // 不要当前节点
    }

    /**
     * 动态规划 dp[][]
     *
     * @param arr
     * @return dp row: sum j   col: arr[i]
     * dp(i,j) : 含义是 0~i 范围上的累加和 j
     */
    public static int unformedSum2(int[] arr) {
        if (arr == null || arr.length == 0) {
            return 1;
        }

        int sum = 0;
        int min = Integer.MAX_VALUE;
        for (int i = 0; i != arr.length; i++) {
            sum += arr[i];
            min = Math.min(min, arr[i]);
        }

        boolean[][] dp = new boolean[arr.length][sum + 1];
        dp[0][arr[0]] = true; // 只有一个元素累加和，第一行只有这一个是true，其他都是false
        for (int i = 0; i < arr.length; i++) {
            dp[i][0] = true;
        }

        for (int i = 1; i < arr.length; i++) {
            for (int j = 1; j <= sum; j++) {
                if (j - arr[i] >= 0) { // 防止越界
                    dp[i][j] = dp[i - 1][j] || dp[i - 1][j - arr[i]];
                } else {
                    dp[i][j] = dp[i - 1][j];
                }

//                System.out.println("begin-----------------");// 打印每一次dp[][]的填充
//                for (int m = 0; m < dp.length; m++) {
//                    for (int n = 0; n < dp[0].length; n++) {
//                        System.out.print(dp[m][n] + "\t");
//                    }
//                    System.out.println();
//                }
//                System.out.println("end----------------\n\n");
            }
        }


        for (int j = min; j < dp[0].length; j++) {
            if (!dp[arr.length - 1][j])
                return j;
        }
        return sum + 1;
    }


    /**
     * 动态规划优化 dp[]
     * 降维
     */
    public static int unformedSum3(int[] arr) {
        if (arr == null || arr.length == 0)
            return 1;

        int sum = 0;
        int min = Integer.MAX_VALUE;
        for (int i = 0; i != arr.length; i++) {
            sum += arr[i];
            min = Math.min(min, arr[i]);
        }

        boolean[] dp = new boolean[sum + 1];
        dp[0] = true;
        for (int row = 0; row < arr.length; row++) {
            for (int col = sum; col >= arr[row]; col--) {
                dp[col] = dp[col] || (col - arr[row] >= 0 ? dp[col - arr[row]] : false);
//                System.out.println(Arrays.toString(dp));
            }
        }

        for (int i = min; i < dp.length; i++) {
            if (!dp[i])
                return i;
        }

        return sum + 1;
    }

    /**
     * 进阶
     * 正数数组中一定存在 1 这个正数，快速求出那个不可能的和
     * <p>
     * 先排序，维护一个变量 range
     * range 表示遍历到当前位置 1~range 范围内的数是可以加出来的和
     * <p>
     * 当下一个数 大于 range 超过1 ，那么返回 range+1
     */
    public static int unformedSum4(int[] arr) {
        if (arr == null || arr.length == 0) {
            return 0;
        }
        Arrays.sort(arr);
        int range = 0;
        for (int i = 0; i != arr.length; i++) {
            if (arr[i] > range + 1) {
                return range + 1;
            } else {
                range += arr[i];
            }
        }
        return range + 1;
    }


    public static void main(String[] args) {
        int[] arr = {2, 3, 5};
        System.out.println(unformedSum1(arr));
        System.out.println(unformedSum2(arr));
        System.out.println(unformedSum3(arr));
        System.out.println(unformedSum4(arr));
    }
}

```