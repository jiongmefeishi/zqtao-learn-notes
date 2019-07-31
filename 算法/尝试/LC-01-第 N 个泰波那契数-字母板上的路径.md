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

实例1：5139. 第 N 个泰波那契数

实例2：5140. 字母板上的路径

------

------



### 5139. 第 N 个泰波那契数

原题：https://leetcode-cn.com/contest/weekly-contest-147/problems/n-th-tribonacci-number/

泰波那契序列 Tn 定义如下： 

T0 = 0, T1 = 1, T2 = 1, 且在 n >= 0 的条件下 Tn+3 = Tn + Tn+1 + Tn+2

给你整数 `n`，请返回第 n 个泰波那契数 Tn 的值。

**示例 1：**

```
输入：n = 4
输出：4
解释：
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
```

  

**示例 2：**

```
输入：n = 25
输出：1389537
```

**提示：**

- `0 <= n <= 37`
- 答案保证是一个 32 位整数，即 `answer <= 2^31 - 1`。

```
    public static int tribonacci(int n) {
        if (n == 0) return 0;
        if (n == 1 || n == 2) return 1;

        int a = 0;
        int b = 1;
        int c = 1;
        int res = 0;
        for (int i = 3; i <= n; i++) {
            res = a + b+ c;
            a = b;
            b = c;
            c = res;
        }
        return res > Integer.MAX_VALUE ? -1 : res;
    }
```

### 5140. 字母板上的路径

原题：https://leetcode-cn.com/contest/weekly-contest-147/problems/alphabet-board-path/

我们从一块字母板上的位置 `(0, 0)` 出发，该坐标对应的字符为 `board[0][0]`。

  

在本题里，字母板为`board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]`.

  

我们可以按下面的指令规则行动：

  

- 如果方格存在，`'U'` 意味着将我们的位置上移一行；
- 如果方格存在，`'D'` 意味着将我们的位置下移一行；
- 如果方格存在，`'L'` 意味着将我们的位置左移一列；
- 如果方格存在，`'R'` 意味着将我们的位置右移一列；
- `'!'` 会把在我们当前位置 `(r, c)` 的字符 `board[r][c]` 添加到答案中。

  

返回指令序列，用最小的行动次数让答案和目标 `target` 相同。你可以返回任何达成目标的路径。

**示例 1：**

```
输入：target = "leet"
输出："DDR!UURRR!!DDD!"
```

  

**示例 2：**

```
输入：target = "code"
输出："RR!DDRR!UUL!R!"
```

**提示：**

- `1 <= target.length <= 100`
- `target` 仅含有小写英文字母。

```
1、看做6个桶，前5个桶，每个桶里面5个位置
2、最后一个桶只有一个元素，涉及到左右移动时，需要提前处理
```



```
	public static String alphabetBoardPath(String target) {
        char[] chars = target.toCharArray();
        int tIndex = 0; // 桶指针
        int pIndex = 0; // 桶内具体位置指针
        int tong = 0; // 桶号
        int p = 0; // 桶内位置号

        String res = "";
        for (char c : chars) {
            int num = c - 'a';
            p = num % 5; // 桶内目标位置
            tong = num / 5; // 桶

            // 移动桶
            String stong = tIndex >= tong ? "U" : "D"; // 上下方向
            int tmp1 = Math.abs(tIndex - tong);
            // 移动位
            String snum = pIndex >= p ? "L" : "R"; // 左右方向
            int tmp2 = Math.abs(pIndex - p);

            if (tong == 5 && Math.abs(p - pIndex) > 0) { // 针对最后一个z 进行处理，先进行左右移动，在进行上下移动
                while (tmp1 > 1) {
                    res += stong;
                    tmp1--;
                }
            } else {
                while (tmp1 > 0) {
                    res += stong;
                    tmp1--;
                }
            }

            while (tmp2 > 0) {
                res += snum;
                tmp2--;
            }

            if (tmp1 > 0) { // z 处理最后一次上下移动
                res += stong;
            }

            tIndex = tong; // 更新桶位置
            pIndex = p; // 更新移动位置

            res += "!";
        }
        return res;
    }
```

