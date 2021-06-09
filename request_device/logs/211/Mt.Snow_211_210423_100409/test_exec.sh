./xconsole.py --cmd off --bmcip 10.38.172.46 --debug 0 --board_type Mt.Snow
./xconsole.py --cmd on --bmcip 10.38.172.46 --debug 0 --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/211/Mt.Snow_211_210423_100409/sensor-test_delivery-1.log --D 1
./ipmitool_sensor_chartjs.py --log logs/211/Mt.Snow_211_210423_100409/sensor.log --D 1
