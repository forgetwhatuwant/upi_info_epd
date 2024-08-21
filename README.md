
# Raspberry Pi SPI 接口配置和环境安装指南

## 1. 配置 SPI 接口

1. 打开 Raspberry Pi 配置工具：
   ```bash
   sudo raspi-config
   ```
2. 选择 `Interfacing Options` -> `SPI` -> `Yes` 启用 SPI 接口。

3. 重启 Raspberry Pi：
   ```bash
   sudo reboot
   ```

## 2. 安装必要的软件包

1. 更新软件包列表：
   ```bash
   sudo apt-get update
   ```

2. 安装 `pip`、`PIL`、`numpy` 等 Python 包：
   ```bash
   sudo apt-get install python3-pip
   sudo apt-get install python3-pil
   sudo apt-get install python3-numpy
   ```

3. 安装 RPi.GPIO 和 spidev 库：
   ```bash
   sudo pip3 install RPi.GPIO
   sudo pip3 install spidev
   ```

4. 再次更新软件包列表：
   ```bash
   sudo apt-get update
   ```

5. 安装 `gpiozero` 库：
   ```bash
   sudo apt install python3-gpiozero
   ```

## 3. 克隆项目并运行

1. 克隆项目代码仓库（替换为实际仓库地址）：
   ```bash
   git clone <repository_url>
   ```

2. 进入项目目录：
   ```bash
   cd upi_info_epd
   cd upi_info_display
   ```

3. 运行 Python 脚本：
   ```bash
   sudo python3 display_info.py
   ```

## 注意

- 确保所有依赖库和工具包安装成功。
- 在克隆仓库时，替换 `<repository_url>` 为实际的 Git 仓库地址。
- 如果遇到权限问题，请确保以 `sudo` 运行相关命令。




