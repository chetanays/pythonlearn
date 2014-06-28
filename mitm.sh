#!/bin/bash
echo "Do you want to start mitm? Y/N"
read opt
if [ $opt == "Y" -o $opt == "y" ];
then
	`echo 1 > /proc/sys/net/ipv4/ip_forward`
elif [ $opt == "N" -o $opt == "n" ];
then
	`echo 0 > /proc/sys/net/ipv4/ip_forward`
else
	echo "Usage ./mitm.sh"
fi

