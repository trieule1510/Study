./xconsole.py --cmd off --hostuser root --hostip 10.38.172.2 --bmcip 10.38.172.51 --hostpass root --board_type Mt.Jade
./xconsole.py --cmd sel_list --hostuser root --hostip 10.38.172.2 --bmcip 10.38.172.51 --hostpass root --board_type Mt.Jade
./xconsole.py --hostip 10.38.172.2 --hostuser root --set_nvparm [SI_S0_PCP_ACTIVECPM_32_63:1146888:0xFFFFFFFF][SI_RO_BOARD_S0_DIMM_AVAIL:6225952:0xFFFF][SI_PLT_Y_BOTTOM:1130840:0xFFFFFFE8][SI_DDR_ECC_MODE:1146952:0x0][SI_PLT_Y_PARAM:1130808:0x2][SI_PLT_X_RIGHT:1130824:0x50][SI_RAS_BERT_ENABLED:1147080:0x1][SI_PLT_EN:1130752:0x1][SI_RO_BOARD_S1_DIMM_AVAIL:6225960:0xFFFF][SI_DDR_SCRUB_EN:1146944:0x0][SI_PLT_X_STEP:1130832:0x4][SI_S0_PCP_ACTIVECPM_0_31:1146880:0xFFFFFFFF][SI_S1_PCP_ACTIVECPM_0_31:1146896:0xFFFFFFFF][SI_PLT_Y_TOP:1130848:0x18][SI_PLT_X_PARAM:1130800:0x3][SI_S1_PCP_ACTIVECPM_32_63:1146904:0xFFFFFFFF][SI_PLT_Y_STEP:1130856:0x2][SI_PLT_X_LEFT:1130816:0xFFFFFFB0][SI_DDR_ZQCS_EN:1147208:0x0] --bmcip 10.38.172.51 --hostpass root --board_type Mt.Jade
./xconsole.py --cmd on --hostuser root --hostip 10.38.172.2 --bmcip 10.38.172.51 --hostpass root --board_type Mt.Jade
./xconsole.py --cmd sel_list --hostuser root --hostip 10.38.172.2 --bmcip 10.38.172.51 --hostpass root --board_type Mt.Jade
./ipmitool_sensor_chartjs.py --log logs/37/Mt.Jade_37_210426_141129/sensor-ddr_margin-1.log --sensor_interval 30
./xconsole.py --cmd off --hostuser root --hostip 10.38.172.2 --bmcip 10.38.172.51 --hostpass root --board_type Mt.Jade
./xconsole.py --cmd sel_list --hostuser root --hostip 10.38.172.2 --bmcip 10.38.172.51 --hostpass root --board_type Mt.Jade
./xconsole.py --hostip 10.38.172.2 --hostuser root --set_nvparm [SI_S0_PCP_ACTIVECPM_32_63:1146888:0xFFFFFFFF][SI_RO_BOARD_S0_DIMM_AVAIL:6225952:0xFFFF][SI_PLT_Y_BOTTOM:1130840:0xFFFFFFE8][SI_DDR_ECC_MODE:1146952:0x0][SI_PLT_Y_PARAM:1130808:0x1][SI_PLT_X_RIGHT:1130824:0x50][SI_RAS_BERT_ENABLED:1147080:0x1][SI_PLT_EN:1130752:0x1][SI_RO_BOARD_S1_DIMM_AVAIL:6225960:0xFFFF][SI_DDR_SCRUB_EN:1146944:0x0][SI_PLT_X_STEP:1130832:0x4][SI_S0_PCP_ACTIVECPM_0_31:1146880:0xFFFFFFFF][SI_S1_PCP_ACTIVECPM_0_31:1146896:0xFFFFFFFF][SI_PLT_Y_TOP:1130848:0x18][SI_PLT_X_PARAM:1130800:0x2][SI_S1_PCP_ACTIVECPM_32_63:1146904:0xFFFFFFFF][SI_PLT_Y_STEP:1130856:0x2][SI_PLT_X_LEFT:1130816:0xFFFFFFB0][SI_DDR_ZQCS_EN:1147208:0x0] --bmcip 10.38.172.51 --hostpass root --board_type Mt.Jade
./xconsole.py --cmd on --hostuser root --hostip 10.38.172.2 --bmcip 10.38.172.51 --hostpass root --board_type Mt.Jade
./xconsole.py --cmd sel_list --hostuser root --hostip 10.38.172.2 --bmcip 10.38.172.51 --hostpass root --board_type Mt.Jade
./ipmitool_sensor_chartjs.py --log logs/37/Mt.Jade_37_210426_141129/sensor-ddr_margin-2.log --sensor_interval 30
./xconsole.py --cmd off --hostuser root --hostip 10.38.172.2 --bmcip 10.38.172.51 --hostpass root --board_type Mt.Jade
./xconsole.py --cmd sel_list --hostuser root --hostip 10.38.172.2 --bmcip 10.38.172.51 --hostpass root --board_type Mt.Jade
./xconsole.py --hostip 10.38.172.2 --hostuser root --set_nvparm [SI_S0_PCP_ACTIVECPM_32_63:1146888:0xFFFFFFFF][SI_RO_BOARD_S0_DIMM_AVAIL:6225952:0xFFFF][SI_PLT_Y_BOTTOM:1130840:0xFFFFFFE8][SI_DDR_ECC_MODE:1146952:0x0][SI_PLT_Y_PARAM:1130808:0x1][SI_PLT_X_RIGHT:1130824:0x50][SI_RAS_BERT_ENABLED:1147080:0x1][SI_PLT_EN:1130752:0x1][SI_RO_BOARD_S1_DIMM_AVAIL:6225960:0xFFFF][SI_DDR_SCRUB_EN:1146944:0x0][SI_PLT_X_STEP:1130832:0x4][SI_S0_PCP_ACTIVECPM_0_31:1146880:0xFFFFFFFF][SI_S1_PCP_ACTIVECPM_0_31:1146896:0xFFFFFFFF][SI_PLT_Y_TOP:1130848:0x18][SI_PLT_X_PARAM:1130800:0x1][SI_S1_PCP_ACTIVECPM_32_63:1146904:0xFFFFFFFF][SI_PLT_Y_STEP:1130856:0x2][SI_PLT_X_LEFT:1130816:0xFFFFFFB0][SI_DDR_ZQCS_EN:1147208:0x0] --bmcip 10.38.172.51 --hostpass root --board_type Mt.Jade
./xconsole.py --cmd on --hostuser root --hostip 10.38.172.2 --bmcip 10.38.172.51 --hostpass root --board_type Mt.Jade
./xconsole.py --cmd sel_list --hostuser root --hostip 10.38.172.2 --bmcip 10.38.172.51 --hostpass root --board_type Mt.Jade
./ipmitool_sensor_chartjs.py --log logs/37/Mt.Jade_37_210426_141129/sensor-ddr_margin-3.log --sensor_interval 30
./xconsole.py --cmd off --hostuser root --hostip 10.38.172.2 --bmcip 10.38.172.51 --hostpass root --board_type Mt.Jade
./xconsole.py --cmd sel_list --hostuser root --hostip 10.38.172.2 --bmcip 10.38.172.51 --hostpass root --board_type Mt.Jade
./xconsole.py --hostip 10.38.172.2 --hostuser root --set_nvparm [SI_S0_PCP_ACTIVECPM_32_63:1146888:0xFFFFFFFF][SI_RO_BOARD_S0_DIMM_AVAIL:6225952:0xFFFF][SI_PLT_Y_BOTTOM:1130840:0xFFFFFFE8][SI_DDR_ECC_MODE:1146952:0x0][SI_PLT_Y_PARAM:1130808:0x1][SI_PLT_X_RIGHT:1130824:0x50][SI_RAS_BERT_ENABLED:1147080:0x1][SI_PLT_EN:1130752:0x1][SI_RO_BOARD_S1_DIMM_AVAIL:6225960:0xFFFF][SI_DDR_SCRUB_EN:1146944:0x0][SI_PLT_X_STEP:1130832:0x4][SI_S0_PCP_ACTIVECPM_0_31:1146880:0xFFFFFFFF][SI_S1_PCP_ACTIVECPM_0_31:1146896:0xFFFFFFFF][SI_PLT_Y_TOP:1130848:0x18][SI_PLT_X_PARAM:1130800:0x6][SI_S1_PCP_ACTIVECPM_32_63:1146904:0xFFFFFFFF][SI_PLT_Y_STEP:1130856:0x2][SI_PLT_X_LEFT:1130816:0xFFFFFFB0][SI_DDR_ZQCS_EN:1147208:0x0] --bmcip 10.38.172.51 --hostpass root --board_type Mt.Jade
./xconsole.py --cmd on --hostuser root --hostip 10.38.172.2 --bmcip 10.38.172.51 --hostpass root --board_type Mt.Jade
./xconsole.py --cmd sel_list --hostuser root --hostip 10.38.172.2 --bmcip 10.38.172.51 --hostpass root --board_type Mt.Jade
./ipmitool_sensor_chartjs.py --log logs/37/Mt.Jade_37_210426_141129/sensor-ddr_margin-4.log --sensor_interval 30
./ipmitool_sensor_chartjs.py --log logs/37/Mt.Jade_37_210426_141129/sensor.log --D 1 --sensor_interval 30
./xconsole.py --hostip 10.38.172.2 --hostuser root --set_nvparm [SI_DDR_SCRUB_EN:1146944:0x5A0][SI_DDR_ZQCS_EN:1147208:0x1][SI_DDR_ECC_MODE:1146952:0x1][SI_PLT_EN:1130752:0x0] --bmcip 10.38.172.51 --hostpass root --board_type Mt.Jade
./xconsole.py --cmd off --hostuser root --hostip 10.38.172.2 --bmcip 10.38.172.51 --hostpass root --board_type Mt.Jade
./xconsole.py --cmd sel_list --hostuser root --hostip 10.38.172.2 --bmcip 10.38.172.51 --hostpass root --board_type Mt.Jade
./xconsole.py --hostip 10.38.172.2 --hostuser root --set_nvparm [SI_DDR_VMARGIN:1130496:0x0][SI_SOC_VMARGIN:1130504:0x0] --bmcip 10.38.172.51 --hostpass root --board_type Mt.Jade
./xconsole.py --cmd on --hostuser root --hostip 10.38.172.2 --bmcip 10.38.172.51 --hostpass root --board_type Mt.Jade
cksum static/test_script/test_delivery.sh
cksum static/test_script/memtester.elf
cksum static/test_script/stressapptest.elf
./xconsole.py --cmd sel_list --hostuser root --hostip 10.38.172.2 --bmcip 10.38.172.51 --hostpass root --board_type Mt.Jade
./ipmitool_sensor_chartjs.py --log logs/37/Mt.Jade_37_210426_141129/sensor-test_delivery-1.log --sensor_interval 30
./xconsole.py --cmd off --hostuser root --hostip 10.38.172.2 --bmcip 10.38.172.51 --hostpass root --board_type Mt.Jade
./xconsole.py --cmd sel_list --hostuser root --hostip 10.38.172.2 --bmcip 10.38.172.51 --hostpass root --board_type Mt.Jade
./xconsole.py --hostip 10.38.172.2 --hostuser root --set_nvparm [SI_DDR_VMARGIN:1130496:0x0][SI_SOC_VMARGIN:1130504:0xFFFFFFDA] --bmcip 10.38.172.51 --hostpass root --board_type Mt.Jade
./xconsole.py --cmd on --hostuser root --hostip 10.38.172.2 --bmcip 10.38.172.51 --hostpass root --board_type Mt.Jade
cksum static/test_script/test_delivery.sh
cksum static/test_script/memtester.elf
cksum static/test_script/stressapptest.elf
./xconsole.py --cmd sel_list --hostuser root --hostip 10.38.172.2 --bmcip 10.38.172.51 --hostpass root --board_type Mt.Jade
./ipmitool_sensor_chartjs.py --log logs/37/Mt.Jade_37_210426_141129/sensor-test_delivery-2.log --sensor_interval 30
./xconsole.py --cmd off --hostuser root --hostip 10.38.172.2 --bmcip 10.38.172.51 --hostpass root --board_type Mt.Jade
./xconsole.py --cmd sel_list --hostuser root --hostip 10.38.172.2 --bmcip 10.38.172.51 --hostpass root --board_type Mt.Jade
./xconsole.py --hostip 10.38.172.2 --hostuser root --set_nvparm [SI_DDR_VMARGIN:1130496:0x0][SI_SOC_VMARGIN:1130504:0x25] --bmcip 10.38.172.51 --hostpass root --board_type Mt.Jade
./xconsole.py --cmd on --hostuser root --hostip 10.38.172.2 --bmcip 10.38.172.51 --hostpass root --board_type Mt.Jade
cksum static/test_script/test_delivery.sh
cksum static/test_script/memtester.elf
cksum static/test_script/stressapptest.elf
./xconsole.py --cmd sel_list --hostuser root --hostip 10.38.172.2 --bmcip 10.38.172.51 --hostpass root --board_type Mt.Jade
./ipmitool_sensor_chartjs.py --log logs/37/Mt.Jade_37_210426_141129/sensor-test_delivery-3.log --sensor_interval 30
./xconsole.py --cmd off --hostuser root --hostip 10.38.172.2 --bmcip 10.38.172.51 --hostpass root --board_type Mt.Jade
./xconsole.py --cmd sel_list --hostuser root --hostip 10.38.172.2 --bmcip 10.38.172.51 --hostpass root --board_type Mt.Jade
./xconsole.py --hostip 10.38.172.2 --hostuser root --set_nvparm [SI_DDR_VMARGIN:1130496:0xFFFFFFC4][SI_SOC_VMARGIN:1130504:0x0] --bmcip 10.38.172.51 --hostpass root --board_type Mt.Jade
./xconsole.py --cmd on --hostuser root --hostip 10.38.172.2 --bmcip 10.38.172.51 --hostpass root --board_type Mt.Jade
cksum static/test_script/test_delivery.sh
cksum static/test_script/memtester.elf
cksum static/test_script/stressapptest.elf
./xconsole.py --cmd sel_list --hostuser root --hostip 10.38.172.2 --bmcip 10.38.172.51 --hostpass root --board_type Mt.Jade
./ipmitool_sensor_chartjs.py --log logs/37/Mt.Jade_37_210426_141129/sensor-test_delivery-4.log --sensor_interval 30
./xconsole.py --cmd off --hostuser root --hostip 10.38.172.2 --bmcip 10.38.172.51 --hostpass root --board_type Mt.Jade
./xconsole.py --cmd sel_list --hostuser root --hostip 10.38.172.2 --bmcip 10.38.172.51 --hostpass root --board_type Mt.Jade
./xconsole.py --hostip 10.38.172.2 --hostuser root --set_nvparm [SI_DDR_VMARGIN:1130496:0xFFFFFFC4][SI_SOC_VMARGIN:1130504:0xFFFFFFDA] --bmcip 10.38.172.51 --hostpass root --board_type Mt.Jade
./xconsole.py --cmd on --hostuser root --hostip 10.38.172.2 --bmcip 10.38.172.51 --hostpass root --board_type Mt.Jade
cksum static/test_script/test_delivery.sh
cksum static/test_script/memtester.elf
cksum static/test_script/stressapptest.elf
