./xconsole.py --cmd off --hostuser amcclab --hostip 10.38.175.31 --bmcip 10.38.175.43 --hostpass amcc1234 --board_type Mt.Jade
./xconsole.py --cmd sel_list --hostuser amcclab --hostip 10.38.175.31 --bmcip 10.38.175.43 --hostpass amcc1234 --board_type Mt.Jade
./xconsole.py --cmd on --hostuser amcclab --hostip 10.38.175.31 --bmcip 10.38.175.43 --hostpass amcc1234 --board_type Mt.Jade
./xconsole.py --cmd sel_list --hostuser amcclab --hostip 10.38.175.31 --bmcip 10.38.175.43 --hostpass amcc1234 --board_type Mt.Jade
./ipmitool_sensor_chartjs.py --log logs/59/Mt.Jade_59_210505_124919/sensor--1.log --sensor_interval 30
