# AIRQUINO

# Introduction
The following documentation will serve as the steps taken by the group members to complete the following project. The operating system flashed on the Raspberry Pi 4 is Bullseye OS. The reason for us using Bullseye OS rather than any older Raspian OS was because there was to many problems with compatibility when installing required packages for using the onboard bluetooth device. While the Bullseye OS is still a newly released, we decided to use it because of the new features that comes with it like the Updater plugin, File manager, Notifications and much more.

# Gateway Client
As for this part of the project has to do more with Linux OS & scripts we had to divide the task in steps as follows:
1.	Connect to Range_Extender ESP's per Zone Scripts
  - Find Service of ESP GATT Server
  - Find Characteristic of ESP GATT Server
  - Read characteristic (air quality)
  - According to the Thingy:52 data sheet the data is advertised as 4 bytes. First 2 bytes as CO2 and Last 2 bytes as VOC.
  - Get current time of RPi 4 and en store characteristic (air quality) per Nordic Thingy:52 per Zone in a list with this format; `(DATE,TIME,ZONE,DEVICE,PPM,VOC)`
  - Append list to a .csv file every time the script runs.
This was mainly done by using Python Programming Language and installing some pip requirements for performing the scripts successfully. Note: Check GitHub / GitLab repo always for requirements.txt file and install them before running the scripts.
2.	Automate Append Range_Extender ESP's Data per Zone to csv Script 
  - Append using Bash script for running 2 Python scripts with one waiting for 20 seconds after the initial running Bash script
  - Make Bash script run every minute when RPi 4 is scanning for devices are deployed and in BLE range to append collected data to csv
  - Log if Bash script has runned successfully or not for debugging if devices were in range or not 
  
# Data Dashboard Server
Display the Data collected with a user friendly Dashboard locally on the RPi 4 – Multiple ways to target this approach
3.	Visualizing collected Data from the Range_Extender ESP's
  - Install required packages for running the server for the Dashboard
  - Using Python with Pandas
  - Using JavaScript with D3js 
  - Using ElasticSearch with Kibana 

# Additional Information
The purpose of the RPi 4 is to collect and store the data per zone to .csv file for displaying afterwards in a user friendly dashboard. As a client it will connect to a Range_Extender ESP and as a server it will host a Python / JavaScript dashboard with real-time data. As we are not so familiar with JavaScript, we decided to try 3 different tools to finally pick the ones that are representing the data more user friendly. 

In order to run the scripts for this project, you need to clone this repo to your Raspberry Pi and you will find the scripts at this `AIRQUINO/BLE - Implementation/RaspberryPi/Data_Collector` path of the repo. 
To read the air quality values for the zones of TQ5 you need to run the script  `read_Zone1_BLE_server.py` and `read_Zone2_BLE_server.py`. 
To read the air quality values for the zones of R10 you need to run the script  `read_Zone1_BLE_server2.py` and `read_Zone2_BLE_server2.py`. 
To start scheduled crontab script configuration you need install crontab package to RPi and configure crontab by typing in cmd: `sudo crontab -e` and you can configure it like these example entries: `30 */2 * * * bash write_###_Zones_to_csv.sh -> 30 minutes past the hour every 2 hours`
`15,45 23 * * * bash write_###_Zones_to_csv.sh -> 11:15PM and 11:45PM every day`

# References
-	Bullseye OS - https://www.raspberrypi.com/news/raspberry-pi-os-debian-bullseye/
-	Schedule Scripts - https://towardsdatascience.com/how-to-schedule-python-scripts-with-cron-the-only-guide-youll-ever-need-deea2df63b4e
-	Bash wait - https://linuxize.com/post/bash-wait/
-	Crontab Syntax - https://crontab.guru/
-	BLE on Linux - https://github.com/IanHarvey/bluepy
