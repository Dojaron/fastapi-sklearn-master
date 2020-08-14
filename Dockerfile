FROM ubuntu
LABEL maintainer='Dojanro'
RUN sed -i 's#http://archive.ubuntu.com/#http://mirrors.tuna.tsinghua.edu.cn/#' /etc/apt/sources.list

RUN apt-get update \
    && apt-get install python3-dev python3-pip -y

RUN python3 -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --upgrade pip setuptools
RUN pip install -U pip
RUN pip config set global.index-url http://mirrors.aliyun.com/pypi/simple
RUN pip config set install.trusted-host mirrors.aliyun.com

COPY fastapiML /home/fastapiML/
COPY requirements.txt /home/fastapiML/requirements.txt

WORKDIR  /home/fastapiML

RUN pip install -r requirements.txt


EXPOSE 8000

ENTRYPOINT ["uvicorn"]
CMD ["main:app", "--host", "0.0.0.0"]