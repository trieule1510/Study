sshpass -p root ssh -o StrictHostKeyChecking=no -t root@10.38.172.55 'echo cleannv && gpiotool --set-data-low 226 && nvparm -c -o 0x110000 && nvparm -c -o 0x120000 && nvparm -c  -o 0x5F0000 && gpiotool --set-data-high 226'
ipmitool -H 10.38.172.55 -U ADMIN -P ADMIN -I lanplus -z 0x7fff chassis power off
sshpass -p root ssh -o StrictHostKeyChecking=no -t root@10.38.172.55 'echo SI_S1_PCP_ACTIVECPM_32_63 && gpiotool --set-data-low 226 && nvparm -s 0x0 -o 0x118018 && gpiotool --set-data-high 226;\
echo SI_S1_PCP_ACTIVECPM_0_31 && gpiotool --set-data-low 226 && nvparm -s 0x1 -o 0x118010 && gpiotool --set-data-high 226;\
echo SI_S0_PCP_ACTIVECPM_32_63 && gpiotool --set-data-low 226 && nvparm -s 0x0 -o 0x118008 && gpiotool --set-data-high 226;\
echo SI_S0_PCP_ACTIVECPM_0_31 && gpiotool --set-data-low 226 && nvparm -s 0x1 -o 0x118000 && gpiotool --set-data-high 226;\
'
ipmitool -H 10.38.172.55 -U ADMIN -P ADMIN -I lanplus -z 0x7fff chassis power on
