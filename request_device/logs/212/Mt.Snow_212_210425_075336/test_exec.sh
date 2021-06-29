./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x0][SI_SOC_VMARGIN:1130504:0x0] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210425_075336/sensor-mem_test-1.log --sensor_interval 30
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x0][SI_SOC_VMARGIN:1130504:0xFFFFFFDA] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/212/Mt.Snow_212_210425_075336/sensor-mem_test-2.log --sensor_interval 30
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x0][SI_SOC_VMARGIN:1130504:0x25] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
