#!/bin/bash
check_error() {
if [ $? != 0 ]
then
        echo "======================未通过========================="
        exit 0
else
        echo "=====================执行成功========================="
fi
}
check_status(){
    if ! rpm -qa | grep -q "^$1"
    then
        yum install -y $1
    else
        echo "$1 already installed"
    fi
}
for i in gcc zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-deve
do
    check_status $i
done
cd /usr/local/src/
[ -f /usr/local/src/Python-3.6.4.tgz ] || wget https://www.python.org/ftp/python/3.6.4/Python-3.6.4.tgz
[ -d "/usr/local/python3" ] && mv /usr/local/python3 /usr/local/python3_`date +%s`
[ -d "/usr/local/Python-3.6.4" ] && rm -rf /usr/local/Python-3.6.4
tar xzvf Python-3.6.4.tgz -C /usr/local/
cd /usr/local/Python-3.6.4 && ./configure --prefix=/usr/local/python3 && make && make install
check_error
#ln -s /usr/local/python3/bin/python3 /usr/bin/python3
export PATH=$PATH:/usr/local/python3/bin
check_error
source ~/.bashrc
check_error
