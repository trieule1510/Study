./xconsole.py --cmd off --bmcip 10.38.172.46 --debug 1 --board_type Mt.Snow
./xconsole.py --cmd on --bmcip 10.38.172.46 --debug 1 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/211/Mt.Snow_211_210423_114017/sensor-test_delivery-1.log --D 1
./ipmitool_sensor_chartjs.py --log logs/211/Mt.Snow_211_210423_114017/sensor.log --D 1
