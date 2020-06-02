#!/bin/sh

echo $FRONTEND_ADDR > /locust/frontend_addr
service locust start
ls -d /locust/*.txt | entr -nrp service locust restart
