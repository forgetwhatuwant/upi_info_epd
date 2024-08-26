import RPi.GPIO as GPIO  # Import Raspberry Pi GPIO library
import time
import os

GPIO.setwarnings(False)  # Ignore warning for now
GPIO.setmode(GPIO.BOARD)  # Use physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Set pin 10 to be an input pin and set initial value to be pulled low (off)

def print_system_info():
    # 获取CPU信息
    cpu_info = os.popen('cat /proc/cpuinfo').read()
    # 获取内存信息
    mem_info = os.popen('free -h').read()
    # 获取系统负载信息
    load_info = os.popen('uptime').read()
    
    print("System Information:")
    print(cpu_info)
    print(mem_info)
    print(load_info)

while True:  # Run forever
    if GPIO.input(10) == GPIO.HIGH:
        print("Button was pushed!")
        print_system_info()
    if GPIO.input(10) == GPIO.LOW:
        print("Button not pressed!")
    time.sleep(1)
