#!/usr/bin/python
import time
import Queue
import signal
import sys
import requests
from datetime import datetime
from threading import Thread
from SF_9DOF import IMU

class WorkerThread(Thread):
	"""docstring for WorkerThread"""
	def __init__(self,imuQueue,emgQueue,deviceid):
		Thread.__init__(self)
		self.exit = False
		self.imuQueue = imuQueue
		self.emgQueue = emgQueue
		self.deviceid = deviceid
		self.imu = IMU()
		self.imu.enable_accel()
		self.imu.enable_mag()
		self.imu.enable_gyro()
		self.imu.accel_range("2G")
		self.imu.mag_range("2GAUSS")
		self.imu.gyro_range("245DPS")
	def run(self):
		global exit
		start = time.time()
		while(self.exit==False):
			if(((time.time()-start)*1000)%50==0):#every 1/20 seconds
				self.imu.read_accel()
				self.imu.read_mag()
				self.imu.read_gyro()
				self.imuQueue.put({"deviceid":self.deviceid, 
"record_time":datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'),"accX":self.imu.ax,"accY":self.imu.ay,"accZ":self.imu.az,"gyroX":self.imu.gx,"gyroY":self.imu.gy,"gyroZ":self.imu.gz,"magX":self.imu.mx,"magY":self.imu.my,"magZ":self.imu.mz})
				self.emgQueue.put({"deviceid":self.deviceid, 
"record_time":datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'),"mag":1})
	def stop(self):
		self.exit = True


def main():
    imuQueue = Queue.Queue()
    emgQueue = Queue.Queue()
    deviceid=1
    reader = WorkerThread(imuQueue,emgQueue,deviceid)
    reader.start()
    try:
        while True:
            count = 0
            imuData = []#TODO: should this instanciation happen outside to save time?
            emgData = []
            while(imuQueue.empty() == False):#get all available data
                count = count + 1
                imuData.append(imuQueue.get(timeout = 0.5))
            try:#then send
                r = requests.post('http://127.0.0.1:5000/IMUData', json=imuData)
            except requests.ConnectionError:
                print("could not connect to server")

            while(emgQueue.empty() == False):
            	emgData.append(emgQueue.get(timeout = 0.5))
            try:
            	r = requests.post('http://127.0.0.1:5000/EMGData', json=emgData)
            except requests.ConnectionError:
            	print("could not connect to server")

            print("sent "+str(count)+" packets")
            time.sleep(1)
    except KeyboardInterrupt:
        print("exit")
        reader.stop()



if __name__ == "__main__":
    main()

		
