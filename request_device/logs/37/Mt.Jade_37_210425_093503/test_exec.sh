./xconsole.py --cmd off --hostuser root --hostip 10.38.172.2 --bmcip 10.38.172.51 --hostpass root --board_type Mt.Jade
./xconsole.py --cmd sel_list --hostuser root --hostip 10.38.172.2 --bmcip 10.38.172.51 --hostpass root --board_type Mt.Jade
./xconsole.py --hostip 10.38.172.2 --hostuser root --set_nvparm [SI_RO_BOARD_S1_DIMM_AVAIL:6225960:0x3][SI_RO_BOARD_S0_DIMM_AVAIL:6225952:0x3] --bmcip 10.38.172.51 --hostpass root --board_type Mt.Jade
./xconsole.py --cmd on --hostuser root --hostip 10.38.172.2 --bmcip 10.38.172.51 --hostpass root --board_type Mt.Jade
cksum static/test_script/test_delivery.sh
cksum static/test_script/memtester.elf
cksum static/test_script/stressapptest.elf
