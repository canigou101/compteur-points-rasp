import time
import datetime

def log(message):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{now} - {message}", flush=True)

with open("/proc/uptime") as f:
    uptime_seconds = int(float(f.read().split()[0]))

log(f"main.py STARTED (Raspberry on for {uptime_seconds} seconds)")

for i in range(1, 101):
    log(f"count {i}")
    time.sleep(1)

log("main.py FINISHED")