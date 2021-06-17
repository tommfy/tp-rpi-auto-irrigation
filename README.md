Code to go along with the [Raspberry Pi Controlled Irrigation System](http://www.instructables.com/id/Raspberry-Pi-Controlled-Irrigation-System) Instructable by Ben Finio.

I have created my own Open Weather code because I'm too cheap to get the Wunderground API key :D

This code contains the script "tp_irrigate.py" which automatically runs an outside sprinkler/drip feeder
on a fixed schedule using a crontab. The sprinkler will only run if the current forecast is not rain.  The script uses the Open Weather API to get current rainfall
