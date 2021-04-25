#!/bin/bash

# sudo apt-get install sshpass
user='root'
pass='root'
hosts=$1
USER='ADMIN'
PASS='ADMIN'
cmd() {
  echo ""
  echo "CMD:$1"
  $1
  echo ""
}

allpciedev () {
	while IFS= read -r line
	do
			short=$(echo $line | awk '{print $1}')
			echo "_______________ $short _______________" >> ${log}
			detail ${short}
			echo "" >> ${log}
			echo "" >> ${log}
	done < <(lspci | grep -v "Ampere")
}

datetime=$(TZ='Asia/Ho_Chi_Minh' date "+%y%m%d-%H%M")

board=$(ipmitool -U ${user} -P ${pass} fru print | grep "Board Serial" | head -n1 | awk -F':' '{print $2}')
board=$(echo ${board} | xargs)

echo "----- ${board} info @ ${datetime} -----"


sshpass -p ${pass} ssh -l ${user}@${hosts}
cmd 'pwd'
allpciedev
echo ${datetime}