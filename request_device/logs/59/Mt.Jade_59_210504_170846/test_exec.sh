./xconsole.py --cmd off --hostuser amcclab --hostip 10.38.175.31 --bmcip 10.38.175.43 --hostpass amcc1234 --board_type Mt.Jade
./xconsole.py --hostip 10.38.175.31 --hostuser amcclab --set_nvparm [SI_SOC_VMARGIN:1130504:0x0][SI_DDR_VMARGIN:1130496:0x0] --bmcip 10.38.175.43 --hostpass amcc1234 --board_type Mt.Jade
./xconsole.py --cmd on --hostuser amcclab --hostip 10.38.175.31 --bmcip 10.38.175.43 --hostpass amcc1234 --board_type Mt.Jade
cksum static/test_script/mem_test.sh
cksum static/test_script/memtester.elf
./ipmitool_sensor_chartjs.py --log logs/59/Mt.Jade_59_210504_170846/sensor-mem_test-1.log --sensor_interval 30
./xconsole.py --cmd off --hostuser amcclab --hostip 10.38.175.31 --bmcip 10.38.175.43 --hostpass amcc1234 --board_type Mt.Jade
./xconsole.py --hostip 10.38.175.31 --hostuser amcclab --set_nvparm [SI_SOC_VMARGIN:1130504:0x0][SI_DDR_VMARGIN:1130496:0xFFFFFFC4] --bmcip 10.38.175.43 --hostpass amcc1234 --board_type Mt.Jade
./xconsole.py --cmd on --hostuser amcclab --hostip 10.38.175.31 --bmcip 10.38.175.43 --hostpass amcc1234 --board_type Mt.Jade
cksum static/test_script/mem_test.sh
cksum static/test_script/memtester.elf
./ipmitool_sensor_chartjs.py --log logs/59/Mt.Jade_59_210504_170846/sensor-mem_test-2.log --sensor_interval 30
./xconsole.py --cmd off --hostuser amcclab --hostip 10.38.175.31 --bmcip 10.38.175.43 --hostpass amcc1234 --board_type Mt.Jade
./xconsole.py --hostip 10.38.175.31 --hostuser amcclab --set_nvparm [SI_SOC_VMARGIN:1130504:0x0][SI_DDR_VMARGIN:1130496:0x3C] --bmcip 10.38.175.43 --hostpass amcc1234 --board_type Mt.Jade
./xconsole.py --cmd on --hostuser amcclab --hostip 10.38.175.31 --bmcip 10.38.175.43 --hostpass amcc1234 --board_type Mt.Jade
cksum static/test_script/mem_test.sh
cksum static/test_script/memtester.elf
./ipmitool_sensor_chartjs.py --log logs/59/Mt.Jade_59_210504_170846/sensor-mem_test-3.log --sensor_interval 30
./xconsole.py --cmd off --hostuser amcclab --hostip 10.38.175.31 --bmcip 10.38.175.43 --hostpass amcc1234 --board_type Mt.Jade
./xconsole.py --hostip 10.38.175.31 --hostuser amcclab --set_nvparm [SI_SOC_VMARGIN:1130504:0xFFFFFFDA][SI_DDR_VMARGIN:1130496:0x0] --bmcip 10.38.175.43 --hostpass amcc1234 --board_type Mt.Jade
./xconsole.py --cmd on --hostuser amcclab --hostip 10.38.175.31 --bmcip 10.38.175.43 --hostpass amcc1234 --board_type Mt.Jade
cksum static/test_script/mem_test.sh
cksum static/test_script/memtester.elf
./ipmitool_sensor_chartjs.py --log logs/59/Mt.Jade_59_210504_170846/sensor-mem_test-4.log --sensor_interval 30
./xconsole.py --cmd off --hostuser amcclab --hostip 10.38.175.31 --bmcip 10.38.175.43 --hostpass amcc1234 --board_type Mt.Jade
./xconsole.py --hostip 10.38.175.31 --hostuser amcclab --set_nvparm [SI_SOC_VMARGIN:1130504:0xFFFFFFDA][SI_DDR_VMARGIN:1130496:0xFFFFFFC4] --bmcip 10.38.175.43 --hostpass amcc1234 --board_type Mt.Jade
./xconsole.py --cmd on --hostuser amcclab --hostip 10.38.175.31 --bmcip 10.38.175.43 --hostpass amcc1234 --board_type Mt.Jade
cksum static/test_script/mem_test.sh
cksum static/test_script/memtester.elf
./ipmitool_sensor_chartjs.py --log logs/59/Mt.Jade_59_210504_170846/sensor-mem_test-5.log --sensor_interval 30
./xconsole.py --cmd off --hostuser amcclab --hostip 10.38.175.31 --bmcip 10.38.175.43 --hostpass amcc1234 --board_type Mt.Jade
./xconsole.py --hostip 10.38.175.31 --hostuser amcclab --set_nvparm [SI_SOC_VMARGIN:1130504:0xFFFFFFDA][SI_DDR_VMARGIN:1130496:0x3C] --bmcip 10.38.175.43 --hostpass amcc1234 --board_type Mt.Jade
./xconsole.py --cmd on --hostuser amcclab --hostip 10.38.175.31 --bmcip 10.38.175.43 --hostpass amcc1234 --board_type Mt.Jade
cksum static/test_script/mem_test.sh
cksum static/test_script/memtester.elf
./ipmitool_sensor_chartjs.py --log logs/59/Mt.Jade_59_210504_170846/sensor-mem_test-6.log --sensor_interval 30
./xconsole.py --cmd off --hostuser amcclab --hostip 10.38.175.31 --bmcip 10.38.175.43 --hostpass amcc1234 --board_type Mt.Jade
./xconsole.py --hostip 10.38.175.31 --hostuser amcclab --set_nvparm [SI_SOC_VMARGIN:1130504:0x25][SI_DDR_VMARGIN:1130496:0x0] --bmcip 10.38.175.43 --hostpass amcc1234 --board_type Mt.Jade
./xconsole.py --cmd on --hostuser amcclab --hostip 10.38.175.31 --bmcip 10.38.175.43 --hostpass amcc1234 --board_type Mt.Jade
cksum static/test_script/mem_test.sh
cksum static/test_script/memtester.elf
./ipmitool_sensor_chartjs.py --log logs/59/Mt.Jade_59_210504_170846/sensor-mem_test-7.log --sensor_interval 30
./xconsole.py --cmd off --hostuser amcclab --hostip 10.38.175.31 --bmcip 10.38.175.43 --hostpass amcc1234 --board_type Mt.Jade
./xconsole.py --hostip 10.38.175.31 --hostuser amcclab --set_nvparm [SI_SOC_VMARGIN:1130504:0x25][SI_DDR_VMARGIN:1130496:0xFFFFFFC4] --bmcip 10.38.175.43 --hostpass amcc1234 --board_type Mt.Jade
./xconsole.py --cmd on --hostuser amcclab --hostip 10.38.175.31 --bmcip 10.38.175.43 --hostpass amcc1234 --board_type Mt.Jade
cksum static/test_script/mem_test.sh
cksum static/test_script/memtester.elf
./ipmitool_sensor_chartjs.py --log logs/59/Mt.Jade_59_210504_170846/sensor-mem_test-8.log --sensor_interval 30
./xconsole.py --cmd off --hostuser amcclab --hostip 10.38.175.31 --bmcip 10.38.175.43 --hostpass amcc1234 --board_type Mt.Jade
./xconsole.py --hostip 10.38.175.31 --hostuser amcclab --set_nvparm [SI_SOC_VMARGIN:1130504:0x25][SI_DDR_VMARGIN:1130496:0x3C] --bmcip 10.38.175.43 --hostpass amcc1234 --board_type Mt.Jade
./xconsole.py --cmd on --hostuser amcclab --hostip 10.38.175.31 --bmcip 10.38.175.43 --hostpass amcc1234 --board_type Mt.Jade
cksum static/test_script/mem_test.sh
cksum static/test_script/memtester.elf
./ipmitool_sensor_chartjs.py --log logs/59/Mt.Jade_59_210504_170846/sensor-mem_test-9.log --sensor_interval 30
./ipmitool_sensor_chartjs.py --log logs/59/Mt.Jade_59_210504_170846/sensor.log --sensor_interval 30
./ipmitool_sensor_chartjs.py --log logs/59/Mt.Jade_59_210504_170846/sensor.log --D 1 --sensor_interval 30
