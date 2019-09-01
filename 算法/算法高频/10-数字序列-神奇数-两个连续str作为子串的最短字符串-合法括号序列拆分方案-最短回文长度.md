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

实例1：数字序列

实例2：神奇数

实例3：两个连续str作为子串的最短字符串

实例4：合法括号序列拆分方案

实例5：最短回文长度

------

------

**实例1：数字序列**

东东从京京那里了解到有一个无限长的数字序列: 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, ...(数字k在该序列中正好出现k次)。

东东想知道这个数字序列的第n项是多少,你能帮帮他么輸入描述:

輸入包括一个整数n(1 <=n<=10^18)

输出描述：

输出一个整数，即数字序列的第n 项

示例1

输入169

输出18

```
/**
 * 1 22 333 4444 5555
 *
 * 每个连续数字的结尾
 * 1:1
 * 2:3
 * 3:6
 * 4:10
 * 5:15
 *
 * 每一个结尾，在这里可以看做是等差数列的求和
 * 例如
 * 6：是1+2+3
 * 15:是1+2+3+4+5
 * 即每个连续数的结尾数，是这个连续数的单数等差数列的和
 * 等差数列求和公式 S(n)= n*(n+1)/2
 *
 * 现在知道了这个 S(n) --> K 来反推这个连续数
 */
public class Code_34_NNum {

    public static int getNum(long n) {
        return (int) Math.ceil((Math.sqrt(1 + 8 * ((double) n)) - 1) / 2);
    }
}
```

**实例2：神奇数**

东东在一本古籍上看到有一种神奇数,如果能够将一个数的数字分成两组,其中一组数字的和等于另一组数字的和,我们就将这个数称为神奇数。例如242就是一个神奇数,我们能够将这个数的数字分成两组,分别是12,2}以及[4),而且这两组数的和都是4.东东现在需要统计给定区间中有多少个神奇数,即给定区间[1, r],统计这个区间中有多少个神奇数,请你来帮助他。

输入描述：

输入包括一行，一行中有两个整数L和R

输出描述:

输出一个整数,即区间内的神奇数个数

示例1输入1 50

输出4

```
import java.util.ArrayList;

/**
 * 思路：背包问题
 * 背包问题就是行是可选择的数，列是能组合成的各种可能结果
 */
public class Code_35_SplitNumberToTwoParts {
    /**
     * 将num 分解为独立的数
     * 求和，然后求是否能够组合成 sum/2
     * <p>
     * dp[][]
     */
    public static boolean isMagic(int num) {
        int sum = 0;
        ArrayList<Integer> nums = new ArrayList<>();
        while (num != 0) {
            int n = num % 10;
            nums.add(n);
            sum += n;
            num /= 10;
        }

        if ((sum & 1) == 1) return false; // 和是奇数无法加出 sum / 2
        sum = sum / 2;
        boolean[][] dp = new boolean[nums.size()][sum + 1];
        dp[0][0] = true;
        if (nums.get(0) <= sum) dp[0][nums.get(0)] = true; // 初始化第一行，只有第一个数时，这个数不能超过 sum
        for (int i = 1; i < nums.size(); i++) {
            for (int j = sum; j >= 0; j--) {
                dp[i][j] = dp[i - 1][j] || (j - nums.get(i) >= 0 ? dp[i - 1][j - nums.get(i)] : false);
            }
        }
        for (int i = 0; i < nums.size(); i++) {
            if (dp[i][sum]) {
                return true;
            }
        }
        return false;
    }

    /**
     * dp[]
     * 降维处理，节约空间资源
     *
     * 从右往左进行填充，不要从左往右进行填充，
     * i 表示第 i 行，那么从左往右填充时，它依赖的上一行的数已经改变
     * 例如
     *
     * 224
     *      0 1 2 3 4 5 6 7 8
     * 2    T F F T F F F F F
     * 2
     * 4
     *
     * 如上从左往右进行遍历时，i=1,arr[i]=2,那么j=5号位置的填充，
     * 需要依赖的是上一行i=0时的 j-arr[i]=3 和 5 两个位置，
     * 由于从左往右进行更新，那么 3 号位置的信息已经被修改，不再是原来上一行的信息了
     */
    public static boolean isMagic2(int num) {
        int sum = 0;
        int tmp = num;
        while (num != 0) {
            sum += num % 10;
            num /= 10;
        }

        if ((sum & 1) == 1) return false;// 奇数
        sum = sum / 2;

        boolean[] dp = new boolean[sum + 1];
        dp[0] = true;
        num = tmp;
        int cur = 0;
        while (num != 0) {
            cur = num % 10;
            for (int i = sum; i >= 0; i--) { // 从右往左进行填表
                dp[i] = dp[i] || (i - cur >= 0 ? dp[i - cur] : false);
            }
            if (dp[sum]) return true; // 只要加出sum 立即结束
            num /= 10;
        }
        return false;
    }

    public static void main(String[] args) {
        for (int i = 0; i < 100000; i++) {
            int num = (int) (Math.random() * 100000 + 1);
            try {
                if (num != 0 && isMagic(num) != isMagic2(num)) {
                    System.out.println(num);
                    System.out.println(isMagic(num));
                    System.out.println(isMagic2(num));
                }
            } catch (Exception e) {
                System.out.println(num + "\t\t" + e.toString());
            }
        }
    }
}
```

**实例3：两个连续str作为子串的最短字符串**

给定一个字符串s,请计算输出含有连续两个s作为子串的最短字符串。注意两个s可能有重叠部分。例如, "ababa"含有两个"aba"输入描述:输入包括一个字符串s,字符串长度length (1 <=ength <= 50), s中每个字符都是小写字母.输出描述:输出一个字符串,即含有连续两个s作为子串的最短字符串。

示例1输入abracadabra

输出abracadabracadabra



具体意思就是给定一个字符串Str=“abcdd" 输出含有两个Str的字符串

**KMP算法**

**字符串查找算法，简称为 “KMP算法”，常用于在一个文本串S内查找一个模式串P 的出现位置**

KMP算法 解决 str1 中是否包含 str2
包含返回 str2 开始位置，不包含返回 -1

1、暴力方法：以str1 的每一个字符去 匹配str2 的每一个字符，str1长N, str2长M,时间复杂度 O(M*N)
2、KMP算法 str1长N, str2长M 可以优化到 O(N) N > M

**开始了解KMP算法前，先了解最长前缀和最长后缀匹配**

注意：**最长前缀和最长后缀匹配**不是针对 str1 的，是针对str2的

一个例子理解：最长前缀和最长后缀匹配

aaaab 求 其中 b 的最长前缀和最长后缀匹配

```
aaaab

长度	前缀	后缀
1	a	a
2	aa	aa
3	aaa	aaa
那么字符串aaaab 中 b 的最长前缀和最长后缀匹配就是 aaa ，长度为3
其中前缀不能冲到 aaaa 长度为4位置，同理后缀
```

**人为规定**
**前缀不能包含最后一个字符**
**后缀不能包含第一个字符**

求一个字符串中每一个字符的最长前缀和最长后缀匹配，用next[] 记录

```
str:	a	a	a	a	a
next[]	-1	0	1	2	3
```

时间复杂度分析

1、未断掉，Str1直接匹配出Str2

2、断掉

未断掉，走的就是 Str2 的长度 ，时间复杂度 O(N)

断掉，一旦断掉Str2 的开始指针就前移一位，知道结束，时间复杂度也是 O(N)

**next[] 怎么求？**

人为规定 0 位置：-1；1位置：0

其他位置 ，当求解 i 位置的时候，可以认为 0~i 位置的已经求解完毕。

```
import java.util.Arrays;

/**
 * @description: 连续Str子串的最短字符串
 * @version: 1.0
 */
public class Code_36_ShortestHaveTwice {

    public static String answer(String str) {
        if (str == null || str.length() == 0) return "";
        char[] chars = str.toCharArray();
        if (chars.length == 1) return str + str;
        if (chars.length == 2) // ab -->  aba是最短的
            return chars[0] == chars[1] ? (str + String.valueOf(chars[0])) : str + str;
        int endNext = endNextLength(chars);
        return str + str.substring(endNext);
    }

    // 求next[]
    private static int endNextLength(char[] chars) {

        int[] next = new int[chars.length + 1];
        next[0] = -1;
        next[1] = 0; // 人为规定0：-1 ，1:0
        int position = 2; // 指向chars[] 的第position位置的元素
        int cn = 0; // 指向next[] 最长前缀和后缀匹配位置
        while (position < next.length) {
            if (chars[position - 1] == chars[cn]){
                next[position++] = ++cn;
            } else if (cn > 0) {
                cn = next[cn];
            } else {
                next[position++] = 0;
            }
        }

        System.out.println(Arrays.toString(next));
        return next[next.length - 1];
    }


    /**
     * KMP算法
     * KMP算法 解决 str1 中是否包含 str2
     * 包含返回 str2 开始位置，不包含返回 -1
     *
     * 1、暴力方法：以str1 的每一个字符去 匹配str2 的每一个字符，str1长N, str2长M,时间复杂度 O(M*N)
     * 2、KMP算法 str1长N, str2长M 可以优化到 O(N) N > M
     *
     * 此题仅仅使用了KMP 算法中的 next[] 的应用
     */
    public static void main(String[] args) {
        String test1 = "a";
        System.out.println(answer(test1));

        String test2 = "aa";
        System.out.println(answer(test2));

        String test3 = "ab";
        System.out.println(answer(test3));

        String test4 = "abcdabcd";
        System.out.println(answer(test4));

        String test5 = "abracadabra";
        System.out.println(answer(test5));
        System.out.println("abracadabra".substring(4)); // 保留 i+1~length-1位置
    }
}
```

**实例4：合法括号序列拆分方案**

合法的括号匹配序列被定义为:、

1.空串""是合法的括号序列

2.如果" "和"Y"是合法的序列,那么"XY"也是一个合法的括号序列

3,如果"X"是一个合法的序列,那么"(X) "也是一个合法的括号序列

4,每个合法的括号序列都可以由上面的规则生成例如"", "()", "() () ()", "(() ())", "(((0))"都是合法的。

东东现在有一个合法的括号序列s,一次移除操作分为两步: 

1·移除序列s中第一个左括号

2,移除序列s中任意一个右括号保证操作之后s还是一个合法的括号序列

东东现在想知道使用上述的移除操作有多少种方案可以把序列s变为空

如果两个方案中有一次移除操作移除的是不同的右括号就认为是不同的方案。例如: s= "() () () () ()",输出1,因为每次都只能选择被移除的左括号所相邻的右括号.s= "(((()))) ,输出24,第一次有4种情况,第二次有3种情

输入描述：

输入包括一行，一个合法的括号序列s，序列长度 <=20

输出描述：

输出一个整数，表示方案数。

```
(((())))
4*3*2*1=24
```



```
思路：
求每一个左括号，右括号比左括号多多少
( ( ( ) ) )
1 2 3

从右向左进行遍历，维护一个sum ， 遇到右括号++，左括号--
```

查看一个单独的合法括号序列移除方案

```
( ( ( ) ) )
第一个( 可以支配的右括号是3个
第二个( 可以支配的右括号是2个
第三个( 可以支配的右括号是1个

( ( ( ) ) )
3 2 1

所以这个合法括号序列移除方案是3*2*1个

其实统计出每一个左括号位置，右括号比左括号多多少，逆序就是每一个( 可以支配的括号数
```

```
public class Code_37_Parentheses {
    /**
     * 维护一个sum 变量，遇到 ) ,sum++，遇到 ( sum--
     *
     * 思路：
     * 求每一个左括号，右括号比左括号多多少
     * ( ( ( ) ) )
     * 1 2 3
     *
     * 从右向左进行遍历，维护一个sum ， 遇到右括号++，左括号--
     *
     * 查看一个单独的合法括号序列移除方案
     * ( ( ( ) ) )
     * 第一个( 可以支配的右括号是3个
     * 第二个( 可以支配的右括号是2个
     * 第三个( 可以支配的右括号是1个
     *
     * ( ( ( ) ) )
     * 3 2 1
     *
     * 所以这个合法括号序列移除方案是3*2*1个
     * 其实统计出每一个左括号位置，右括号比左括号多多少，逆序就是每一个( 可以支配的括号数
     */
    public static int possibilities(String parentheses) {
        char[] chars = parentheses.toCharArray();
        int ans = 1;
        int sum = 0;
        for (int i = chars.length - 1; i >= 0; i--) {
            if (chars[i] == ')'){
                sum++;
            } else {
                ans *= sum--;
            }
        }
        return ans;
    }

    public static void main(String[] args) {
        System.out.println(possibilities("((()))")); // 6
        System.out.println(possibilities("()(())")); // 2
        System.out.println(possibilities("()()()")); // 1
    }
}
```

**实例5：最短回文长度**

京京和东东是好朋友。东东很喜欢回文。回文是指从前往后读和从后往前读是一样的词语。京京准备给东东一个惊喜,先取定一个字符串s,然后在后面附上0个或者更多个字母形成回文,京京希望这个回文越短越好。请帮助京京计算他能够得到的最短的回文长度。

输入描述:输入包括一个字符串s,字符串s长度length (1 <=length<= 50)

输出描述:输出一个整数,表示牛牛能够得到的最短的回文长度。

示例1输入 abab输出 5



```
import java.util.Arrays;

/**
 * @description: 最短回文长度
 */
public class Code_38_ShortestMakePalindrome {

    /**
     * 思路：必须包含最后一个字符的情况下，求最长的回文子串，其中，不是回文串的范围字符，逆序填在后面即可
     * 如 abc1234321
     * 必须包含最后一个字符 4 的情况下，最长的回文子串是 1234321
     * 将不包含在最长回文子串内的其他字符abc逆序cba --> 添加在后面  abc1234321cba
     *
     * 算法被分解为，怎么求一个字符串的最长回文子串，子串要求连续
     * 1、暴力解
     * 以每一个字符向两边进行扩散
     * 121
     *  null<-1->2     ---->0
     *  1<-2->1        ---->3
     *  2<-1->1        ---->0
     *  所以扩散的最长回文长度就是 3
     *  但是问题来了，对于这种对称扩散寻找，121 奇数个，是以实轴进行的扩散，
     *  然而 1221 偶数个，是虚轴扩散才能找到真正的值4，不然就是 0
     *
     *  处理方式：不管是奇数个还是偶数个，都进行扩容处理，求解完毕后除以 2 得到的就是解
     *  121 --> #1#2#1#  最长对称是 7  7/2=3
     *  1221--> #1#2#2#1# 最长对称是 9  9/2=4
     *
     *  注意：添加的字符是 任意的，可以是存在的字符，如 2，不影响相对的结果
     *  时间复杂度 O(N^2)
     *
     *
     * 2、Manacher 算法
     *
     * 1）、回文半径：以每个位置的字符为回文中心求出的回文半径长度；
     *      维护一个回文半径数组，记录每一个位置可以扩散的回文半径
     * 2）、回文最右边界：这个位置及之前的位置的回文子串，所到达的最右边的地方，同时记录最右回文中心；
     *      如果有两个位置扩散到同一个右边界，只记录最早的那个。
     *
     *      如  # 1 # 2 # 2 # 1 #
     *          0 1 2 3 4 5 6 7 8
     *          4号位置# 的回文最右边界达到了8号位置
     *          7号位置1 的回文最右边界达到了8号位置
     *          最右回文中心只记录 4 号位置，不记录 7 号位置
     *
     *算法出现的几种情况
     * a、当前所求的位置，不在左右边界里，此时和暴力方法一样，向两边依次检查
     *      如  # 1 # 2 # 2 # 1 #
     *          0 1 2 3 4 5 6 7 8
     *          0号位置，不在边界，扩
     *          1号位置，不在边界，向两边依次检查，扩到了2 号位置，此时更新左右边界为 2
     * b、在最右回文右边界里面
     * c、在最右回文右边界外
     * d、压线
     *
     * 其中一点就是找到回文的最右边界就停, 同时记录这个最大的回文半径
     *
     */

    // 预处理字符串，排除奇偶个字符的影响
    public static char[] getPreprocessedStr(String str){
        char[] tmp = new char[str.length() * 2 + 1];
        int j = 0;
        for (int i = 0; i < tmp.length; i++) {
            if ((i & 1) == 0) {
                tmp[i] = '#';
            } else {
                tmp[i] = str.charAt(j);
            }
            tmp[i] = (i & 1) == 0 ? '#' : str.charAt(j++);
        }
        return tmp;
    }

    public static int manacherStr(String str) {
        if (str == null || str.length() == 0) return 0;

        char[] preArr = getPreprocessedStr(str);// 预处理字符串，排除奇偶影响

        int index = -1; // 最右回文对称中心
        int maxR = -1; // 最右回文延伸边界
        int max = -1; // 最大延伸长度
        int[] radius = new int[preArr.length]; // 记录每个字符可以延伸的最大回文边界

        for (int i = 0; i < preArr.length; i++) {
            // 找到当前点关于最右回文对称中心的对称点位置
//            int symmetryNode = radius[2 * index - i];
            // 当前点的状态，1、在最右回文边界之外，暂时假设只有自己是回文字符串，记录为1
            // 2、在最右回文边界之内，记录为对称点的回文边界和最右边界-i 中最小的
            radius[i] = maxR > i ? Math.min(radius[2 * index - i], maxR - i) : 1;

            // 检查并更新当前下标为中心的回文串最远延伸的长度
            while (i + radius[i] < preArr.length // 当前位置扩出的最大右边界不能超出数组范围
                && (i - radius[i] + 1) > 0 // 当前位置存在左边点 ：i-radius[i] <-i-> i+radius[i], 可以继续向两边扩
            ) {
                // 继续向外扩充，寻找最大的回文半径
                if (preArr[i + radius[i]] == preArr[i - radius[i]]){
                    radius[i]++;
                } else {
                    break;
                }
            }

            if (i + radius[i] > maxR) {
                maxR = i + radius[i]; // 更新最大回文右边界
                index = i; // 更新最大回文右边界
            }

            if (maxR == preArr.length) { // 最大回文右边界已经扩到了最后一个字符
                max = radius[i]; // 记录最大回文半径
                break;
            }

            System.out.println(Arrays.toString(radius));
        }

        System.out.println("max: " + max);
        return str.length() * 2 - max + 1;
    }

    public static void main(String[] args) {
        System.out.println(manacherStr("abb"));
    }
}
```