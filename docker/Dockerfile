# 使用官方的Ubuntu 22.04镜像作为基础镜像
FROM ubuntu:22.04

# 更新软件包列表并安装Python 3.12
RUN apt-get update && apt-get install -y  \
    python3.12 python3.12-venv  \
    openssh-server \
    gcc git zip unzip wget curl htop libgl1 libglib2.0-0 libpython3-dev gnupg g++ libusb-1.0-0 libsm6

# 设置环境变量以使用新版本的Python
ENV PATH=/usr/bin:$PATH
# 配置OpenSSH服务器监听端口
RUN sed -i 's/#Port 22/Port 2222/' /etc/ssh/sshd_config

# 生成SSH密钥对
RUN ssh-keygen -A

# 设置工作目录
WORKDIR /cs

RUN git clone https://github.com/CossellCollege/cs61a .

# 设置默认命令以启动SSH守护进程并启动一个交互式bash shell
CMD ["/bin/bash", "-c", "/usr/sbin/sshd -D; exec bash"]

# 声明容器将监听的端口
EXPOSE 2222