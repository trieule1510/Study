./xconsole.py --cmd off --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --cmd sel_list --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --set_nvparm [SI_DDR_VMARGIN:1130496:0x0][SI_SOC_VMARGIN:1130504:0x0] --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --cmd on --bmcip 10.38.165.34 --board_type Mt.Snow
cksum static/test_script/test_delivery.sh
cksum static/test_script/memtester.elf
cksum static/test_script/stressapptest.elf
./xconsole.py --cmd sel_list --bmcip 10.38.165.34 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/218/Mt.Snow_218_210428_174055/sensor-mem_test-1.log --sensor_interval 30
./xconsole.py --cmd off --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --cmd sel_list --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --set_nvparm [SI_DDR_VMARGIN:1130496:0x0][SI_SOC_VMARGIN:1130504:0xFFFFFFDA] --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --cmd on --bmcip 10.38.165.34 --board_type Mt.Snow
cksum static/test_script/test_delivery.sh
cksum static/test_script/memtester.elf
cksum static/test_script/stressapptest.elf
./xconsole.py --cmd sel_list --bmcip 10.38.165.34 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/218/Mt.Snow_218_210428_174055/sensor-mem_test-2.log --sensor_interval 30
./xconsole.py --cmd off --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --cmd sel_list --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --set_nvparm [SI_DDR_VMARGIN:1130496:0x0][SI_SOC_VMARGIN:1130504:0x25] --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --cmd on --bmcip 10.38.165.34 --board_type Mt.Snow
cksum static/test_script/test_delivery.sh
cksum static/test_script/memtester.elf
cksum static/test_script/stressapptest.elf
./xconsole.py --cmd sel_list --bmcip 10.38.165.34 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/218/Mt.Snow_218_210428_174055/sensor-mem_test-3.log --sensor_interval 30
./xconsole.py --cmd off --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --cmd sel_list --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --set_nvparm [SI_DDR_VMARGIN:1130496:0xFFFFFFC4][SI_SOC_VMARGIN:1130504:0x0] --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --cmd on --bmcip 10.38.165.34 --board_type Mt.Snow
cksum static/test_script/test_delivery.sh
cksum static/test_script/memtester.elf
cksum static/test_script/stressapptest.elf
./xconsole.py --cmd sel_list --bmcip 10.38.165.34 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/218/Mt.Snow_218_210428_174055/sensor-mem_test-4.log --sensor_interval 30
./xconsole.py --cmd off --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --cmd sel_list --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --set_nvparm [SI_DDR_VMARGIN:1130496:0xFFFFFFC4][SI_SOC_VMARGIN:1130504:0xFFFFFFDA] --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --cmd on --bmcip 10.38.165.34 --board_type Mt.Snow
cksum static/test_script/test_delivery.sh
cksum static/test_script/memtester.elf
cksum static/test_script/stressapptest.elf
./xconsole.py --cmd sel_list --bmcip 10.38.165.34 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/218/Mt.Snow_218_210428_174055/sensor-mem_test-5.log --sensor_interval 30
./xconsole.py --cmd off --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --cmd sel_list --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --set_nvparm [SI_DDR_VMARGIN:1130496:0xFFFFFFC4][SI_SOC_VMARGIN:1130504:0x25] --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --cmd on --bmcip 10.38.165.34 --board_type Mt.Snow
cksum static/test_script/test_delivery.sh
cksum static/test_script/memtester.elf
cksum static/test_script/stressapptest.elf
./xconsole.py --cmd sel_list --bmcip 10.38.165.34 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/218/Mt.Snow_218_210428_174055/sensor-mem_test-6.log --sensor_interval 30
./xconsole.py --cmd off --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --cmd sel_list --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --set_nvparm [SI_DDR_VMARGIN:1130496:0x3C][SI_SOC_VMARGIN:1130504:0x0] --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --cmd on --bmcip 10.38.165.34 --board_type Mt.Snow
cksum static/test_script/test_delivery.sh
cksum static/test_script/memtester.elf
cksum static/test_script/stressapptest.elf
./xconsole.py --cmd sel_list --bmcip 10.38.165.34 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/218/Mt.Snow_218_210428_174055/sensor-mem_test-7.log --sensor_interval 30
./xconsole.py --cmd off --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --cmd sel_list --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --set_nvparm [SI_DDR_VMARGIN:1130496:0x3C][SI_SOC_VMARGIN:1130504:0xFFFFFFDA] --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --cmd on --bmcip 10.38.165.34 --board_type Mt.Snow
cksum static/test_script/test_delivery.sh
cksum static/test_script/memtester.elf
cksum static/test_script/stressapptest.elf
./xconsole.py --cmd sel_list --bmcip 10.38.165.34 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/218/Mt.Snow_218_210428_174055/sensor-mem_test-8.log --sensor_interval 30
./xconsole.py --cmd off --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --cmd sel_list --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --set_nvparm [SI_DDR_VMARGIN:1130496:0x3C][SI_SOC_VMARGIN:1130504:0x25] --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --cmd on --bmcip 10.38.165.34 --board_type Mt.Snow
cksum static/test_script/test_delivery.sh
cksum static/test_script/memtester.elf
cksum static/test_script/stressapptest.elf
./xconsole.py --cmd sel_list --bmcip 10.38.165.34 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/218/Mt.Snow_218_210428_174055/sensor-mem_test-9.log --sensor_interval 30
./xconsole.py --cmd off --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --cmd sel_list --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --set_nvparm [SI_DDR_VMARGIN:1130496:0x0][SI_SOC_VMARGIN:1130504:0x0] --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --cmd on --bmcip 10.38.165.34 --board_type Mt.Snow
cksum static/test_script/test_delivery.sh
cksum static/test_script/memtester.elf
cksum static/test_script/stressapptest.elf
./xconsole.py --cmd sel_list --bmcip 10.38.165.34 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/218/Mt.Snow_218_210428_174055/sensor-mem_test-10.log --sensor_interval 30
./xconsole.py --cmd off --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --cmd sel_list --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --set_nvparm [SI_DDR_VMARGIN:1130496:0x0][SI_SOC_VMARGIN:1130504:0xFFFFFFDA] --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --cmd on --bmcip 10.38.165.34 --board_type Mt.Snow
cksum static/test_script/test_delivery.sh
cksum static/test_script/memtester.elf
cksum static/test_script/stressapptest.elf
./xconsole.py --cmd sel_list --bmcip 10.38.165.34 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/218/Mt.Snow_218_210428_174055/sensor-mem_test-11.log --sensor_interval 30
./xconsole.py --cmd off --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --cmd sel_list --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --set_nvparm [SI_DDR_VMARGIN:1130496:0x0][SI_SOC_VMARGIN:1130504:0x25] --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --cmd on --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --cmd sel_list --bmcip 10.38.165.34 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/218/Mt.Snow_218_210428_174055/sensor-mem_test-12.log --sensor_interval 30
./xconsole.py --cmd off --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --cmd sel_list --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --set_nvparm [SI_DDR_VMARGIN:1130496:0xFFFFFFC4][SI_SOC_VMARGIN:1130504:0x0] --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --cmd on --bmcip 10.38.165.34 --board_type Mt.Snow
cksum static/test_script/test_delivery.sh
cksum static/test_script/memtester.elf
cksum static/test_script/stressapptest.elf
./xconsole.py --cmd sel_list --bmcip 10.38.165.34 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/218/Mt.Snow_218_210428_174055/sensor-mem_test-13.log --sensor_interval 30
./xconsole.py --cmd off --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --cmd sel_list --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --set_nvparm [SI_DDR_VMARGIN:1130496:0xFFFFFFC4][SI_SOC_VMARGIN:1130504:0xFFFFFFDA] --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --cmd on --bmcip 10.38.165.34 --board_type Mt.Snow
cksum static/test_script/test_delivery.sh
cksum static/test_script/memtester.elf
cksum static/test_script/stressapptest.elf
./xconsole.py --cmd sel_list --bmcip 10.38.165.34 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/218/Mt.Snow_218_210428_174055/sensor-mem_test-14.log --sensor_interval 30
./xconsole.py --cmd off --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --cmd sel_list --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --set_nvparm [SI_DDR_VMARGIN:1130496:0xFFFFFFC4][SI_SOC_VMARGIN:1130504:0x25] --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --cmd on --bmcip 10.38.165.34 --board_type Mt.Snow
cksum static/test_script/test_delivery.sh
cksum static/test_script/memtester.elf
cksum static/test_script/stressapptest.elf
./xconsole.py --cmd sel_list --bmcip 10.38.165.34 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/218/Mt.Snow_218_210428_174055/sensor-mem_test-15.log --sensor_interval 30
./xconsole.py --cmd off --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --cmd sel_list --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --set_nvparm [SI_DDR_VMARGIN:1130496:0x3C][SI_SOC_VMARGIN:1130504:0x0] --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --cmd on --bmcip 10.38.165.34 --board_type Mt.Snow
cksum static/test_script/test_delivery.sh
cksum static/test_script/memtester.elf
cksum static/test_script/stressapptest.elf
./xconsole.py --cmd sel_list --bmcip 10.38.165.34 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/218/Mt.Snow_218_210428_174055/sensor-mem_test-16.log --sensor_interval 30
./xconsole.py --cmd off --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --cmd sel_list --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --set_nvparm [SI_DDR_VMARGIN:1130496:0x3C][SI_SOC_VMARGIN:1130504:0xFFFFFFDA] --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --cmd on --bmcip 10.38.165.34 --board_type Mt.Snow
cksum static/test_script/test_delivery.sh
cksum static/test_script/memtester.elf
cksum static/test_script/stressapptest.elf
./xconsole.py --cmd sel_list --bmcip 10.38.165.34 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/218/Mt.Snow_218_210428_174055/sensor-mem_test-17.log --sensor_interval 30
./xconsole.py --cmd off --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --cmd sel_list --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --set_nvparm [SI_DDR_VMARGIN:1130496:0x3C][SI_SOC_VMARGIN:1130504:0x25] --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --cmd on --bmcip 10.38.165.34 --board_type Mt.Snow
cksum static/test_script/test_delivery.sh
cksum static/test_script/memtester.elf
cksum static/test_script/stressapptest.elf
./xconsole.py --cmd sel_list --bmcip 10.38.165.34 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/218/Mt.Snow_218_210428_174055/sensor-mem_test-18.log --sensor_interval 30
./xconsole.py --cmd off --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --cmd sel_list --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --set_nvparm [SI_DDR_VMARGIN:1130496:0x0][SI_SOC_VMARGIN:1130504:0x0] --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --cmd on --bmcip 10.38.165.34 --board_type Mt.Snow
cksum static/test_script/test_delivery.sh
cksum static/test_script/memtester.elf
cksum static/test_script/stressapptest.elf
./xconsole.py --cmd sel_list --bmcip 10.38.165.34 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/218/Mt.Snow_218_210428_174055/sensor-mem_test-19.log --sensor_interval 30
./xconsole.py --cmd off --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --cmd sel_list --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --set_nvparm [SI_DDR_VMARGIN:1130496:0x0][SI_SOC_VMARGIN:1130504:0xFFFFFFDA] --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --cmd on --bmcip 10.38.165.34 --board_type Mt.Snow
cksum static/test_script/test_delivery.sh
cksum static/test_script/memtester.elf
cksum static/test_script/stressapptest.elf
./xconsole.py --cmd sel_list --bmcip 10.38.165.34 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/218/Mt.Snow_218_210428_174055/sensor-mem_test-20.log --sensor_interval 30
./xconsole.py --cmd off --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --cmd sel_list --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --set_nvparm [SI_DDR_VMARGIN:1130496:0x0][SI_SOC_VMARGIN:1130504:0x25] --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --cmd on --bmcip 10.38.165.34 --board_type Mt.Snow
cksum static/test_script/test_delivery.sh
cksum static/test_script/memtester.elf
cksum static/test_script/stressapptest.elf
./xconsole.py --cmd sel_list --bmcip 10.38.165.34 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/218/Mt.Snow_218_210428_174055/sensor-mem_test-21.log --sensor_interval 30
./xconsole.py --cmd off --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --cmd sel_list --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --set_nvparm [SI_DDR_VMARGIN:1130496:0xFFFFFFC4][SI_SOC_VMARGIN:1130504:0x0] --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --cmd on --bmcip 10.38.165.34 --board_type Mt.Snow
cksum static/test_script/test_delivery.sh
cksum static/test_script/memtester.elf
cksum static/test_script/stressapptest.elf
./xconsole.py --cmd sel_list --bmcip 10.38.165.34 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/218/Mt.Snow_218_210428_174055/sensor-mem_test-22.log --sensor_interval 30
./xconsole.py --cmd off --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --cmd sel_list --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --set_nvparm [SI_DDR_VMARGIN:1130496:0xFFFFFFC4][SI_SOC_VMARGIN:1130504:0xFFFFFFDA] --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --cmd on --bmcip 10.38.165.34 --board_type Mt.Snow
cksum static/test_script/test_delivery.sh
cksum static/test_script/memtester.elf
cksum static/test_script/stressapptest.elf
./xconsole.py --cmd sel_list --bmcip 10.38.165.34 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/218/Mt.Snow_218_210428_174055/sensor-mem_test-23.log --sensor_interval 30
./xconsole.py --cmd off --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --cmd sel_list --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --set_nvparm [SI_DDR_VMARGIN:1130496:0xFFFFFFC4][SI_SOC_VMARGIN:1130504:0x25] --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --cmd on --bmcip 10.38.165.34 --board_type Mt.Snow
cksum static/test_script/test_delivery.sh
cksum static/test_script/memtester.elf
cksum static/test_script/stressapptest.elf
./xconsole.py --cmd sel_list --bmcip 10.38.165.34 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/218/Mt.Snow_218_210428_174055/sensor-mem_test-24.log --sensor_interval 30
./xconsole.py --cmd off --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --cmd sel_list --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --set_nvparm [SI_DDR_VMARGIN:1130496:0x3C][SI_SOC_VMARGIN:1130504:0x0] --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --cmd on --bmcip 10.38.165.34 --board_type Mt.Snow
cksum static/test_script/test_delivery.sh
cksum static/test_script/memtester.elf
cksum static/test_script/stressapptest.elf
./xconsole.py --cmd sel_list --bmcip 10.38.165.34 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/218/Mt.Snow_218_210428_174055/sensor-mem_test-25.log --sensor_interval 30
./xconsole.py --cmd off --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --cmd sel_list --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --set_nvparm [SI_DDR_VMARGIN:1130496:0x3C][SI_SOC_VMARGIN:1130504:0xFFFFFFDA] --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --cmd on --bmcip 10.38.165.34 --board_type Mt.Snow
cksum static/test_script/test_delivery.sh
cksum static/test_script/memtester.elf
cksum static/test_script/stressapptest.elf
./xconsole.py --cmd sel_list --bmcip 10.38.165.34 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/218/Mt.Snow_218_210428_174055/sensor-mem_test-26.log --sensor_interval 30
./xconsole.py --cmd off --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --cmd sel_list --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --set_nvparm [SI_DDR_VMARGIN:1130496:0x3C][SI_SOC_VMARGIN:1130504:0x25] --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --cmd on --bmcip 10.38.165.34 --board_type Mt.Snow
cksum static/test_script/test_delivery.sh
cksum static/test_script/memtester.elf
cksum static/test_script/stressapptest.elf
./xconsole.py --cmd sel_list --bmcip 10.38.165.34 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/218/Mt.Snow_218_210428_174055/sensor-mem_test-27.log --sensor_interval 30
./ipmitool_sensor_chartjs.py --log logs/218/Mt.Snow_218_210428_174055/sensor.log --D 1 --sensor_interval 30
