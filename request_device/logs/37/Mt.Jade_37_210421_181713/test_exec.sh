./xconsole.py --hostuser root --bmcip 10.38.172.51 --board Mt.Jade --set_nvparm [SI_DDR_SCRUB_EN:1146944:0x5A0][SI_DDR_ZQCS_EN:1147208:0x1][SI_DDR_ECC_MODE:1146952:0x1][SI_PLT_EN:1130752:0x0] --debug 0 --hostpass root --hostip 10.38.172.2
./xconsole.py --cmd off --hostuser root --bmcip 10.38.172.51 --board Mt.Jade --debug 0 --hostpass root --hostip 10.38.172.2
./xconsole.py --hostuser root --bmcip 10.38.172.51 --board Mt.Jade --set_nvparm [SI_DDR_VMARGIN:1130496:0xFFFFFFC4] --debug 0 --hostpass root --hostip 10.38.172.2
./xconsole.py --cmd on --hostuser root --bmcip 10.38.172.51 --board Mt.Jade --debug 0 --hostpass root --hostip 10.38.172.2
grep -hn 'Call trace' -R 'logs/37/Mt.Jade_37_210421_181713/Mt.Jade_memtester_300.cfg_at_1_210421_181739uefi.log'
grep -hn 'Call trace' -R 'logs/37/Mt.Jade_37_210421_181713/Mt.Jade_memtester_300.cfg_at_1_210421_181739uefi.log'
./xconsole.py --cmd off --hostuser root --bmcip 10.38.172.51 --board Mt.Jade --debug 0 --hostpass root --hostip 10.38.172.2
./xconsole.py --hostuser root --bmcip 10.38.172.51 --board Mt.Jade --set_nvparm [SI_DDR_VMARGIN:1130496:0x3C] --debug 0 --hostpass root --hostip 10.38.172.2
./xconsole.py --cmd on --hostuser root --bmcip 10.38.172.51 --board Mt.Jade --debug 0 --hostpass root --hostip 10.38.172.2
grep -hn 'Call trace' -R 'logs/37/Mt.Jade_37_210421_181713/Mt.Jade_memtester_300.cfg_at_2_210421_182028uefi.log'
grep -hn 'Call trace' -R 'logs/37/Mt.Jade_37_210421_181713/Mt.Jade_memtester_300.cfg_at_2_210421_182028uefi.log'
./xconsole.py --cmd off --hostuser root --bmcip 10.38.172.51 --board Mt.Jade --debug 0 --hostpass root --hostip 10.38.172.2
./xconsole.py --hostuser root --bmcip 10.38.172.51 --board Mt.Jade --set_nvparm [SI_DDR_VMARGIN:1130496:0xFFFFFFC4] --debug 0 --hostpass root --hostip 10.38.172.2
./xconsole.py --cmd on --hostuser root --bmcip 10.38.172.51 --board Mt.Jade --debug 0 --hostpass root --hostip 10.38.172.2
grep -hn 'Call trace' -R 'logs/37/Mt.Jade_37_210421_181713/Mt.Jade_memtester_300.cfg_at_3_210421_182313uefi.log'
grep -hn 'Call trace' -R 'logs/37/Mt.Jade_37_210421_181713/Mt.Jade_memtester_300.cfg_at_3_210421_182313uefi.log'
./xconsole.py --cmd off --hostuser root --bmcip 10.38.172.51 --board Mt.Jade --debug 0 --hostpass root --hostip 10.38.172.2
./xconsole.py --hostuser root --bmcip 10.38.172.51 --board Mt.Jade --set_nvparm [SI_DDR_VMARGIN:1130496:0x3C] --debug 0 --hostpass root --hostip 10.38.172.2
./xconsole.py --cmd on --hostuser root --bmcip 10.38.172.51 --board Mt.Jade --debug 0 --hostpass root --hostip 10.38.172.2
grep -hn 'Call trace' -R 'logs/37/Mt.Jade_37_210421_181713/Mt.Jade_memtester_300.cfg_at_4_210421_182556uefi.log'
grep -hn 'Call trace' -R 'logs/37/Mt.Jade_37_210421_181713/Mt.Jade_memtester_300.cfg_at_4_210421_182556uefi.log'
