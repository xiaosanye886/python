print ("hello world")

'''
1:
关于Python的一些细节

1、容器列表的切片索引正向是从0开始，反向是从-1开始，如
ll = [1,2,3,4,5]
ll[0:2] = [1,2]
ll[-1:-2] = [5]

ll2 = ll 不会创建一个新的列表，只是ll和ll2都指向同样的数据
ll2 = ll[:]将创建一个新的列表，彼此互不影响

ll = [1,2,3]
ll2 = ll
ll2 [2] = 4
print(ll)
print(id(ll),id(ll2))
'''
'''
常用函数：
1: divmod(7, 2)
>>(3, 1)  输出商和余数

2: staticmethod() 静态函数，不用实例化直接调用
class C(object):
    @staticmethod
    def f():
        print('runoob');
 
C.f();          # 静态方法无需实例化
cobj = C()
cobj.f()        # 也可以实例化后调用

3： all()  序列所有为true则返回true  >>> all(['a', 'b', 'c', 'd'])  # 列表list，元素都不为空或0  True
   /any() 序列所有为空则返回fales 否则为true  any(['a', 'b', '', 'd'])   # 列表list，存在一个为空的元素 True
   >>> any([0, '', False])        # 列表list,元素全为0,'',false  False

4：enumerate  遍历索引和对应值 
    >>>seq = ['one', 'two', 'three']
    >>> for i, element in enumerate(seq):
    ...     print i, element
    ... 
    0 one
    1 two
    2 three
    
5： ord() 返回对应的ascii  ord('a') = 97

6：isinstance() 与 type() 区别：

    type() 不会认为子类是一种父类类型，不考虑继承关系。

    isinstance() 会认为子类是一种父类类型，考虑继承关系。

    如果要判断两个类型是否相同推荐使用 isinstance()。
    class A:
    pass
 
    class B(A):
        pass
     
    isinstance(A(), A)    # returns True
    type(A()) == A        # returns True
    isinstance(B(), A)    # returns True
    type(B()) == A        # returns False
    
7：执行其他文件　execfile('hello.py')

8：issubclass（Ｂ，Ａ）判断ｂ是否是ａ的子类
    class A:
        pass
    class B(A):
        pass
        
    print(issubclass(B,A))    # 返回 True
    
    
9：super() 函数是用于调用父类(超类)的一个方法。调用父类的方法，（构造函数或者其他函数）
    class A(object):   # Python2.x 记得继承 object
        def add(self, x):
             y = x+1
             print(y)
    class B(A):
        def add(self, x):
            super(B, self).add(x)
    b = B()
    b.add(2)  # 3
    
10：filter（函数，序列）
    def is_odd(n):
        return n % 2 == 1
     
    newlist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(newlist)
    输出结果 ：
    [1, 3, 5, 7, 9]

11：　callable() 函数用于检查一个对象是否是可调用的。
    >>> def add(a, b):
    ...     return a + b
    ... 
    >>> callable(add)             # 函数返回 True

12：classmethod 修饰符对应的函数不需要实例化
    class A(object):
    bar = 1
    def func1(self):  
        print ('foo') 
    @classmethod
    def func2(cls):
        print ('func2')
        print (cls.bar)
        cls().func1()   # 调用 foo 方法
 
    A.func2()               # 不需要实例化

13： getattr() 函数用于返回一个对象属性值。类似于获取类的数据成员　hasattr() 函数用于判断对象是否包含对应的属性。setattr() 函数对应函数 getattr()，用于设置属性值，该属性不一定是存在的。

14： lambda 匿名函数 map(lambda x: x ** 2, [1, 2, 3, 4, 5])  # 使用 lambda 匿名函数、

15： cmp(x,y) 函数用于比较2个对象，如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1。

16：reverse() 函数用于反向列表中元素

17：hash() 用于获取取一个对象（字符 串或者数值等）的哈希值。hash('test')            # 字符串
    2314058222102390712
    
18: set() 函数创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等。

19: hex() 函数用于将10进制整数转换成16进制，以字符串形式表示。

20: CPython 中 id() 函数用于获取对象的内存地址。
21:　oct() 函数将一个整数转换成8进制字符串。
22: sorted() 函数对所有可迭代的对象进行排序操作。

    sort 与 sorted 区别：
    
    sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。
    
    list 的 sort 方法返回的是对已经存在的列表进行操作，无返回值，而内建函数 sorted 方法返回的是一个新的 list，
     而不是在原来的基础上进行的操作。
    '''