./xconsole.py --tty_bmc FTDBIL23 --hostuser root --bmc_fw cfg/bmc_fw/jade_bmc_1.05.210423.ima --hostip 10.38.172.2 --bmcip 10.38.172.51 --hostpass root --board_type Mt.Jade
./xconsole.py --scp_fw cfg/scp_fw/altra_scp_signed_1.05.20210422.hpm --hostuser root --hostip 10.38.172.2 --bmcip 10.38.172.51 --hostpass root --board_type Mt.Jade
./xconsole.py --atfbios_fw cfg/atfbios_fw/jade_aptiov_atf_signed_1.05.20210422.hpm --hostuser root --hostip 10.38.172.2 --bmcip 10.38.172.51 --hostpass root --board_type Mt.Jade
./xconsole.py --hostip 10.38.172.2 --hostuser root --set_nvparm [SI_DDR_SCRUB_EN:1146944:0x5A0][SI_DDR_ZQCS_EN:1147208:0x1][SI_DDR_ECC_MODE:1146952:0x1][SI_PLT_EN:1130752:0x0] --bmcip 10.38.172.51 --hostpass root --board_type Mt.Jade
./xconsole.py --hostip 10.38.172.2 --hostuser root --set_nvparm [SI_DDR_SCRUB_EN:1146944:0x5A0][SI_DDR_ZQCS_EN:1147208:0x1][SI_DDR_ECC_MODE:1146952:0x1][SI_PLT_EN:1130752:0x0] --bmcip 10.38.172.51 --hostpass root --board_type Mt.Jade
./xconsole.py --tty_bmc FTDBIL23 --hostuser root --bmc_fw cfg/bmc_fw/jade_bmc_1.05.210423.ima --hostip 10.38.172.2 --bmcip 10.38.172.51 --hostpass root --board_type Mt.Jade
