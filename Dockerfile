
FROM python:3.8-buster


#Install locust
RUN pip install locust==1.0 pickledb

RUN mkdir /locust
COPY ./locustfile.py /locust
COPY ./server.py /server.py

CMD ["python", "/server.py"]
