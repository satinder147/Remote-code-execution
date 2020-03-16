import os
import sys

def compare(original,user_ans):
    for i in range(len(original)):
        if(original[i]!=user_ans[i]):
            return False
        
    return True

def validater(i):
    data=os.popen("./a.out<test/test"+str(i)+".txt").read()
    user_ans=data.split("\n")
    original=[]
    with open("test/ans"+str(i)+".txt") as f:
        lis=(f.readlines())
    for k in lis:
        k=k[:-1]
        original.append(k)
    #print(original)
    #print(user_ans)
    if(compare(original,user_ans)):
        return True
    else:
        return False

