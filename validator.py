import os

def compare(original,user_ans):
    for i in range(len(original)):
        if(original[i]!=user_ans[i]):
            return False
        
    return True
os.system("g++ code.cpp")
num_test_cases=10

for i in range(num_test_cases):

    data=os.popen("./a.out<test/test"+str(i)+".txt").read()
    user_ans=data.split("\n")
    original=[]
    with open("test/ans"+str(i)+".txt") as f:
        lis=(f.readlines())

    for k in lis:
        k=k[:-1]
        original.append(k)
    flag=True
    if(compare(original,user_ans)):
        print("Test Case {} Passed".format(str(i+1)))
    else:
        print("Test Case {} Failed".format(str(i+1)))
        Flag=False

if(flag):
    print("All test cases passed")
else:
    print("Some test cases failed")