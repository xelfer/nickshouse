# nickshouse
Nick's House, a hackster.io project

Add this to your /etc/rc.local to make the application work on boot:

~~~~/usr/local/bin/pigpiod
screen -dmS "awstemp"
screen -S "awstemp" -p 0 -X stuff "/home/pi/awstemp.sh$printf \\r"~~~~
