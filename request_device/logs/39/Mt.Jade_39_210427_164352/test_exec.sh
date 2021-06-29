./xconsole.py --scp_fw cfg/scp_fw/altra_scp_signed_1.05.20210422.hpm --hostuser amplab --hostip 10.38.165.3 --bmcip 10.38.165.32 --hostpass Ampere@4655 --board_type Mt.Jade
./xconsole.py --atfbios_fw cfg/atfbios_fw/jade_aptiov_atf_signed_1.05.20210422.hpm --hostuser amplab --hostip 10.38.165.3 --bmcip 10.38.165.32 --hostpass Ampere@4655 --board_type Mt.Jade
./xconsole.py --cmd off --hostuser amplab --hostip 10.38.165.3 --bmcip 10.38.165.32 --hostpass Ampere@4655 --board_type Mt.Jade
./xconsole.py --cmd sel_list --hostuser amplab --hostip 10.38.165.3 --bmcip 10.38.165.32 --hostpass Ampere@4655 --board_type Mt.Jade
./xconsole.py --cmd on --hostuser amplab --hostip 10.38.165.3 --bmcip 10.38.165.32 --hostpass Ampere@4655 --board_type Mt.Jade
