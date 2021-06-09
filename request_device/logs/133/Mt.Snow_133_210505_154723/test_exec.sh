./xconsole.py --cmd cleannv --hostuser root --hostip 10.38.172.2 --bmcip 10.38.172.63 --hostpass root --board_type Mt.Snow
./xconsole.py --scp_fw cfg/scp_fw/MP32_AR0_scp_signed_1.04.20210223_SHA256.hpm --hostuser root --hostip 10.38.172.2 --bmcip 10.38.172.63 --hostpass root --board_type Mt.Snow
./xconsole.py --atfbios_fw cfg/atfbios_fw/MP32-AR0.F09b3.hpm --hostuser root --hostip 10.38.172.2 --bmcip 10.38.172.63 --hostpass root --board_type Mt.Snow
./xconsole.py --cmd off --hostuser root --hostip 10.38.172.2 --bmcip 10.38.172.63 --hostpass root --board_type Mt.Snow
./xconsole.py --cmd on --hostuser root --hostip 10.38.172.2 --bmcip 10.38.172.63 --hostpass root --board_type Mt.Snow
./ipmitool_sensor_chartjs.py --log logs/133/Mt.Snow_133_210505_154723/sensor--1.log --sensor_interval 30
./ipmitool_sensor_chartjs.py --log logs/133/Mt.Snow_133_210505_154723/sensor.log --sensor_interval 30
./ipmitool_sensor_chartjs.py --log logs/133/Mt.Snow_133_210505_154723/sensor.log --D 1 --sensor_interval 30
