                           Server Health Monitoring (lightweight)

Its a simple Python + Bash script that logs CPU, virtual memory, Disk storage and network usage on a Linux Server. Scheduled to run every 10 minutes using crontabs.

============================================================================

Features are 
1--> Logs resource usage. Easy to track

2--> Bash for automation

3--> Easy to customize and extend depending on the requirement

4--> Monitors CPU, Memory, Disk usage and Network I/O

5--> Logs system stats to a log file with timestamps

6--> Runs automatically using 'cron' every 10 minutes

============================================================================

Technologies used are

Python3
psutil(python package)
datetime(python package)
Bash
Cron

=============================================================================

SET UP INSTRUCTIONS

1) Install required dependencies 

sudo apt update
sudo apt install python3 python3-pip
pip3 install psutil (or) sudo apt install python3 python3-psutil 

2) create a folder in your directory using 
mkdir folder_name

3) get into the folder using cd command
cd folder_name

4)either use nano editor or vi editor to create a new file named health_monitor.py
nano health_monitor.py

==> using nano editor --> don't forget to Write out(CTRL + O) and then enter and then Exit(CTRL + X)

5)create Bash Wrapper Script name Monitor.sh
nano Monitor.sh

6)Make them Executable for errors using 

chmod +x health_monitor.py
chmod +x monitor.sh

7)now scheduling with Crontab
crontab -e

8)if running the logs for 1st time, it will take 10min to create the log(sys_health.log)

9) for sample output, check for the screenshot image in the repo

================================================================================

License:
This project is licensed under the MIT license. Feel free to use and modify it.

Acknowledgements:
Thanks to the Python3 psutil package and the Linux open-source community.

===============================================================================
