#!/bin/bash
# Requirements
#   yum install -y ipmitool nvme-cli pci-utils net-utils
#
#
# Variables
centosIp=$1
user="root"
pass="root"
bmcUser="ADMIN"
bmcPassword="ADMIN"
if [ -z "$1" ]
        then
        echo "Usage : $0 <ip>"
        exit
fi

# sub function

exec_centos (){
        echo sshpass -p ${pass} ssh -o StrictHostKeyChecking=no -t ${user}@${centosIp} "'${1}'"
        sshpass -p ${pass} ssh -o StrictHostKeyChecking=no -t ${user}@${centosIp} "${1}"
		}
		
# Wget script
exec_centos 'rm -f /var/tmp/deviceInformation.sh'
exec_centos 'wget -P /var/tmp http://10.38.13.103/projects/hcm/diagnostic/QA/Scripts/deviceInformation.sh'		
		

datetime=$(TZ='Asia/Ho_Chi_Minh' date "+%y%m%d-%H%M")

logname="${centosIp}_${datetime}.log"
logpath="/var/tmp/${logname}"
exec_centos 'chmod 777 /var/tmp/deviceInformation.sh'
exec_centos "/var/tmp/deviceInformation.sh ${logname}"


# SCP and Cat log file
echo sshpass -p ${pass} scp ${user}@${centosIp}:${logname} .
sshpass -p ${pass} scp ${user}@${centosIp}:${logname} .
echo "------------------------------------------------------------------"
echo "-                                                                -"
echo "-        			Information                                    -"
echo "-                                                                -"
echo "------------------------------------------------------------------"
cat ${logname}
