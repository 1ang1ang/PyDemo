# -*- encoding:utf-8 -*-
from com.guoyang.util.Constants import *
import os
import pandas

def createFile():
    with open(FILE_NAME, "a+") as f:
        f.read()
        f.seek(0)
        f.write("this is a new text2")
# createFile()

def deleteFile():
    os.remove(FILE_NAME)
# deleteFile()

def readAndWriteFile():
    with open(FILE_NAME, "w+") as f:
        arr=["hello","world"]
        for s in arr:
            f.writelines(s + "\n")
        f.seek(0)
        dst = f.readlines()
        print(dst)
# readAndWriteFile()

# 通过遍历计算协议消耗平均时长~并且排序输出
def handleLog():
    print("waiting...")
    with open(LOG_NAME, "r", -1, "utf-8") as f:
        print(f.name)
        wordCount={}
        wordTime={}
        allLines=f.readlines()
        for line in allLines:
            if line.find("|CMD|") < 1:
                continue
            lineArr = line.split("|")
            if not wordCount.get(lineArr[6]):
                wordCount[lineArr[6]] = 0
                wordTime[lineArr[6]] = 0
            wordCount[lineArr[6]] = wordCount[lineArr[6]] + 1
            wordTime[lineArr[6]] = wordTime[lineArr[6]] + int(lineArr[8])
        for protocol in wordTime.keys():
            wordTime[protocol] = wordTime[protocol] / wordCount[protocol]

        print(sorted(wordTime.items(), key=lambda e:e[1],reverse=True))
# handleLog()

# 使用pandas统计日志平均时长
def handleLogWithPandas():
    help(pandas.read_table)
handleLogWithPandas()