import psutil
import datetime

def log_status():
	with open("/home/ubuntu/System_Health_Monitor/sys_health.log", "a") as log:
		log.write(f"\n=== System Health @ {datetime.datetime.now()} ====\n")
		log.write(f"Memory Usage: {psutil.virtual_memory().percent}%\n")
		log.write(f"CPU Usage: {psutil.cpu_percent()}%\n")
		log.write(f"Disk Usage: {psutil.disk_usage('/').percent}%\n")
		net = psutil.net_io_counters()
		log.write(f"Network - Sent: {net.bytes_sent /1024**2:.2f} MB, Received: {net.bytes_recv / 1024**2:.2f} MB \n ")

if __name__ == "__main__":
	log_status()
