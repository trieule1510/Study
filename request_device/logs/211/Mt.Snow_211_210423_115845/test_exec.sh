./xconsole.py --cmd off --bmcip 10.38.172.46 --debug 0 --board_type Mt.Snow
./xconsole.py --bmcip 10.38.172.46 --set_nvparm [SI_SOC_VMARGIN:1130504:0x0] --debug 0 --board_type Mt.Snow
./xconsole.py --cmd on --bmcip 10.38.172.46 --debug 0 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/211/Mt.Snow_211_210423_115845/sensor-test_delivery-1.log --D 1
./xconsole.py --cmd off --bmcip 10.38.172.46 --debug 0 --board_type Mt.Snow
./xconsole.py --bmcip 10.38.172.46 --set_nvparm [SI_SOC_VMARGIN:1130504:0xFFFFFFDA] --debug 0 --board_type Mt.Snow
./xconsole.py --cmd on --bmcip 10.38.172.46 --debug 0 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/211/Mt.Snow_211_210423_115845/sensor-test_delivery-2.log --D 1
./xconsole.py --cmd off --bmcip 10.38.172.46 --debug 0 --board_type Mt.Snow
./xconsole.py --bmcip 10.38.172.46 --set_nvparm [SI_SOC_VMARGIN:1130504:0x25] --debug 0 --board_type Mt.Snow
./xconsole.py --cmd on --bmcip 10.38.172.46 --debug 0 --board_type Mt.Snow
