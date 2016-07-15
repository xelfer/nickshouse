# nickshouse
Nick's House, a hackster.io project: https://www.hackster.io/xelfer/nick-s-house-echo-pi-weather-b08dde

You will need to set up your AWS environment:
~~~~# aws config~~~~

Generate your IoT Certificates: https://github.com/mariocannistra/python-paho-mqtt-for-aws-iot

~~~~
cd nickshouse
aws iot create-thing --thing-name "
aws iot create-keys-and-certificate --set-as-active --certificate-pem-outfile cert.pem --public-key-outfile publicKey.pem --private-key-outfile privkey.pem~~~~

record arn

aws iot create-policy --policy-name "PubSubToAnyTopic" --policy-document file://iotpolicy.json
aws iot attach-principal-policy --principal "arn:aws:iot:ap-southeast-2:127362029329:cert/58debbfe90fa58cad4df8426bdf3f20a71cf7644437203e251b503b994dfb8f3" --policy-name "PubSubToAnyTopic"

get endpoint: a1v9yu6xvaswb1.iot.ap-southeast-2.amazonaws.com
edit awstemp.py and enter your endpoint and your device name


~~~~

Install pigpiod:
~~~~apt-get update
sudo apt-get install pigpio python-pigpio python3-pigpio
service pigpiod start~~~~


Add this to your /etc/rc.local to make the application work on boot:

~~~~/usr/local/bin/pigpiod
screen -dmS "awstemp"
screen -S "awstemp" -p 0 -X stuff "/home/pi/awstemp.sh$printf \\r"~~~~


