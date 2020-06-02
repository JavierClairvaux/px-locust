#!/bin/sh

users=$1
hatch_rate=$2
re='^[0-9]+$'

if [ $users -gt 0 ] && [ $hatch_rate -gt 0 ]
then
	#Update users
	echo $users > /locust/users.txt
	#Update hatch rate
	echo $hatch_rate > /locust/hatch_rate.txt
else
	echo "Both users and hatch rate have to numbers greater than 0!"
	echo "Usage example: ./locus_updater <users> <hatch rate>"
fi
