#!/bin/bash

centosIp=$1
user="amcclab"
pass="amcc1234"

if [ -z "$1" ]
        then
        echo "Usage: $0 <ip>"
        exit
fi

exec_centos (){
  echo sshpass -p ${pass} ssh -o StrictHostKeyChecking=no -t ${user}@${centosIp} "'${1}'"
  sshpass -p ${pass} ssh -o StrictHostKeyChecking=no -t ${user}@${centosIp} "${1}"
}

exec_centos 'ifconfig'

datetime=$(TZ='Asia/Ho_Chi_Minh' date "+%y%m%d-%H%M")

logname="${centosIp}_${datetime}.log"

