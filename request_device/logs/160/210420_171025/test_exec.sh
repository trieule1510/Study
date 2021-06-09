sshpass -p root ssh -o StrictHostKeyChecking=no -t root@10.38.172.2 'ipmitool -H 10.38.162.31 -U ADMIN -P ADMIN -I lanplus -z 0x7fff chassis power off'
sshpass -p root ssh -o StrictHostKeyChecking=no -t root@10.38.172.2 'ipmitool -H 10.38.162.31 -U ADMIN -P ADMIN -I lanplus -z 0x7fff chassis power off'
