# -*- coding: utf-8 -*-
class Dp1(object):                                     #动态规划类
    def __init__(self,n):                              #初始化
        self.mark = [0 for _ in xrange(n+1)]           #定义一个一维数组，初始化全部为0，长度为台阶数。用来当作“备忘录”。
        print self.dp(n)                               #开始递归
    def dp(self,n):                                    #递归的方法
        if self.mark[n] != 0:                          #先从备忘录寻找n，若存在mark[n]不等于0,则代表曾经计算过，n个台阶有mark[n]种跳法
            self.m = self.mark[n]                      #若备忘录有，则直接得到n层台阶的答案
            return self.m 
        
        elif n <= 1:                                   #从这里开始的四行是用来判断“边界问题”
            if n == 1:                                 #若刚好跳完台阶，则这样算一种方法
                self.m = 1                             #m变成1,代表是一种可行方法
            else:                                      
                self.m = 1                             
        
        elif n>1:                                      #这里两行是用于规划转移方程式（其实这里很简单），青蛙只有两种可能，跳一层或者跳两层。
            self.m = self.dp(n-2)+self.dp(n-1)         #当前n层台阶的解个数 等于 n-1层台阶的解 + n-2层台阶的解
        
        if n>=0:
            self.mark[n] = self.m                      #把m放入备忘录，下次若是再次是n层台阶，则不用计算直接取备忘录的数。（优化）

        return self.m                                  #返回
if __name__ == '__main__':
    dp1 = Dp1(10)
