# 使用官方的Ubuntu 22.04镜像作为基础镜像
FROM ubuntu:22.04

# 更新软件包列表并安装Python 3.12
RUN apt-get update && apt-get install -y python3.12 python3.12-venv openssh-server

RUN apt update \
    && apt install --no-install-recommends -y gcc git zip unzip wget curl htop libgl1 libglib2.0-0 libpython3-dev gnupg g++ libusb-1.0-0 libsm6


# 设置环境变量以使用新版本的Python
ENV PATH=/usr/bin:$PATH

# 设置工作目录
WORKDIR /cs

RUN git clone https://github.com/CossellCollege/cs61a .

# 声明容器将监听的端口
EXPOSE 22