#!/usr/bin/python

import time
import pigpio
import DHT22
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTShadowClient

# Edit this to be the awshost you got from `aws iot describe-endpoint`
awshost = "a1v9yu6xvaswb1.iot.ap-southeast-2.amazonaws.com"

# Edit this to be your device name in the AWS IoT console
thing = "pi"

if __name__ == "__main__":
	pi = pigpio.pi()
	s = DHT22.sensor(pi, 22, LED=16, power=8)

	awsport = 8883
	caPath = "aws-iot-rootCA.crt"
	certPath = "cert.pem"
	keyPath = "privkey.pem"

	# For certificate based connection
	myShadowClient = AWSIoTMQTTShadowClient(thing)
	myShadowClient.configureEndpoint(awshost, awsport)
	myShadowClient.configureCredentials(caPath, keyPath, certPath)
	myShadowClient.configureConnectDisconnectTimeout(60) 
	myShadowClient.configureMQTTOperationTimeout(10)  

	myShadowClient.connect()
	myDeviceShadow = myShadowClient.createShadowHandlerWithName("pi", True)

	while 1==1:
		s.trigger()
		tempreading = "{ \"state\" : { \"reported\": { \"temp\": \"%s\", \"humid\": \"%s\" } } }" % (str(s.temperature()), str(s.humidity()))
		print("payload: %s" % tempreading)
		if s.temperature() != -999:
			myDeviceShadow.shadowUpdate(tempreading, None, 5)
		time.sleep(60)
