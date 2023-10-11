#!/bin/bash

array=`sudo cat /etc/hosts | grep "#211*" | awk '{print $2}'`

for var in ${array};
do
	echo $var
	sed -i "s|^$var|#&|g" inventory
done    

