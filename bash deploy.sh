#!/bin/bash
#this code runs in ubuntu os
#the code downloads the project files from git 

install_nodejs(){
    echo "nodejs install started"
    sudo apt -y install curl
    echo "installing node.js"
	curl -sL https://deb.nodesource.com/setup_14.x | sudo bash -
    sudo apt -y install nodejs
    node  -v  && echo "nodejs install successfully"
    echo "---------------------------------------------------------------------------------------------------"
}
ip_config(){
    #this function take the ip that the host already have and make it the static ip
    echo "network configration"
    dev_name=$(nmcli device show | head -n 9| grep 'GENERAL.CONNECTION:'|sed "s/^GENERAL\.CONNECTION: *//g")
    ip_add=$(nmcli device show | head -n 15| grep 'IP4.ADDRESS'|awk '{print $2}')
    #the variable 'ip_add' have the ip and subnet mask
    gateway=$(nmcli device show | head -n 15| grep 'IP4.GATEWAY'|awk '{print $2}')
    sudo nmcli connection modify "$dev_name"  ipv4.method manual ipv4.addresses "$ip_add" ipv4.gateway "$gateway" ipv4.dns 1.1.1.1
    sudo nmcli connection down "$dev_name"
    sudo nmcli connection up "$dev_name"
    echo "network configrated sucessfully"
    echo "---------------------------------------------------------------------------------------------------"
    #this code to get the ip only
    ip_add=$(echo "$ip_add" |awk -F '/' '{print $1}')
}
db_setup(){
    echo "database configration"
    sudo apt install postgresql postgresql-contrib
    sudo systemctl start postgresql.service
    sudo -u postgres psql -c "CREATE USER $db_name WITH PASSWORD '$db_passwd';"
    sudo -u postgres psql -c "CREATE DATABASE $db_name;"
    sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE $db_name TO $db_name;"
    sudo -u postgres psql $db_name -c "ALTER SYSTEM SET listen_addresses = '0.0.0.0';"
    sudo -u postgres psql $db_name -c "ALTER SYSTEM SET port = 5432;"
    sudo -u postgres psql $db_name -c "SELECT pg_reload_conf();"
    sudo bash -c "echo 'host    $db_name     $db_name     0.0.0.0/0    md5' >> /etc/postgresql/12/main/pg_hba.conf"
    sudo systemctl restart postgresql.service
    echo "database configrated sucessfully"
    echo "---------------------------------------------------------------------------------------------------"
}
ui_build_config(){
    echo "ui build"
    npm install && npm run build && echo "ui build sucessfully"
    echo "---------------------------------------------------------------------------------------------------"
}
api_build(){
    echo "api build"
    sed -i "s|localhost|$ip_add|g" webpack.config.js 
    sed -i "s|bhargavbachina|$db_name|g" webpack.config.js
    sed -i "s|''|$db_passwd|g" webpack.config.js
    npm install && ENVIRONMENT=test npm run build && echo "api build sucessfully"
    echo "---------------------------------------------------------------------------------------------------"
}


#database username and passward
db_name='deploy_db'
db_passwd=123456



sudo apt update
sudo apt install git
#download the project files from git
git clone https://github.com/omarmohsen/pern-stack-example.git
#change to the project files
cd pern-stack-example
#installing node.js
install_nodejs
#ip configration
ip_config
#database setup
db_setup
#change to ui directory and build
cd ui
ui_build_config
#change to api directory and build
cd ../api
api_build
#change to the main project files directory and collect files to deploy
cd ..
#download require dependenes
npm install pg
cp -r api/dist/* .
cp api/swagger.css .
echo 'http//'$ip_add':3080'
#start the wed server
node api.bundle.js