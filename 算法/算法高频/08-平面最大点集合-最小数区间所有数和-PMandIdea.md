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

实例1：平面最大点集合

实例2：最小数*区间所有数和

实例3：PMandIdea

------

------

**实例1：平面最大点集合**

P为给定的二维平面整数点集。定义P中某点x,如果x满足P中任意点都不在×的右上方区域内(横纵坐标都大于x) ,则称其为“最大的”。求出所有“最大的”点的集合。(所有点的横坐标和纵坐标都不重复,坐标轴范围在[0, 1e9)内)如下图:实心点为满足条件的点的集合。

![1_1_点集分布.png](https://upload-images.jianshu.io/upload_images/18567339-09a5c6ce4dcde67d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


请实现代码找到集合P中的所有”最大“点的集合并输出。输入第一行输入点集的个数N, 接下来N行,每行两个数字代表点的x轴和Y轴。输出输出“最大的” 点集合, 按照 轴从小到大的方式输出,每行两个数字分别代表点的x轴和Y轴。

样例输入 

5

1 2

5 3

4 6

7 5

9 0

输出结果按照 x 轴排序

4 6

7 5

9 0

```
按照x从小到大排序，然后从后向前进行遍历

扩展：x y 可以重复，即边界点不算在右上角
同理先按照x 从小到大排序，再按照y 大到小排序，然后向前进行遍历
```

```
import java.util.Arrays;
import java.util.Comparator;
import java.util.LinkedList;
import java.util.Scanner;

public class Code_25_RightCorner {

    public static class Node {
        int x;
        int y;

        public Node(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    // 暴力
    public static LinkedList<Node> getRightCornerNodes1(Node[] nodes) {

        if (nodes == null || nodes.length == 0) return null;

        Arrays.sort(nodes, new Comparator<Node>() {
            @Override
            public int compare(Node o1, Node o2) {
                return o1.x - o2.x;
            }
        });

        LinkedList<Node> res = new LinkedList<>();

        int index = 0;
        for (int i = 0; i < nodes.length; i++) {
            Node a = nodes[i];
            boolean flag = true;
            for (int j = 0; j < nodes.length; j++) {
                Node b = nodes[j];
                if (b.x > a.x && b.y > a.y) {
                    flag = false;
                    break;
                }
            }
            if (flag) {
                res.add(a);
            }
        }
        return res;
    }

    // O(N)
    public static LinkedList<Node> getRightCornerNodes2(Node[] nodes) {
        LinkedList<Node> res = new LinkedList<>();

        Arrays.sort(nodes, new Comparator<Node>() {
            @Override
            public int compare(Node o1, Node o2) {
                return o1.x - o2.x;
            }
        });

        res.add(nodes[nodes.length - 1]); // 最后一个点，一定满足

        int rightMaxY = nodes[nodes.length - 1].y; // 记录最高 y

        // 从右往左遍历，只要是小于maxY 的一定都不满足
        for (int i = nodes.length - 2; i >= 0; i--) {
            Node node = nodes[i];
            if (rightMaxY < node.y) {
                res.addFirst(node);
            }
            rightMaxY = Math.max(rightMaxY, nodes[i].y);
        }

        return res;
    }

    // O(N) 扩展，点的x , y 可以相同
    public static LinkedList<Node> getRightCornerNodes3(Node[] nodes) {
        LinkedList<Node> res = new LinkedList<>();

        Arrays.sort(nodes, new Comparator<Node>() {
            @Override
            public int compare(Node o1, Node o2) {
                if (o1.x != o2.x) {
                    return o1.x - o2.x; // x -> 小到大
                } else {
                    return o2.y - o1.y; // y -> 大到小
                }
            }
        });

        res.addFirst(nodes[nodes.length - 1]);
        int rightMaxY = nodes[nodes.length - 1].y;
        for (int i = nodes.length - 2; i >=0; i--) {
            if (nodes[i].y >= rightMaxY) {
                res.addFirst(nodes[i]);
            }
            rightMaxY = Math.max(rightMaxY, nodes[i].y);
        }
        return res;
    }

    public static void printLinkedList(LinkedList<Node> list) {
        for (Node node : list) {
            System.out.print("(" + node.x + "," + node.y + ") ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        while (in.hasNext()) {
            int N = in.nextInt();

            Node[] nodes = new Node[N];
            for (int i = 0; i < N; i++) {
                nodes[i] = new Node(in.nextInt(), in.nextInt());
            }

            printLinkedList(getRightCornerNodes1(nodes));
            printLinkedList(getRightCornerNodes2(nodes));
            printLinkedList(getRightCornerNodes3(nodes));
        }
    }
}
```

**实例2：最小数*区间所有数和**

给定一个数组序列,需要求选出一个区间,使得该区间是所有区间中经过如下计算的值最大的一个:

区间中的最小数*****区间所有数的和最后程序

输出经过计算后的最大值即可,不需要输出具体的区间。如给定序列[6 2 1]则根据上述公式,可得到所有可以选定各个区间的计算值:

[6] =6* 6=36;

[2] =2*2=4 ；

*[1] =1*1=1;

[6,2] =2 *8= 16;*

*[2,1] =1*3=3;

[6, 2, 1] =1 * 9= 9;

从上述计算可见选定区间[6] ,计算值为36,则程序输出为36区间内的所有数字都在[0, 100]的范围内;

```
单调栈：递减栈，快速找到一个元素两边最近比它大的数
```

```
import java.util.Stack;

public class Code_26_AllTimesMinToMax {

	// 暴力
	public static int max1(int[] arr) {
		int max = Integer.MIN_VALUE;
		for (int i = 0; i < arr.length; i++) { // 0~N-1
			for (int j = i; j < arr.length; j++) { // i~N-1
				int minNum = Integer.MAX_VALUE;
				int sum = 0;

				for (int k = i; k <= j; k++) { // i~j 之间子数组
					sum += arr[k];
					minNum = Math.min(minNum, arr[k]);
				}
				max = Math.max(max, minNum * sum);
			}
		}
		return max;
	}

	// 单调栈
	public static int max2(int[] arr) {
		int size = arr.length;
		int[] sums = new int[size]; // 预处理数组
		sums[0] = arr[0];
		for (int i = 1; i < size; i++) {
			sums[i] = sums[i - 1] + arr[i];// 计算arr数组每一项和
			// 6 2 8
			// 6 8 16
		}
		int max = Integer.MIN_VALUE;
		Stack<Integer> stack = new Stack<>(); // 单调栈：递减栈，快速找到一个元素两边最近比它大的数
		// 这里单调栈存放下标

		for (int i = 0; i < size; i++) {
			while (!stack.isEmpty() && arr[stack.peek()] >= arr[i]) {
				int j = stack.pop(); // 当前区间最小
				max = Math.max(max,
						(stack.isEmpty() ? sums[i - 1] : (sums[i - 1] - sums[stack.peek()]))
								* arr[j]);
			}
			stack.push(i);
		}
		while (!stack.isEmpty()) { // 余栈处理
			int j = stack.pop();
			max = Math.max(max, (stack.isEmpty() ? sums[size - 1]
					: (sums[size - 1] - sums[stack.peek()])) * arr[j]);
		}
		return max;
	}

	public static int[] gerenareRondomArray() {
		int[] arr = new int[(int) (Math.random() * 20) + 10];
		for (int i = 0; i < arr.length; i++) {
			arr[i] = (int) (Math.random() * 101);
		}
		return arr;
	}

	public static void main(String[] args) {
		int testTimes = 2000000;
		for (int i = 0; i < testTimes; i++) {
			int[] arr = gerenareRondomArray();
			if (max1(arr) != max2(arr)) {
				System.out.println("FUCK!");
				break;
			}
		}

	}

}
```

**实例3：PMandIdea**

产品经理(PM)有很多好的idea,而这些idea需要程序员实现。现在有N个PM,在某个时间会想出一个 idea,每个idea有提出时间、所需时间和优先等级。对于一个PM来说,最想实现的 idea首先考虑优先等级高的,相同的情况下优先所需时间最小的,还相同的情况下选择最早想出的,没有PM会在同一时刻提出两个idea同时有M个程序员,每个程序员空闲的时候就会查看每个PM尚未执行并且最想完成的一个idea,然后从中挑选出所需时间最小的一个idea独立实现,如果所需时间相同则选择PM序号最小的。直到完成了idea才会重复上述操作。如果有多个同时处于空闲状态的程序员,那么他们会依次进行查看idea的操作。求每个idea实现的时间。

输入

输入第一行三个数N、M、P,分别表示有N个PM, M个程序员, P个idea。随后有P行,每行有4个数字,分别是PM序号、提出时间、优先等级和所需时间。所有输入数据范围为[1, 3000]

输出

输出P行,分别表示每个idea实现的时间点。

样例输入 

2 2 5 

1 1 1 2 

1 2 1 1 

1 3 2 2 

2 1 1 2 

2 3 5 5

样例输出 

3

4

5

3

9

```
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.PriorityQueue;

/**
 * @description: SED: Software Develop Engineer
 * PM: Project Manager
 */
public class Code_27_SDEandPM {

    /**
     * 项目的数据结构
     * 封装项目的基本属性
     */
    public static class Program {
        public int index; // 项目编号
        public int pmId; // 归属于哪个 pm, pmId: Project Manager的ID
        public int startTime; // 项目可以开始做的时间，start之前的时间段不能做
        public int rank; // 项目的优先级
        public int costTime; // 项目花费时间

        public Program(int index, int pmId, int beginTime, int rank, int costTime) {
            this.index = index;
            this.pmId = pmId;
            this.startTime = beginTime;
            this.rank = rank;
            this.costTime = costTime;
        }
    }


    /**
     * 比较器
     * pm 拥有众多项目，按照比较器规则排序最喜欢的项目
     * <p>
     * 规则：
     * 1、优先级高
     * 2、花费时间短
     * 3、最先想出的
     */
    public static class PmLoveRule implements Comparator<Program> {
        @Override
        public int compare(Program o1, Program o2) {
            if (o1.rank != o2.rank) {
                return o1.rank - o2.rank;
            } else if (o1.costTime != o2.costTime) {
                return o1.costTime - o2.costTime;
            } else {
                return o1.startTime - o2.startTime;
            }
        }
    }


    /**
     * 大结构
     * 1、对于激活状态的项目program（startTime 在 程序员苏醒范围内），进入大结构
     * <p>
     * 2、对于这个program
     * 先经过pm 喜欢的规则进行排序，选出 PM 最想做的项目
     * 然后经过SDE 喜欢的规则进行排序，最后弹出是程序员最想做的项目
     * <p>
     * 3、这个大结构唯一暴露出去的只有两个接口，一个是add()  一个是pop()
     */
    public static class BigQueues {
        private List<PriorityQueue<Program>> pmQueues;// PM 组成的队列集合，每一个PM独立为一个堆
        private Program[] heap; // 存放每一个PM最想做的项目，排序规则按照SdeLoveRule, 选出程序员最想做的项目
        private int[] indexes;
        private int heapSize; // 大结构里项目个数

        public BigQueues(int size) { // size是PM 的个数
            this.heapSize = 0;
            this.heap = new Program[size]; // 每个PM都贡献一个自己最想要做的项目
            this.indexes = new int[size + 1];
            for (int i = 0; i <= size; i++) {
                indexes[i] = -1;
            }

            pmQueues = new ArrayList<>();
            for (int i = 0; i <= size; i++) { // size 个PM，每一个都独立一个堆
                pmQueues.add(new PriorityQueue<>(new PmLoveRule()));
            }
        }

        public boolean isEmpty() {
            return heapSize == 0;
        }


        // 新增一个项目进大结构
        public void add(Program program) {
            PriorityQueue<Program> queue = pmQueues.get(program.pmId);
            queue.add(program);

            // 大结构中新增元素后，heap可能会发生变化
            Program head = queue.peek();
            int heapindex = indexes[head.pmId];
            if (heapindex == -1) {
                heap[heapSize] = head;
                indexes[head.pmId] = heapSize;
                heapInsert(heapSize++);
            } else {
                heap[heapindex] = head;
                heapInsert(heapindex);
            }
        }


        private void heapInsert(int index) {
            while (index != 0) {
                int parent = (index - 1) / 2;
                if (sdeLoveRule(heap[parent], heap[index]) > 0) {
                    swap(parent, index);
                    index = parent;
                } else {
                    break;
                }
            }
        }


        private void swap(int index1, int index2) {
            Program p1 = heap[index1];
            Program p2 = heap[index2];
            heap[index1] = p2;
            heap[index2] = p1;
            indexes[p1.pmId] = index2;
            indexes[p2.pmId] = index1;
        }


        // SDE 排序规则
        private static int sdeLoveRule(Program o1, Program o2) {
            if (o1.costTime != o2.costTime) {
                return o1.costTime - o2.costTime;
            } else {
                return o1.pmId - o2.pmId;
            }
        }


        public Program pop() {
            Program head = heap[0];
            PriorityQueue<Program> queue = pmQueues.get(head.pmId);
            queue.poll();
            if (queue.isEmpty()) {
                swap(0, heapSize - 1);
                heap[--heapSize] = null;
                indexes[head.pmId] = -1;
            } else {
                heap[0] = queue.peek();
            }
            heapify(0);
            return head;
        }

        private void heapify(int index) {
            int left = index * 2 + 1;
            int right = index * 2 + 2;
            int best = index;
            while (left < heapSize) {
                if (sdeLoveRule(heap[left], heap[index]) < 0) {
                    best = left;
                }
                if (right < heapSize && sdeLoveRule(heap[right], heap[best]) < 0) {
                    best = right;
                }
                if (best == index) {
                    break;
                }
                swap(best, index);
                index = best;
                left = index * 2 + 1;
                right = index * 2 + 2;
            }
        }

    }

    public static class StartRule implements Comparator<Program> {

        @Override
        public int compare(Program o1, Program o2) {
            return o1.startTime - o2.startTime;
        }

    }

    public static int[] workFinish(int pms, int sdes, int[][] programs) {
        PriorityQueue<Program> programsQueue = new PriorityQueue<>(new StartRule());
        for (int i = 0; i < programs.length; i++) {
            Program program = new Program(i, programs[i][0], programs[i][1], programs[i][2], programs[i][3]);
            programsQueue.add(program);
        }
        PriorityQueue<Integer> sdeWakeQueue = new PriorityQueue<>();
        for (int i = 0; i < sdes; i++) {
            sdeWakeQueue.add(1);
        }
        BigQueues bigQueues = new BigQueues(pms);
        int finish = 0;
        int[] ans = new int[programs.length];
        while (finish != ans.length) {
            int sdeWakeTime = sdeWakeQueue.poll();
            while (!programsQueue.isEmpty()) {
                if (programsQueue.peek().startTime > sdeWakeTime) {
                    break;
                }
                bigQueues.add(programsQueue.poll());
            }
            if (bigQueues.isEmpty()) {
                sdeWakeQueue.add(programsQueue.peek().startTime);
            } else {
                Program program = bigQueues.pop();
                ans[program.index] = sdeWakeTime + program.costTime;
                sdeWakeQueue.add(ans[program.index]);
                finish++;
            }
        }
        return ans;
    }

    public static void printArray(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            System.out.println(arr[i]);
        }
    }

    public static void main(String[] args) {
        int pms = 2;
        int sde = 2;
        int[][] programs = {{1, 1, 1, 2}, {1, 2, 1, 1}, {1, 3, 2, 2}, {2, 1, 1, 2}, {2, 3, 5, 5}};
        int[] ans = workFinish(pms, sde, programs);
        printArray(ans);
    }
}
```