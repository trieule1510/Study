./xconsole.py --cmd 1 --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --scp_fw cfg/scp_fw/MP32_AR0_scp_signed_1.04.20210223_SHA256.hpm --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --atfbios_fw cfg/atfbios_fw/MP32-AR0.F09b3.hpm --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x0][SI_SOC_VMARGIN:1130504:0x0] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
cksum static/test_script/test_delivery.sh
cksum static/test_script/memtester.elf
cksum static/test_script/stressapptest.elf
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x0][SI_SOC_VMARGIN:1130504:0xFFFFFFDA] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
cksum static/test_script/test_delivery.sh
cksum static/test_script/memtester.elf
cksum static/test_script/stressapptest.elf
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0x0][SI_SOC_VMARGIN:1130504:0x25] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
cksum static/test_script/test_delivery.sh
cksum static/test_script/memtester.elf
cksum static/test_script/stressapptest.elf
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0xFFFFFFC4][SI_SOC_VMARGIN:1130504:0x0] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
cksum static/test_script/test_delivery.sh
cksum static/test_script/memtester.elf
cksum static/test_script/stressapptest.elf
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd off --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd sel_list --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --hostip 10.38.172.2 --set_nvparm [SI_DDR_VMARGIN:1130496:0xFFFFFFC4][SI_SOC_VMARGIN:1130504:0xFFFFFFDA] --bmcip 10.38.172.48 --board_type Mt.Snow
./xconsole.py --cmd on --hostip 10.38.172.2 --bmcip 10.38.172.48 --board_type Mt.Snow
