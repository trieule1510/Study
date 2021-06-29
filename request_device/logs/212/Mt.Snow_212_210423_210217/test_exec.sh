./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x0][SI_SOC_VMARGIN:1130504:0x0] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-1.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x0][SI_SOC_VMARGIN:1130504:0xFFFFFFDA] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-2.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x0][SI_SOC_VMARGIN:1130504:0x25] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-3.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0xFFFFFFC4][SI_SOC_VMARGIN:1130504:0x0] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-4.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0xFFFFFFC4][SI_SOC_VMARGIN:1130504:0xFFFFFFDA] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-5.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0xFFFFFFC4][SI_SOC_VMARGIN:1130504:0x25] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-6.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x3C][SI_SOC_VMARGIN:1130504:0x0] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-7.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x3C][SI_SOC_VMARGIN:1130504:0xFFFFFFDA] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-8.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x3C][SI_SOC_VMARGIN:1130504:0x25] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-9.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x0][SI_SOC_VMARGIN:1130504:0x0] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-10.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x0][SI_SOC_VMARGIN:1130504:0xFFFFFFDA] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-11.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x0][SI_SOC_VMARGIN:1130504:0x25] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-12.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0xFFFFFFC4][SI_SOC_VMARGIN:1130504:0x0] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-13.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0xFFFFFFC4][SI_SOC_VMARGIN:1130504:0xFFFFFFDA] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-14.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0xFFFFFFC4][SI_SOC_VMARGIN:1130504:0x25] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-15.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x3C][SI_SOC_VMARGIN:1130504:0x0] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-16.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x3C][SI_SOC_VMARGIN:1130504:0xFFFFFFDA] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-17.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x3C][SI_SOC_VMARGIN:1130504:0x25] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-18.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x0][SI_SOC_VMARGIN:1130504:0x0] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-19.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x0][SI_SOC_VMARGIN:1130504:0xFFFFFFDA] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-20.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x0][SI_SOC_VMARGIN:1130504:0x25] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-21.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0xFFFFFFC4][SI_SOC_VMARGIN:1130504:0x0] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-22.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0xFFFFFFC4][SI_SOC_VMARGIN:1130504:0xFFFFFFDA] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-23.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0xFFFFFFC4][SI_SOC_VMARGIN:1130504:0x25] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-24.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x3C][SI_SOC_VMARGIN:1130504:0x0] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-25.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x3C][SI_SOC_VMARGIN:1130504:0xFFFFFFDA] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-26.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x3C][SI_SOC_VMARGIN:1130504:0x25] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-27.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x0][SI_SOC_VMARGIN:1130504:0x0] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-28.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x0][SI_SOC_VMARGIN:1130504:0xFFFFFFDA] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-29.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x0][SI_SOC_VMARGIN:1130504:0x25] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-30.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0xFFFFFFC4][SI_SOC_VMARGIN:1130504:0x0] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-31.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0xFFFFFFC4][SI_SOC_VMARGIN:1130504:0xFFFFFFDA] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-32.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0xFFFFFFC4][SI_SOC_VMARGIN:1130504:0x25] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-33.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x3C][SI_SOC_VMARGIN:1130504:0x0] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-34.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x3C][SI_SOC_VMARGIN:1130504:0xFFFFFFDA] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-35.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x3C][SI_SOC_VMARGIN:1130504:0x25] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-36.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x0][SI_SOC_VMARGIN:1130504:0x0] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-37.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x0][SI_SOC_VMARGIN:1130504:0xFFFFFFDA] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-38.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x0][SI_SOC_VMARGIN:1130504:0x25] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-39.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0xFFFFFFC4][SI_SOC_VMARGIN:1130504:0x0] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-40.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0xFFFFFFC4][SI_SOC_VMARGIN:1130504:0xFFFFFFDA] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-41.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0xFFFFFFC4][SI_SOC_VMARGIN:1130504:0x25] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-42.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x3C][SI_SOC_VMARGIN:1130504:0x0] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-43.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x3C][SI_SOC_VMARGIN:1130504:0xFFFFFFDA] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-44.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x3C][SI_SOC_VMARGIN:1130504:0x25] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-45.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x0][SI_SOC_VMARGIN:1130504:0x0] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-46.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x0][SI_SOC_VMARGIN:1130504:0xFFFFFFDA] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-47.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x0][SI_SOC_VMARGIN:1130504:0x25] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-48.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0xFFFFFFC4][SI_SOC_VMARGIN:1130504:0x0] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-49.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0xFFFFFFC4][SI_SOC_VMARGIN:1130504:0xFFFFFFDA] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-50.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0xFFFFFFC4][SI_SOC_VMARGIN:1130504:0x25] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-51.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x3C][SI_SOC_VMARGIN:1130504:0x0] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-52.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x3C][SI_SOC_VMARGIN:1130504:0xFFFFFFDA] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-53.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x3C][SI_SOC_VMARGIN:1130504:0x25] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-54.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x0][SI_SOC_VMARGIN:1130504:0x0] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-55.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x0][SI_SOC_VMARGIN:1130504:0xFFFFFFDA] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-56.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x0][SI_SOC_VMARGIN:1130504:0x25] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-57.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0xFFFFFFC4][SI_SOC_VMARGIN:1130504:0x0] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-58.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0xFFFFFFC4][SI_SOC_VMARGIN:1130504:0xFFFFFFDA] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-59.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0xFFFFFFC4][SI_SOC_VMARGIN:1130504:0x25] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-60.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x3C][SI_SOC_VMARGIN:1130504:0x0] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-61.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x3C][SI_SOC_VMARGIN:1130504:0xFFFFFFDA] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-62.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x3C][SI_SOC_VMARGIN:1130504:0x25] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-63.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x0][SI_SOC_VMARGIN:1130504:0x0] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-64.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x0][SI_SOC_VMARGIN:1130504:0xFFFFFFDA] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-65.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x0][SI_SOC_VMARGIN:1130504:0x25] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-66.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0xFFFFFFC4][SI_SOC_VMARGIN:1130504:0x0] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-67.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0xFFFFFFC4][SI_SOC_VMARGIN:1130504:0xFFFFFFDA] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-68.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0xFFFFFFC4][SI_SOC_VMARGIN:1130504:0x25] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-69.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x3C][SI_SOC_VMARGIN:1130504:0x0] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-70.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x3C][SI_SOC_VMARGIN:1130504:0xFFFFFFDA] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-71.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x3C][SI_SOC_VMARGIN:1130504:0x25] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-72.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x0][SI_SOC_VMARGIN:1130504:0x0] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-73.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x0][SI_SOC_VMARGIN:1130504:0xFFFFFFDA] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-74.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x0][SI_SOC_VMARGIN:1130504:0x25] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-75.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0xFFFFFFC4][SI_SOC_VMARGIN:1130504:0x0] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-76.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0xFFFFFFC4][SI_SOC_VMARGIN:1130504:0xFFFFFFDA] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-77.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0xFFFFFFC4][SI_SOC_VMARGIN:1130504:0x25] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-78.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x3C][SI_SOC_VMARGIN:1130504:0x0] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-79.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x3C][SI_SOC_VMARGIN:1130504:0xFFFFFFDA] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-80.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x3C][SI_SOC_VMARGIN:1130504:0x25] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-81.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x0][SI_SOC_VMARGIN:1130504:0x0] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-82.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x0][SI_SOC_VMARGIN:1130504:0xFFFFFFDA] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-83.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x0][SI_SOC_VMARGIN:1130504:0x25] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-84.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0xFFFFFFC4][SI_SOC_VMARGIN:1130504:0x0] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-85.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0xFFFFFFC4][SI_SOC_VMARGIN:1130504:0xFFFFFFDA] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-86.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0xFFFFFFC4][SI_SOC_VMARGIN:1130504:0x25] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-87.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x3C][SI_SOC_VMARGIN:1130504:0x0] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-88.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x3C][SI_SOC_VMARGIN:1130504:0xFFFFFFDA] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-89.log --D 1
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x3C][SI_SOC_VMARGIN:1130504:0x25] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor-mem_test-90.log --D 1
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210423_210217/sensor.log --D 1
