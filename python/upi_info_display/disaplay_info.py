#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)
import logging
import psutil
import time
import termios
import tty
from waveshare_epd import epd2in13_V4
from PIL import Image, ImageDraw, ImageFont

logging.basicConfig(level=logging.DEBUG)

def get_key_press():
    """检测键盘输入"""
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

try:
    logging.info("Initializing e-Paper display")
    
    epd = epd2in13_V4.EPD()
    epd.init()
    epd.Clear(0xFF)

    font15 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 15)

    while True:
        # 创建新图像，每次循环都重置图像
        image = Image.new('1', (epd.height, epd.width), 255)
        draw = ImageDraw.Draw(image)

        # 获取实时CPU和内存使用信息
        cpu_usage = psutil.cpu_percent(interval=0.1)  # 使用短时间间隔来更新CPU使用率
        memory_info = psutil.virtual_memory()
        memory_usage = memory_info.percent

        # 在图像上绘制文本
        draw.text((10, 10), f"CPU Usage: {cpu_usage:.1f}%", font=font15, fill=0)
        draw.text((10, 30), f"Memory Usage: {memory_usage:.1f}%", font=font15, fill=0)

        # 更新显示内容
        logging.info(f"Updating display: CPU={cpu_usage:.1f}%, Memory={memory_usage:.1f}%")
        epd.display(epd.getbuffer(image))



        time.sleep(2)  # 每秒刷新一次

    # 清理并进入休眠
    epd.Clear(0xFF)
    logging.info("Going to sleep...")
    epd.sleep()

except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("Program interrupted")
    epd2in13_V4.epdconfig.module_exit(cleanup=True)
    exit()
