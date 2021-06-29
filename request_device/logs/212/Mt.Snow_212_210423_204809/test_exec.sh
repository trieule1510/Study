./xconsole.py --bmcip 10.38.172.48 --set_nvparm [SI_DDR_SCRUB_EN:1146944:0x5A0][SI_DDR_ZQCS_EN:1147208:0x1][SI_DDR_ECC_MODE:1146952:0x1][SI_PLT_EN:1130752:0x0] --debug 1 --hostip 10.38.172.2 --board_type Mt.Snow
./xconsole.py --cmd off --bmcip 10.38.172.48 --debug 1 --hostip 10.38.172.2 --board_type Mt.Snow
./xconsole.py --bmcip 10.38.172.48 --set_nvparm [SI_DDR_VMARGIN:1130496:0xFFFFFFC4] --debug 1 --hostip 10.38.172.2 --board_type Mt.Snow
./xconsole.py --cmd on --bmcip 10.38.172.48 --debug 1 --hostip 10.38.172.2 --board_type Mt.Snow
./xconsole.py --cmd off --bmcip 10.38.172.48 --debug 1 --hostip 10.38.172.2 --board_type Mt.Snow
./xconsole.py --bmcip 10.38.172.48 --set_nvparm [SI_DDR_VMARGIN:1130496:0x3C] --debug 1 --hostip 10.38.172.2 --board_type Mt.Snow
./xconsole.py --cmd on --bmcip 10.38.172.48 --debug 1 --hostip 10.38.172.2 --board_type Mt.Snow
