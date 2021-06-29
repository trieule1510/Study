./xconsole.py --cmd off --bmcip 10.38.172.46 --board_type Mt.Snow
./xconsole.py --cmd sel_list --bmcip 10.38.172.46 --board_type Mt.Snow
./xconsole.py --set_nvparm [SI_DDR_VMARGIN:1130496:0x0][SI_SOC_VMARGIN:1130504:0x0] --bmcip 10.38.172.46 --board_type Mt.Snow
./xconsole.py --cmd on --bmcip 10.38.172.46 --board_type Mt.Snow
./xconsole.py --cmd sel_list --bmcip 10.38.172.46 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/211/Mt.Snow_211_210425_075319/sensor-mem_test-1.log --sensor_interval 30
./xconsole.py --cmd off --bmcip 10.38.172.46 --board_type Mt.Snow
./xconsole.py --cmd sel_list --bmcip 10.38.172.46 --board_type Mt.Snow
./xconsole.py --set_nvparm [SI_DDR_VMARGIN:1130496:0x0][SI_SOC_VMARGIN:1130504:0xFFFFFFDA] --bmcip 10.38.172.46 --board_type Mt.Snow
./xconsole.py --cmd on --bmcip 10.38.172.46 --board_type Mt.Snow
./xconsole.py --cmd sel_list --bmcip 10.38.172.46 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/211/Mt.Snow_211_210425_075319/sensor-mem_test-2.log --sensor_interval 30
./xconsole.py --cmd off --bmcip 10.38.172.46 --board_type Mt.Snow
./xconsole.py --cmd sel_list --bmcip 10.38.172.46 --board_type Mt.Snow
./xconsole.py --set_nvparm [SI_DDR_VMARGIN:1130496:0x0][SI_SOC_VMARGIN:1130504:0x25] --bmcip 10.38.172.46 --board_type Mt.Snow
./xconsole.py --cmd on --bmcip 10.38.172.46 --board_type Mt.Snow
