./xconsole.py --cmd off --hostuser root --hostip 10.38.172.2 --bmcip 10.38.172.63 --hostpass root --board_type Mt.Snow
./xconsole.py --cmd on --hostuser root --hostip 10.38.172.2 --bmcip 10.38.172.63 --hostpass root --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/133/Mt.Snow_133_210505_154304/sensor--1.log --sensor_interval 30
./ipmitool_sensor_chartjs.py --log logs/133/Mt.Snow_133_210505_154304/sensor.log --sensor_interval 30
./ipmitool_sensor_chartjs.py --log logs/133/Mt.Snow_133_210505_154304/sensor.log --D 1 --sensor_interval 30
