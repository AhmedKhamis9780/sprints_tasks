#!/bin/bash


#functions

error_check (){
	if [ $? == 0 ]; then
		echo "The text file is created with name $1"
	else
		echo "error in creating file $1"
	fi	
}


	

#variable

process_file="process_info.txt"
memory_file="memory_info.txt"
disk_file="disk_info.txt"
target_hostname="ahmed"
target_ip="127.0.0.1"


#creating the work directory

mkdir ~/code_testing
cd ~/code_testing

#listing process information, memory usage, current disk usage, and log file

ps aux > $process_file
error_check $process_file
free -h > $memory_file
error_check $memory_file
df -h | awk '{ if (NR==1 || NR==4) { print $0 }}' > $disk_file
error_check $disk_file
cp /var/log/dmesg dmesg_backup

#checking for created files
if [ -e $process_file ] && [ -e $memory_file ] && [ -e $disk_file ] && [ -e dmesg_backup ]; then
		echo "The files created"

		# compressing the files

		tar -cvf info.tar disk_info.txt memory_info.txt process_info.txt dmesg_backup >/dev/null
		gzip info.tar

		#sending the compressed file over the network

		scp -r info.tar.gz $target_hostname@$target_ip:~

	else
		echo "files not found"
	fi	


