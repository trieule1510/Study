./xconsole.py --hostip 10.38.172.2 --hostuser root --set_nvparm [SI_DDR_SCRUB_EN:1146944:0x5A0][SI_DDR_ZQCS_EN:1147208:0x1][SI_DDR_ECC_MODE:1146952:0x1][SI_PLT_EN:1130752:0x0] --bmcip 10.38.172.51 --hostpass root --board_type Mt.Jade
./xconsole.py --cmd off --hostuser root --hostip 10.38.172.2 --bmcip 10.38.172.51 --hostpass root --board_type Mt.Jade
./xconsole.py --cmd sel_list --hostuser root --hostip 10.38.172.2 --bmcip 10.38.172.51 --hostpass root --board_type Mt.Jade
./xconsole.py --hostip 10.38.172.2 --hostuser root --set_nvparm [SI_DDR_VMARGIN:1130496:0x0] --bmcip 10.38.172.51 --hostpass root --board_type Mt.Jade
./xconsole.py --cmd on --hostuser root --hostip 10.38.172.2 --bmcip 10.38.172.51 --hostpass root --board_type Mt.Jade
