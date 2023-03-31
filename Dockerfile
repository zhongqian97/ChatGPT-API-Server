# 使用官方的Python基础镜像作为基础
FROM python:3.11-slim

# 设置工作目录
WORKDIR /app

# 安装所需的Python包
RUN pip install --trusted-host pypi.python.org Flask requests revChatGPT

# 将当前目录的内容复制到容器的/app目录
COPY . /app

# 使端口80可用于该容器之外
EXPOSE 5000

# 运行app.py，启动服务器
CMD ["python", "app.py"]
