FROM ubuntu
RUN apt-get update && apt install -y python3 && apt install -y python3-pip
RUN pip3 install flask
COPY main.py /home
ENTRYPOINT ["python3","/home/main.py"]