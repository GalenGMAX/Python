yum install gcc
cd /usr/src
wget https://www.python.org/ftp/python/2.7.13/Python-2.7.13.tgz
tar xzf Python-2.7.13.tgz
cd Python-2.7.13

yum install zlib
yum install zlib-devel
yum install openssl-devel

./configure
#./configure --enable-shared
make
make install

mv /usr/bin/python /usr/bin/python23
cp ./python /usr/bin/python

vi /usr/bin/yum
#change the first line to use python23 instead

curl -O https://bootstrap.pypa.io/get-pip.py
python get-pip.py
pip install MySQL-python

#32-bit system
ln -s /usr/local/mysql/lib/libmysqlclient.so.18 /usr/lib/libmysqlclient.so.18
#64-bit system
ln -s /usr/local/mysql/lib/libmysqlclient.so.18 /usr/lib64/libmysqlclient.so.18