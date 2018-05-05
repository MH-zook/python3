#!/bin/bash
check_error() {
if [ $? == 0 ]
then
        echo "已通过"
        exit 0
else
        echo "未通过"
fi
}
if ! rpm -qa |grep gcc
then
        yum install -y gcc
else
        echo "gcc installed"
fi
cd /usr/local/src/
[ -f /usr/local/src/Python-3.6.4.tgz ] || wget https://www.python.org/ftp/python/3.6.4/Python-3.6.4.tgz
[ -d "/usr/local/python3" ] && rm -rf /usr/local/python3
[ -d "/usr/local/Python-3.6.4" ] && rm -rf /usr/local/Python-3.6.4
tar xzvf Python-3.6.4.tgz -C /usr/local/
[-d "/usr/local/Python-3.6.4"] && /
ln -s /usr/local/Python-3.6.4 /usr/local/python3
cd /usr/local/python3 && ./configure && make && make install
ln -s /usr/local/python3/bin/python3 /usr/bin/python3
export PATH=$PATH:/usr/local/python3/bin
source ~/.bashrc
check_error
