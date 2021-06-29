./xconsole.py --cmd cleannv --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --scp_fw cfg/scp_fw/MP32_AR0_scp_signed_1.04.20210223_SHA256.hpm --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --atfbios_fw cfg/atfbios_fw/MP32-AR0.F09b3.hpm --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --cmd off --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --cmd sel_list --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --cmd on --bmcip 10.38.165.34 --board_type Mt.Snow
./xconsole.py --cmd sel_list --bmcip 10.38.165.34 --board_type Mt.Snow
