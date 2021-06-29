sshpass -p root ssh -o StrictHostKeyChecking=no -t root@10.38.172.55 'echo cleannv && gpiotool --set-data-low 226 && nvparm -c -o 0x110000 && nvparm -c -o 0x120000 && nvparm -c  -o 0x5F0000 && gpiotool --set-data-high 226'
ipmitool -H 10.38.172.55 -U ADMIN -P ADMIN -I lanplus -z 0x7fff chassis power off
echo yyy |ipmitool -H 10.38.172.55 -U ADMIN -P ADMIN -I lanplus -z 0x7fff hpm upgrade /projects/hcm/diagnostic/QA/Equipment/request_device/cfg/scp_fw/altra_scp_signed_1.04.20210326.hpm force
ipmitool -H 10.38.172.55 -U ADMIN -P ADMIN -I lanplus -z 0x7fff chassis power off
echo yyy |ipmitool -H 10.38.172.55 -U ADMIN -P ADMIN -I lanplus -z 0x7fff hpm upgrade /projects/hcm/diagnostic/QA/Equipment/request_device/cfg/atfbios_fw/jade_aptiov_atf_signed_1.04.20210326.hpm force
ipmitool -H 10.38.172.55 -U ADMIN -P ADMIN -I lanplus -z 0x7fff chassis power off
ipmitool -H 10.38.172.55 -U ADMIN -P ADMIN -I lanplus -z 0x7fff chassis power on
