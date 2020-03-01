
import PID
import time
import os.path

class MainPID:
    """MainPID contains the code to run all PID systems for the drone"""
    
    def createConfig ():
	    if not os.path.isfile('/Dronecode/DroneIO/pid.conf'):
		    with open ('/Dronecode/DroneIO/pid.conf', 'w') as f:
			    f.write('%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s'%(targetP,PP,PI,PD,targetR,RP,RI,RD,targetY,YP,YI,YD))
    def readConfig (x):
	    global targetT
        # 0 = pitch 1 = roll 2 = yaw
	    with open ('/Dronecode/DroneIO/pid.conf', 'r') as f:
		    config = f.readline().split(',')Dronecode
		    pid.SetPoint = float(config[0+x*3])
		    targetT = pid.SetPoint
		    pid.setKp (float(config[1+x*3]))
		    pid.setKi (float(config[2+x*3]))
		    pid.setKd (float(config[3+x*3]))
    
    def pitch (targetAngle,measuredAngle)
        #THIS is not yet functional
        
        P = 10
        I = 1
        D = 1

        pid = PID.PID(P, I, D)
        pid.SetPoint = targetT
        pid.setSampleTime(1)


	    temperature = (a0 - 0.5) * 100

	    pid.update(temperature)
	    targetPwm = pid.output
	    targetPwm = max(min( int(targetPwm), 100 ),0)

	    print "Target: %.1f C | Current: %.1f C | PWM: %s %%"%(targetT, temperature, targetPwm)

	    # Set PWM expansion channel 0 to the target setting
	    pwmExp.setupDriver(0, targetPwm, 0)
	    time.sleep(0.5)