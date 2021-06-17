Code to go along with the [Raspberry Pi Controlled Irrigation System](http://www.instructables.com/id/Raspberry-Pi-Controlled-Irrigation-System) Instructable by Ben Finio.

This code contains the script "run_sprinkler.py" which automatically runs an outside sprinkler 
on a fixed schedule using a crontab.  The sprinkler will only run if there has been little to 
no rain in the past 24 hours.  The script uses the Weather Underground API to estimate recent rainfall

All credit goes to this guy for creating everything:
https://github.com/markveillette/rpi_sprinkler

I just tailored it to my settings.
