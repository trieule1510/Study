./xconsole.py --cmd cleannv --hostuser amcclab --hostip 10.38.175.31 --bmcip 10.38.14.243 --hostpass amcc1234 --board_type Mt.Jade
./xconsole.py --scp_fw cfg/scp_fw/altra_scp_signed_1.03.20210206.hpm --hostuser amcclab --hostip 10.38.175.31 --bmcip 10.38.14.243 --hostpass amcc1234 --board_type Mt.Jade
./xconsole.py --atfbios_fw cfg/atfbios_fw/jade_aptiov_atf_signed_1.03.20210206.hpm --hostuser amcclab --hostip 10.38.175.31 --bmcip 10.38.14.243 --hostpass amcc1234 --board_type Mt.Jade
./xconsole.py --cmd off --hostuser amcclab --hostip 10.38.175.31 --bmcip 10.38.14.243 --hostpass amcc1234 --board_type Mt.Jade
./xconsole.py --cmd on --hostuser amcclab --hostip 10.38.175.31 --bmcip 10.38.14.243 --hostpass amcc1234 --board_type Mt.Jade
./ipmitool_sensor_chartjs.py --log logs/3/Mt.Jade_3_210505_134356/sensor--1.log --sensor_interval 30
./ipmitool_sensor_chartjs.py --log logs/3/Mt.Jade_3_210505_134356/sensor.log --sensor_interval 30
./ipmitool_sensor_chartjs.py --log logs/3/Mt.Jade_3_210505_134356/sensor.log --D 1 --sensor_interval 30
