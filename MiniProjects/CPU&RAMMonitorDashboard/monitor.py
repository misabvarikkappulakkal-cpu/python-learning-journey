import psutil
import time

print("🖥️ CPU & RAM Monitor Dashboard")
print("-" * 35)

try:
    while True:
        cpu = psutil.cpu_percent(interval=1)
        ram = psutil.virtual_memory()

        print(f"CPU Usage : {cpu}%")
        print(f"RAM Usage : {ram.percent}%")
        print(f"Available RAM : {ram.available / (1024**3):.2f} GB")
        print("-" * 35)

        time.sleep(2)

except KeyboardInterrupt:
    print("\nMonitoring stopped.")