./xconsole.py --cmd off --bmcip 10.38.172.46 --board_type Mt.Snow
./xconsole.py --cmd sel_list --bmcip 10.38.172.46 --board_type Mt.Snow
./xconsole.py --set_nvparm [SI_DDR_VMARGIN:1130496:0x0][SI_SOC_VMARGIN:1130504:0x0] --bmcip 10.38.172.46 --board_type Mt.Snow
./xconsole.py --cmd on --bmcip 10.38.172.46 --board_type Mt.Snow
cksum static/test_script/test_delivery.sh
cksum static/test_script/memtester.elf
cksum static/test_script/stressapptest.elf
./xconsole.py --cmd sel_list --bmcip 10.38.172.46 --board_type Mt.Snow
./xconsole.py --cmd sel_list --bmcip 10.38.172.46 --board_type Mt.Snow
./xconsole.py --cmd off --bmcip 10.38.172.46 --board_type Mt.Snow
./xconsole.py --cmd off --bmcip 10.38.172.46 --board_type Mt.Snow
