# -*- coding: utf-8 -*-

import math
import collections
import functools

#basic function
aInt = 100;
def testPlus(aInt):
    print(aInt * 23)
#testPlus(aInt)

#basic lambda function
result = lambda a: a * 24;
#print(result(aInt))

#get prime count within one num
def getPrime(max):
    primeCount = 0
    for i in range(2,max + 1):
        if isPrime(i):
            print(i," is prime")
            primeCount += 1
    print("sum prime count is ", primeCount)
def isPrime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

#getPrime(100)

#false judge test
def falseJudge():
    if (3>4) == 0:
        print("111")
    if []:
        print("free array")

#new line test
def newLine():
    print('''hello
world''')
    print('hello \
world')
    print('hello \n world')

#newLine()

#generator and List Comprehensions
def announceFunction():
    L= [j for j in range(10) if j %2 == 0]
    print(L)
    K= (j for j in range(10))
    for n in K:
        print(n,end=" ")

# announceFunction()

#function with default param
def defaultParam(first,second=123):
    if second > 100:
        print("second big than 100,first is ", first)
    else:
        print("second little than 100, first is ", second)

# defaultParam("hahaha",1)

#slice
def slice():
    a=[1,2,3,4,5,6,7,8,9]
    print(a[1:4])
    print(a[-2:-1])
    print(a[-2:])
    print(a[:8:3])
# slice()

# iteration function
def iteration():
    str = 'ABCDEFGHIJKLMN'
    print(isinstance(str,collections.Iterable))
    for c in str:
        print(c)
    arr = ['a','b','c']
    for a in arr:
        print(a)
    dic=enumerate(arr)
    for key,value in dic:
        print(key,' ',value)
# iteration()

#function program
def functionProgram(f):
    f
# functionProgram(defaultParam(1111))
# defaultParam(2222)

# map reduce usage
def handleNum(higher,lower):
    return higher * 10 + lower
def mapReduce(s):
    return functools.reduce(handleNum, map(int,s))
# print(mapReduce('123334'))

# filter
def isOdd(num):
    return num % 2 ==1
# print(list(filter(isOdd, range(10))))
# print(list(filter(isPrime, range(2,100))))
# one way
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n
def _not_divisible(n):
    return lambda x: x % n > 0
def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列
def get100Prime():
    # 打印100以内的素数:
    for n in primes():
        if n < 100:
            print(n)
        else:
            break
# get100Prime()

def exceptionCatch():
    try:
        a = 1 / 1
    except :
        print("111")
    else:
        print("else block")
exceptionCatch()