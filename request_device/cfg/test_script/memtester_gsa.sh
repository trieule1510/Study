#!/bin/bash
# Usage: test_delivery platform
# Author: hqbui
# -------------------------------------------------
number_test=2
testtime=$(($1 / $number_test))

stop_chronyd () {
	# Sometime timeout does not correct because of date&time is changed during 
	# running test. Stop chronyd service to make sure date/time not update.
	echo "[Info] Stop chronyd service"
	systemctl stop chronyd
}
dump_log () {
	log=$1
	echo "dump_log_start = ${log}"
	cat ${log}
	echo "dump_log_end = ${log}"
}
test_command_compare () {
	echo "test_command_compare $@"
	cmd=$@
	log="${cmd// /_}"
	log0=${log}.0.log
	log1=${log}.1.log
	
	if [ -f "${log0}" ]; then
		${cmd} > ${log1}
		if diff ${log0} ${log1}; then
			dump_log ${log0}
	    	echo "${log1} ${log0} is same"
	    	return 0
		else
			dump_log ${log1}
			dump_log ${log0}
	    	mv ${log1} ${log0}
	    	echo "${log1} ${log0} is diff"
	    	return 1
		fi
	else 
	    ${cmd} > ${log0}
	fi
	return 0
}
run_stressapptest () {
	echo "run_stressapptest"
	free_mem_str=$(free -m | grep Mem: | awk '{ print $4 }')
	test_size=$((free_mem_str*94/100-4096))	#in MB
	echo "free mem : $free_mem_str"
	echo "test size: $test_size"

	if [  "$test_size" -le 0 ]; then
		echo "Error: Invalid free mem size"
		return 1
	fi
	test_timeout=$((testtime + 600))
	timeout -k $test_timeout $test_timeout ./stressapptest.elf -s $testtime -W -M $test_size
	exit_code=$?
	return ${exit_code}
}
run_memtester () {
	result=0
	while :
	do 
		free_mem=$(free -m | grep Mem: | awk '{ print $4 }')
		t_free_mem=$((${free_mem}))
		t_m_size=0
		free_mem_cond=$((${free_mem}))
		cpu_count=`cat /proc/cpuinfo |grep processor|tail -n 1|awk '{print $3}'`
		cpu_count_test=$((cpu_count+1)) 
		m_size=$(((free_mem*90/100-1024)/${cpu_count_test}))
		start_time=${SECONDS}
		loop=0
		while [ ${t_m_size} -lt ${free_mem_cond} ]
		do
			loop=$((loop+1))
			if [ $loop -gt $cpu_count_test ]; then
				break
			else
				timeout -k ${testtime} ${testtime} ./memtester.elf "${m_size}"M > /dev/null &
				free_mem=$((${free_mem}-${m_size}))
				t_m_size=$((${m_size}+${t_m_size}))
			fi
		done
		echo " [memtest_launcher] Total Available Memory: ${t_free_mem}"
		echo " [memtest_launcher] Memtester size: ${t_m_size}"
		sleep 5
		free -m
		# wait memtest done 
		for job in `jobs -p`
		do
			wait $job
			child_status=$?
			result=$child_status
			if [ $child_status -eq 124 ]; then
				# test enough time, set result to success
				result=0
			elif [ $child_status -ne 0 ]; then
				# memtester has 3 error codes when fail: 1, 2 and 4
				echo "Memtester test fail with exit code $child_status"
				result=$child_status
				break
			fi
		done

		if [ ${result} -ne 0 ]; then
			break
		fi
		
		# if memtest done and pass, but testtime is not enough, need rerun
		duration=$((${SECONDS} - ${start_time}))
		echo  "Test elapsed: ${duration}"
		
		if [ ${duration} -gt 0 ] && [ ${duration} -lt ${testtime} ]; then
			newtime=$((${testtime} - ${duration}))
			testtime=${newtime}
			echo  "[memtest_launcher] Continue running memtester in ${testtime} seconds"
		else
			break
		fi
	done
	return ${result}
}
xdiaglinux_is_done () {
	log=$1
	grep "DIAG TEST DONE ALL" -R ${log} -a
	exit_code=$?
	return ${exit_code}
}
xdiaglinux_status () {
	log=$1
	grep "TEST FAILED ==========" -R ${log} -a
	is_fail=$?
	if [ $is_fail -eq 0 ]
	then
		return 1
	fi
	grep "TEST PASSED ==========" -R ${log} -a
	is_pass=$?
	if [ $is_pass -eq 0 ]
	then
		return 0
	fi
	return -1
}
xdiaglinux_start_test () {
	cmd=$@
	echo "xdiaglinux_start_test ${cmd}"
	xdiaglinux="./xdiaglinux"
	dir="/tmp/xdiaglinux-$(date +'%m-%d-%Y-%H-%M-%S')"
	echo "cleanup/copy xdiaglinux ${dir}"
	rm -rf ${dir}
	mkdir -p ${dir}
	cp -rf ${xdiaglinux} ${dir}/${xdiaglinux}
	cp -rf memtester ${dir}/memtester
	cd ${dir}
	echo "exec ${cmd} ${xdiaglinux} at ${dir}"
	echo "${cmd}" | ${xdiaglinux} &
	sleep 5
	log=${dir}/`ls xdiaglinux*log`
	echo "check status ${log}"
	while true; do
		xdiaglinux_is_done ${log}
		is_done=$?
		if [ ${is_done} -eq 0 ]
		then
			xdiaglinux_status ${log}
			is_status=$?
			kill %1
			return ${is_status}
		else
			sleep 10
			echo -n "."
		fi
		sleep 10
	done
}
for test_case in "stop_chronyd" "lspci -vvv" "test_command_compare dmidecode --type memory" \
				   "test_command_compare lspci" "run_memtester" "run_stressapptest"
do
	echo "Start test_case: ${test_case}"
	${test_case}
	exit_code=$?
	if [ $exit_code -eq 0 ]
	then
	  echo "End test_case: ${test_case} exit_code:${exit_code}"
	else
	  echo "End test_case: ${test_case} exit_code:${exit_code}"
	  exit ${exit_code}
	fi
done
exit 0