## Steps to build/run the application ##

## These steps I did in my machine, which runs Ubuntu
1. Run the AVD emulator

	$ cd /home/<user>/Android/Sdk/
	$ sudo emulator/emulator -avd <virtual_device_name>


2. Run the application

	# change the IP in App.js from 127.0.0.1 to the one used to run the server

	$ sudo npm run android
