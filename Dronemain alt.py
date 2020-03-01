#import libraries
import DroneIO
import time
import sys
import socket
import math
from twisted.internet import task, reactor
# setup all variables, functions / one time setup:
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('127.0.0.1', 10000)
print("Starting up on "+str(server_address))
sock.bind(server_address)
timeout = 0.01
sock.listen(2)
connection, client_address = sock.accept()
drone = DroneIO.DroneControl()


#Coefficent of motor speed (Changes setting of motors based on the drone weight/thrust ration) Note 4000 is the thrust
thrustWeight = (500/4000)
# Array controlling thrust modifications by the systems
thrustArray = {"frontLeft":{"upDown":0,"yaw":0,"roll":0,"pitch":0},
"frontRight":{"upDown":0,"yaw":0,"roll":0,"pitch":0,},
"backLeft": {"upDown":0,"yaw":0,"roll":0,"pitch":0,},
"backRight": {"upDown":0,"yaw":0,"roll":0,"pitch":0,},
}


#called when W key pressed on controlling computer - Forwards (Axis Forward-Back X)
def WKey(drone):

    return
#called when S key pressed on controlling computer - Right (Axis Left-Right Z)
def SKey(drone):

    return
#called when A key pressed on controlling computer - Left (Axis Left-Right Z)
def AKey(drone):

    return
#called when D key pressed on controlling computer - Backwards (Axis Forward-Back X)
def DKey(drone):

    return
#called when Z key pressed on controlling computer - Drone Down (Axis Forward-Back Y)
def ZKey(drone):

    return
#called when X key pressed on controlling computer - Drone Up (Axis Forward-Back Y)
def XKey(drone):

    return
#called when Q key pressed on controlling computer - Spin Left (Rotation XY - <XOY )
def QKey(drone):

    return
#called when E key pressed on controlling computer - Spin Right (Rotation XY - <XOY )
def EKey(drone):

    return
#called when Left Arrow key pressed on controlling computer - Roll Left (Rotation ZY - <ZOY )
def LAKey(drone):

    return
#called when Right Arrow key pressed on controlling computer - Roll Right (Rotation ZY - <ZOY )
def RAKey(drone):

    return
#called when Up Arrow key pressed on controlling computer - Pitch Up (Rotation ZX - <ZOX )
def UAKey(drone):

    return
#called when Down Arrow key pressed on controlling computer - Pitch Down (Rotation ZX - <ZOX )
def DAKey(drone,thrustWeight,thrustArray):

    return
def upDown(drone,thrustWeight,thrustArray):

    return
def yaw(drone,thrustWeight,thrustArray):

    return
def roll(drone,thrustWeight,thrustArray):

    return

def pitch(drone,thrustWeight,thrustArray):

    return
def getMotorValues(drone, thrustWeight,controlJur,thrustMod,x,i,moddedThrust):
    if i == 1:
     m = thrustArray['frontLeft']
    elif i == 2:
        m = thrustArray['frontRight']

    elif i == 3:
        m = thrustArray['backLeft']

    else:
        m = thrustArray['backRight']
     # "upDown":0,"yaw":0,"roll":0,"pitch":0
    x = max(min(m[upDown] + m[yaw] + m[roll] +m[pitch] +thrustweight*100),100),0)


    return
#For Processing Accelerometer data
def motorControl(drone,thrustWeight,controlJur,thrustMod,moddedThrust,thrustArray):
    x = 0
    upDown(drone,thrustWeight,thrustArray)
    yaw(drone,thrustWeight,thrustArray)
    roll(drone,thrustWeight,thrustArray)
    pitch(drone,thrustWeight,thrustArray)
    for i in range(1,4):
        x = 0
        getMotorValues(drone,thrustWeight,controlJur,thrustMod,x,i,moddedThrust)
        drone.setMotor(i,x)

    return

#store starting time
starttime=time.time()
# begin function loop
def MainLoop(thrustWeight, thrustMod):
    incoming = connection.recv(1024)
    print("Received MSG: %s" % incoming.decode('utf-8'))
    message = incoming.decode('utf-8')
    #check all keys pressed
    if message == "w":
        WKey(drone)
    if message == "a":
        AKey(drone)
    if message == "s":
        SKey(drone)
    if message == "d":
        DKey(drone)
    if message == "x":
        XKey(drone)
    if message == "z":
        ZKey(drone)
    if message == "q":
        QKey(drone)
    if message == "e":
        EKey(drone)
    if message == "la":
        LAKey(drone)
    if message == "ra":
        RAKey(drone)
    if message == "ua":
        UAKey(drone)
    if message == "da":
        DAKey(drone)
    motorControl(drone,thrustWeight,controlJur,thrustMod,moddedThrust)

#begin MainLoop cycle
taskloop = task.LoopingCall(MainLoop)
taskloop.start(timeout)

reactor.run()
