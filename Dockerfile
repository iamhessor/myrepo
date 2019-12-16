FROM ubuntu:16.04
EXPOSE 10000
RUN apt-get update && apt-get -y install python3 && apt-get -y install python3-pip && python3 -m pip install requests
RUN apt-get -y install netcat && apt-get -y install telnet && apt-get -y install net-tools
COPY ./telegram.py /home/telegram.py
COPY ./client.py /home/client.py
CMD python3 /home/telegram.py
