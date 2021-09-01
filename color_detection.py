# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 12:07:27 2021

@author: Ayan
"""

from collections import deque
from opcua import Client
import numpy as np
import argparse
import imutils
import cv2
import urllib 

def startLogging(ip,username,password,rate,path):
                print("Starting")
                print(ip)
                print(username)
                print(password)
                print(rate)
                print(path)
                url = "opc.tcp://192.168.1.20:4840" 
                client = Client(url)
                #KUKA_OPC_UA_Logger_GUI.gui.setEntry("Logging Status","Logging Started")
                #KUKA_OPC_UA_Logger_GUI.startbutton = "Logging Active"
                print("try session connect")
                client.set_user("opcuaoperator")
                client.set_password("kuka")
                print("session success")
                client.connect()
                print("Client Connected to KUKA OPC Server")
url = "opc.tcp://192.168.1.20:4840"
client = Client(url)
print("try session connect")
client.set_user("opcuaoperator")
client.set_password("kuka")
print("session success")
client.connect()
print("Client Connected")
variableid1 = client.get_node("ns=5;s=MotionDeviceSystem.ProcessData.R1.System.$config.REACHPOS")
red = client.get_node("ns=5;s=MotionDeviceSystem.ProcessData.R1.System.$config.RED")
blue = client.get_node("ns=5;s=MotionDeviceSystem.ProcessData.R1.System.$config.BLUE")
green = client.get_node("ns=5;s=MotionDeviceSystem.ProcessData.R1.System.$config.GREEN")
yellow = client.get_node("ns=5;s=MotionDeviceSystem.ProcessData.R1.System.$config.YELLOW")
orange = client.get_node("ns=5;s=MotionDeviceSystem.ProcessData.R1.System.$config.ORANGE")
#pir= client.get_node("ns=5;s=MotionDeviceSystem.ProcessData.R1.System.$config.CONVEYORSENSOR2")
#input()
ap = argparse.ArgumentParser()
# ap.add_mutually_exclusive_group("-b", type=int, default=64)

ap.add_argument("-v", "--video", help="path to the (optional) video file")
ap.add_argument("-b", "--buffer", type=int, default=64, help="max buffer size")
args = vars(ap.parse_args())
 


lower = {'red':(166, 84, 141), 'green':(66, 122, 129), 'blue':(97, 100, 117), 'yellow':(23, 59, 119), 'orange':(0, 50, 80)} 
upper = {'red':(186,255,255), 'green':(86,255,255), 'blue':(117,255,255), 'yellow':(54,255,255), 'orange':(20,255,255)}
 

colors = {'red':(0,0,255), 'green':(0,255,0), 'blue':(255,0,0), 'yellow':(0, 255, 217), 'orange':(0,140,255)}
 

if not args.get("video", False):
    if(variableid1==True):
        camera = cv2.VideoCapture(0)

else:
    camera = cv2.VideoCapture(args["video"])

while True:

    (grabbed, frame) = camera.read()
    if args.get("video") and not grabbed:
        break
 
 
    frame = imutils.resize(frame, width=900)
 
    blurred = cv2.GaussianBlur(frame, (11, 11), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

    for key, value in upper.items():
    
        kernel = np.ones((9,9),np.uint8)
        mask = cv2.inRange(hsv, lower[key], upper[key])
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
               
    
        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE)[-2]
        center = None
       


        if len(cnts) > 0:
            
            c = max(cnts, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            M = cv2.moments(c)
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
       

            if radius > 0.5:
            
                cv2.circle(frame, (int(x), int(y)), int(radius), colors[key], 5)
                cv2.putText(frame,key + "color", (int(x-radius),int(y-radius)), cv2.FONT_HERSHEY_SIMPLEX, 0.6,colors[key],2)
                if(colors[key]=='red'):
                    red.set_value(1.0)
                elif(colors[key]=='blue'):
                    blue.set_value(1.0)
                elif(colors[key]=='green'):
                    green.set_value(1.0)
                elif(colors[key]=='yellow'):
                    yellow.set_value(1.0)
                elif(colors[key]=='orange'):
                    orange.set_value(1.0)
    cv2.imshow("Frame", frame)
   
    key = cv2.waitKey(1) & 0xFF
    # press 'q' to stop the loop
    if key == ord("q"):
        break
 
camera.release()
cv2.destroyAllWindows()