# Requirements
#   yum install -y ipmitool nvme-cli pci-utils net-utils
#   dot2unix all_info_2.sh
#

# Variables
user="ADMIN"
pass="ADMIN"

# sub function
detail() {
	# lspci check device LnkSta
	if [ -z "$1" ]
		then
		echo "Usage : $0 <sbdf>"
		lspci
		exit
	fi
	sbdf=$1
	lspci -s $sbdf -nn -D >> ${log}
	lspci -s $sbdf -vvv | grep -i Subsystem >> ${log}
	lspci -s $sbdf -vvv | grep -i "part number" >> ${log}
	lspci -s $sbdf -vvv | grep LnkCap >> ${log}
	lspci -s $sbdf -vvv | grep LnkSta >> ${log}
	lspci -s $sbdf -vvv | grep "Kernel driver" >> ${log}
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

# dump all CPU/BMC info

cmd() {
	echo "" >> ${log}
	echo "CMD: $1" >> ${log}
	$1 >> ${log}
	echo "" >> ${log}
}

datetime=$(TZ='Asia/Ho_Chi_Minh' date "+%y%m%d-%H%M")
if [ "$#" -ge 1 ]; then
        board=$1
else
		board=$(ipmitool -U ${user} -P ${pass} fru print | grep "Board Serial" | head -n1 | awk -F':' '{print $2}')
		board=$(echo ${board} | xargs)
fi
log="${board}_${datetime}.log"

# Create log file
echo "----- ${board} info @ ${datetime} -----" > ${log}

# BMC
cmd 'ipmitool lan print'
cmd 'ipmitool fru print'
cmd 'ipmitool mc info'
cmd 'ipmitool mc guid'

# BIOS version
cmd 'dmidecode -t bios'

# Processor info
cmd 'dmidecode -t processor'
cmd 'lscpu'

# Memory
cmd 'free -h'
dmidecode -t memory | grep Part >> ${log}
echo "Count DIMM: " >> ${log}
dmidecode -t memory | grep Part -c >> ${log}

# PCIe
cmd 'lspci -nn -D -k'
cmd 'lspci -t'
allpciedev

# SCSI
cmd 'lsscsi -v'
cmd 'nvme list'
cmd 'nvme list-subsys'
cmd 'lsblk -at'
cmd 'lsusb -t'

# Ethernet
cmd 'ifconfig -a'
cmd 'ip addr'
cmd 'ip route'
cmd 'ip rule'

# Kernel/OS
cmd 'uname -a'
cmd 'cat /etc/centos-release'

# Cat log file
cat ${log}
echo ""
echo "Log file: $(pwd)/${log}"