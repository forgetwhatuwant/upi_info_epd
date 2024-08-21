sudo raspi-config
Choose Interfacing Options -> SPI -> Yes Enable SPI interface

sudo reboot

sudo apt-get update
sudo apt-get install python3-pip
sudo apt-get install python3-pil
sudo apt-get install python3-numpy
sudo pip3 install RPi.GPIO
sudo pip3 install spidev

sudo apt-get update
# python3
sudo apt install python3-gpiozero

git clone ..
cd upi_info_epd
cd upi_info_display
sudo python3  display_info.py
