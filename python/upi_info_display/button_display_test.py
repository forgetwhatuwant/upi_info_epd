import RPi.GPIO as GPIO
import time
import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)
from waveshare_epd import epd2in13_V4
from PIL import Image, ImageDraw, ImageFont

# 初始化GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# 初始化e-Paper
epd = epd2in13_V4.EPD()
epd.init()
epd.Clear(0xFF)  # 清空屏幕

def get_system_info():
    # 获取CPU信息
    cpu_info = os.popen('cat /proc/cpuinfo').read().split('\n')[:6]  # 只取前6行，便于显示
    # 获取内存信息
    mem_info = os.popen('free -h').readlines()[1].strip()  # 获取内存使用情况
    # 获取系统负载信息
    load_info = os.popen('uptime').read().strip()

    system_info = "\n".join(cpu_info) + "\n\n" + mem_info + "\n\n" + load_info
    return system_info

def display_on_epaper(text):
    # 创建一个新的图像对象，背景为白色
    image = Image.new('1', (epd.height, epd.width), 255)
    draw = ImageDraw.Draw(image)
    
    # 使用默认字体
    font = ImageFont.load_default()

    # 在图像上绘制文本
    draw.text((10, 0), text, font=font, fill=0)

    # 显示图像
    epd.display(epd.getbuffer(image))

while True:  # 永久循环
    if GPIO.input(10) == GPIO.HIGH:
        print("Button was pushed!")
        system_info = get_system_info()
        display_on_epaper(system_info)
        time.sleep(5)  # 等待一段时间，让用户看到内容
    if GPIO.input(10) == GPIO.LOW:
        print("Button was unpressed")
        
    time.sleep(1)

