./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x0][SI_SOC_VMARGIN:1130504:0x0] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
cksum static/test_script/test_delivery.sh
cksum static/test_script/memtester.elf
cksum static/test_script/stressapptest.elf
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210425_092519/sensor-mem_test-1.log --sensor_interval 30
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x0][SI_SOC_VMARGIN:1130504:0xFFFFFFDA] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
cksum static/test_script/test_delivery.sh
cksum static/test_script/memtester.elf
cksum static/test_script/stressapptest.elf
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210425_092519/sensor-mem_test-2.log --sensor_interval 30
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x0][SI_SOC_VMARGIN:1130504:0x25] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
cksum static/test_script/test_delivery.sh
cksum static/test_script/memtester.elf
cksum static/test_script/stressapptest.elf
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210425_092519/sensor-mem_test-3.log --sensor_interval 30
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0xFFFFFFC4][SI_SOC_VMARGIN:1130504:0x0] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
cksum static/test_script/test_delivery.sh
cksum static/test_script/memtester.elf
cksum static/test_script/stressapptest.elf
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210425_092519/sensor-mem_test-4.log --sensor_interval 30
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0xFFFFFFC4][SI_SOC_VMARGIN:1130504:0xFFFFFFDA] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
cksum static/test_script/test_delivery.sh
cksum static/test_script/memtester.elf
cksum static/test_script/stressapptest.elf
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210425_092519/sensor-mem_test-5.log --sensor_interval 30
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0xFFFFFFC4][SI_SOC_VMARGIN:1130504:0x25] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
cksum static/test_script/test_delivery.sh
cksum static/test_script/memtester.elf
cksum static/test_script/stressapptest.elf
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210425_092519/sensor-mem_test-6.log --sensor_interval 30
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x3C][SI_SOC_VMARGIN:1130504:0x0] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
cksum static/test_script/test_delivery.sh
cksum static/test_script/memtester.elf
cksum static/test_script/stressapptest.elf
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210425_092519/sensor-mem_test-7.log --sensor_interval 30
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x3C][SI_SOC_VMARGIN:1130504:0xFFFFFFDA] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
cksum static/test_script/test_delivery.sh
cksum static/test_script/memtester.elf
cksum static/test_script/stressapptest.elf
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210425_092519/sensor-mem_test-8.log --sensor_interval 30
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x3C][SI_SOC_VMARGIN:1130504:0x25] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
cksum static/test_script/test_delivery.sh
cksum static/test_script/memtester.elf
cksum static/test_script/stressapptest.elf
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210425_092519/sensor-mem_test-9.log --sensor_interval 30
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x0][SI_SOC_VMARGIN:1130504:0x0] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
cksum static/test_script/test_delivery.sh
cksum static/test_script/memtester.elf
cksum static/test_script/stressapptest.elf
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210425_092519/sensor-mem_test-10.log --sensor_interval 30
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x0][SI_SOC_VMARGIN:1130504:0xFFFFFFDA] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
cksum static/test_script/test_delivery.sh
cksum static/test_script/memtester.elf
cksum static/test_script/stressapptest.elf
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210425_092519/sensor-mem_test-11.log --sensor_interval 30
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x0][SI_SOC_VMARGIN:1130504:0x25] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
cksum static/test_script/test_delivery.sh
cksum static/test_script/memtester.elf
cksum static/test_script/stressapptest.elf
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210425_092519/sensor-mem_test-12.log --sensor_interval 30
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0xFFFFFFC4][SI_SOC_VMARGIN:1130504:0x0] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
cksum static/test_script/test_delivery.sh
cksum static/test_script/memtester.elf
cksum static/test_script/stressapptest.elf
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210425_092519/sensor-mem_test-13.log --sensor_interval 30
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0xFFFFFFC4][SI_SOC_VMARGIN:1130504:0xFFFFFFDA] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
cksum static/test_script/test_delivery.sh
cksum static/test_script/memtester.elf
cksum static/test_script/stressapptest.elf
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210425_092519/sensor-mem_test-14.log --sensor_interval 30
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0xFFFFFFC4][SI_SOC_VMARGIN:1130504:0x25] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
cksum static/test_script/test_delivery.sh
cksum static/test_script/memtester.elf
cksum static/test_script/stressapptest.elf
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210425_092519/sensor-mem_test-15.log --sensor_interval 30
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x3C][SI_SOC_VMARGIN:1130504:0x0] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
cksum static/test_script/test_delivery.sh
cksum static/test_script/memtester.elf
cksum static/test_script/stressapptest.elf
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210425_092519/sensor-mem_test-16.log --sensor_interval 30
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x3C][SI_SOC_VMARGIN:1130504:0xFFFFFFDA] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
cksum static/test_script/test_delivery.sh
cksum static/test_script/memtester.elf
cksum static/test_script/stressapptest.elf
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210425_092519/sensor-mem_test-17.log --sensor_interval 30
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x3C][SI_SOC_VMARGIN:1130504:0x25] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
cksum static/test_script/test_delivery.sh
cksum static/test_script/memtester.elf
cksum static/test_script/stressapptest.elf
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210425_092519/sensor-mem_test-18.log --sensor_interval 30
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x0][SI_SOC_VMARGIN:1130504:0x0] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
cksum static/test_script/test_delivery.sh
cksum static/test_script/memtester.elf
cksum static/test_script/stressapptest.elf
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210425_092519/sensor-mem_test-19.log --sensor_interval 30
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x0][SI_SOC_VMARGIN:1130504:0xFFFFFFDA] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
cksum static/test_script/test_delivery.sh
cksum static/test_script/memtester.elf
cksum static/test_script/stressapptest.elf
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210425_092519/sensor-mem_test-20.log --sensor_interval 30
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x0][SI_SOC_VMARGIN:1130504:0x25] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
cksum static/test_script/test_delivery.sh
cksum static/test_script/memtester.elf
cksum static/test_script/stressapptest.elf
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210425_092519/sensor-mem_test-21.log --sensor_interval 30
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0xFFFFFFC4][SI_SOC_VMARGIN:1130504:0x0] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
cksum static/test_script/test_delivery.sh
cksum static/test_script/memtester.elf
cksum static/test_script/stressapptest.elf
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210425_092519/sensor-mem_test-22.log --sensor_interval 30
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0xFFFFFFC4][SI_SOC_VMARGIN:1130504:0xFFFFFFDA] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
cksum static/test_script/test_delivery.sh
cksum static/test_script/memtester.elf
cksum static/test_script/stressapptest.elf
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210425_092519/sensor-mem_test-23.log --sensor_interval 30
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0xFFFFFFC4][SI_SOC_VMARGIN:1130504:0x25] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
cksum static/test_script/test_delivery.sh
cksum static/test_script/memtester.elf
cksum static/test_script/stressapptest.elf
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210425_092519/sensor-mem_test-24.log --sensor_interval 30
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x3C][SI_SOC_VMARGIN:1130504:0x0] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
cksum static/test_script/test_delivery.sh
cksum static/test_script/memtester.elf
cksum static/test_script/stressapptest.elf
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210425_092519/sensor-mem_test-25.log --sensor_interval 30
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x3C][SI_SOC_VMARGIN:1130504:0xFFFFFFDA] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
cksum static/test_script/test_delivery.sh
cksum static/test_script/memtester.elf
cksum static/test_script/stressapptest.elf
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210425_092519/sensor-mem_test-26.log --sensor_interval 30
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x3C][SI_SOC_VMARGIN:1130504:0x25] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
cksum static/test_script/test_delivery.sh
cksum static/test_script/memtester.elf
cksum static/test_script/stressapptest.elf
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210425_092519/sensor-mem_test-27.log --sensor_interval 30
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x0][SI_SOC_VMARGIN:1130504:0x0] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
cksum static/test_script/test_delivery.sh
cksum static/test_script/memtester.elf
cksum static/test_script/stressapptest.elf
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210425_092519/sensor-mem_test-28.log --sensor_interval 30
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x0][SI_SOC_VMARGIN:1130504:0xFFFFFFDA] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
cksum static/test_script/test_delivery.sh
cksum static/test_script/memtester.elf
cksum static/test_script/stressapptest.elf
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210425_092519/sensor-mem_test-29.log --sensor_interval 30
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x0][SI_SOC_VMARGIN:1130504:0x25] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
cksum static/test_script/test_delivery.sh
cksum static/test_script/memtester.elf
cksum static/test_script/stressapptest.elf
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210425_092519/sensor-mem_test-30.log --sensor_interval 30
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0xFFFFFFC4][SI_SOC_VMARGIN:1130504:0x0] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
cksum static/test_script/test_delivery.sh
cksum static/test_script/memtester.elf
cksum static/test_script/stressapptest.elf
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210425_092519/sensor-mem_test-31.log --sensor_interval 30
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0xFFFFFFC4][SI_SOC_VMARGIN:1130504:0xFFFFFFDA] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
cksum static/test_script/test_delivery.sh
cksum static/test_script/memtester.elf
cksum static/test_script/stressapptest.elf
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210425_092519/sensor-mem_test-32.log --sensor_interval 30
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0xFFFFFFC4][SI_SOC_VMARGIN:1130504:0x25] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
cksum static/test_script/test_delivery.sh
cksum static/test_script/memtester.elf
cksum static/test_script/stressapptest.elf
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210425_092519/sensor-mem_test-33.log --sensor_interval 30
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x3C][SI_SOC_VMARGIN:1130504:0x0] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
cksum static/test_script/test_delivery.sh
cksum static/test_script/memtester.elf
cksum static/test_script/stressapptest.elf
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210425_092519/sensor-mem_test-34.log --sensor_interval 30
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x3C][SI_SOC_VMARGIN:1130504:0xFFFFFFDA] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
cksum static/test_script/test_delivery.sh
cksum static/test_script/memtester.elf
cksum static/test_script/stressapptest.elf
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210425_092519/sensor-mem_test-35.log --sensor_interval 30
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x3C][SI_SOC_VMARGIN:1130504:0x25] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
cksum static/test_script/test_delivery.sh
cksum static/test_script/memtester.elf
cksum static/test_script/stressapptest.elf
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210425_092519/sensor-mem_test-36.log --sensor_interval 30
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x0][SI_SOC_VMARGIN:1130504:0x0] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
cksum static/test_script/test_delivery.sh
cksum static/test_script/memtester.elf
cksum static/test_script/stressapptest.elf
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210425_092519/sensor-mem_test-37.log --sensor_interval 30
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x0][SI_SOC_VMARGIN:1130504:0xFFFFFFDA] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
cksum static/test_script/test_delivery.sh
cksum static/test_script/memtester.elf
cksum static/test_script/stressapptest.elf
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210425_092519/sensor-mem_test-38.log --sensor_interval 30
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x0][SI_SOC_VMARGIN:1130504:0x25] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
cksum static/test_script/test_delivery.sh
cksum static/test_script/memtester.elf
cksum static/test_script/stressapptest.elf
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210425_092519/sensor-mem_test-39.log --sensor_interval 30
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0xFFFFFFC4][SI_SOC_VMARGIN:1130504:0x0] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
cksum static/test_script/test_delivery.sh
cksum static/test_script/memtester.elf
cksum static/test_script/stressapptest.elf
