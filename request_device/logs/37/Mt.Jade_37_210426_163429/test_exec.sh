./xconsole.py --scp_fw cfg/scp_fw/altra_scp_signed_1.05.20210422.hpm --hostuser root --hostip 10.38.172.2 --bmcip 10.38.172.51 --hostpass root --board_type Mt.Jade
./xconsole.py --atfbios_fw cfg/atfbios_fw/jade_aptiov_atf_signed_1.05.20210422.hpm --hostuser root --hostip 10.38.172.2 --bmcip 10.38.172.51 --hostpass root --board_type Mt.Jade
./xconsole.py --cmd off --hostuser root --hostip 10.38.172.2 --bmcip 10.38.172.51 --hostpass root --board_type Mt.Jade
./xconsole.py --cmd sel_list --hostuser root --hostip 10.38.172.2 --bmcip 10.38.172.51 --hostpass root --board_type Mt.Jade
./xconsole.py --cmd on --hostuser root --hostip 10.38.172.2 --bmcip 10.38.172.51 --hostpass root --board_type Mt.Jade
./xconsole.py --cmd sel_list --hostuser root --hostip 10.38.172.2 --bmcip 10.38.172.51 --hostpass root --board_type Mt.Jade
