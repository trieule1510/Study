./xconsole.py --cmd off --hostuser root --hostip 10.38.172.2 --bmcip 10.38.172.51 --hostpass root --board_type Mt.Jade
./xconsole.py --cmd sel_list --hostuser root --hostip 10.38.172.2 --bmcip 10.38.172.51 --hostpass root --board_type Mt.Jade
./xconsole.py --cmd on --hostuser root --hostip 10.38.172.2 --bmcip 10.38.172.51 --hostpass root --board_type Mt.Jade
cksum cfg/test_script/test_delivery.sh
cksum cfg/test_script/memtester.elf
cksum cfg/test_script/stressapptest.elf
