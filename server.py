from flask import Flask,render_template,request
import subprocess
import json
import asyncio
import websockets
from validator import *

app=Flask(__name__)
num=5
async def validate(websocket,path):
    message=await websocket.recv()
    for i in range(num):
        if(validater(i)):
            await websocket.send("Test case {} Passed".format(str(i+1)))
        else:
            await websocket.send("Test case {} Failed".format(str(i+1)))


@app.route("/test")
def test():
    msg=request.args.get('msg')
    print(msg)
    for i in range(num):
        if(validater(i)):
            print("Test case {} Passed".format(str(i+1)))
        else:
            print("Test case {} Failed".format(str(i+1)))
    #start_server=websockets.serve(validate,"localhost",12345)
    #asyncio.get_event_loop().run_until_complete(start_server)
    #asyncio.get_event_loop().run_forever()
# //intialize serer start
    return "passed"

def create(content):
    with open("code.cpp",'w') as f:
        f.write(content)

@app.route("/code")
def code():
    return render_template("code.html")

@app.route("/result")
def results():
    return render_template("results.html")

@app.route("/ajax",methods=['POST'])
def compilation():
    req_data = request.get_json()
    create(json.loads(req_data)['code'])
    command='g++ code.cpp'
    res=subprocess.getoutput(command)
    if(len(res)==0):
        return "success"
    else:
        return "fail"
# app.route
#    listen websocket
#    validator
#    string s;
#    send
#    agla
if __name__=="__main__":
    app.run(debug=True)