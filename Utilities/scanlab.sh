#!/bin/bash

centosIp=$1
user="amcclab"
pass="amcc1234"

if [ -z "$1" ]
        then
        echo "Usage: $0 <ip>"
        exit
fi

#`command`


exec_centos (){
  echo sshpass -p ${pass} ssh -o StrictHostKeyChecking=no -t ${user}@${centosIp} "'${1}'"
  sshpass -p ${pass} ssh -o StrictHostKeyChecking=no -t ${user}@${centosIp} "${1}"
}

echo "------------------------------------------------------------------"
echo "-                                                                -"
echo "-        			             Information                                    -"
echo "-                                                                -"
echo "------------------------------------------------------------------"


echo Check IP
exec_centos 'ifconfig | grep 10.38'
echo "------------------------------------------------------------------"
echo Java Version
exec_centos 'java -version'
echo "------------------------------------------------------------------"
echo CPU Info
exec_centos 'lscpu'


datetime=$(TZ='Asia/Ho_Chi_Minh' date "+%y%m%d-%H%M")
logname="${centosIp}_${datetime}.log"

exec_centos "ifconfig ${logname}"

# SCP and Cat log file
#echo sshpass -p ${pass} scp {user}@{centosIp}:${logname} .
#sshpass -p ${pass} scp ${user}@${centosIp}:${logname} .

echo ${logname}