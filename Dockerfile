
FROM python:3.8-buster

RUN apt-get update; apt-get install entr

#Install locust
RUN pip install locust==1.0

RUN mkdir /locust

#Provision locust
COPY ./locustfile.py /locust/
RUN echo 5 > /locust/users.txt; echo 1 > /locust/hatch_rate.txt

#Provision locust service
COPY ./locust /etc/init.d/
RUN chmod +x /etc/init.d/locust; update-rc.d locust defaults 

#Provision locust_updater.sh
COPY ./locust_updater.sh /locust_updater.sh
RUN chmod +x /locust_updater.sh


COPY ./entr.sh /entr.sh
RUN chmod +x /entr.sh


ENTRYPOINT /entr.sh 
