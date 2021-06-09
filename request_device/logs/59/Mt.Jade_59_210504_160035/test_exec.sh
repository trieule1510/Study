./xconsole.py --scp_fw cfg/scp_fw/altra_scp_signed_1.05.20210426_59.hpm --hostuser amcclab --hostip 10.38.175.31 --bmcip 10.38.175.43 --hostpass amcc1234 --board_type Mt.Jade
./xconsole.py --atfbios_fw cfg/atfbios_fw/jade_aptiov_atf_signed_1.05.20210426.hpm --hostuser amcclab --hostip 10.38.175.31 --bmcip 10.38.175.43 --hostpass amcc1234 --board_type Mt.Jade
./xconsole.py --cmd off --hostuser amcclab --hostip 10.38.175.31 --bmcip 10.38.175.43 --hostpass amcc1234 --board_type Mt.Jade
./xconsole.py --cmd on --hostuser amcclab --hostip 10.38.175.31 --bmcip 10.38.175.43 --hostpass amcc1234 --board_type Mt.Jade
./ipmitool_sensor_chartjs.py --log logs/59/Mt.Jade_59_210504_160035/sensor--1.log --sensor_interval 30
./ipmitool_sensor_chartjs.py --log logs/59/Mt.Jade_59_210504_160035/sensor.log --sensor_interval 30
./ipmitool_sensor_chartjs.py --log logs/59/Mt.Jade_59_210504_160035/sensor.log --D 1 --sensor_interval 30
