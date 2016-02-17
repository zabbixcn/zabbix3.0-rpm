# zabbix3.0-rpm
#系统版本要求
本项目RPM仅用于Zabbix3.0 For CentOS 6 x64位的安装
#环境要求
PHP >= 5.4
curl >= 7.20 (如需支持SMTP认证)
```
git clone https://github.com/zabbixcn/zabbix3.0-rpm.git
cd  zabbix3.0-rpm/RPMS
```
#一 安装MySQL
#MySQL建议使用5.6版本，CentOS6默认为5.1，不建议使用，性能偏低
```
rpm -ivh http://dev.mysql.com/get/mysql-community-release-el6-5.noarch.rpm
yum install mysql-server -y  #此过程会因为网路问题偏慢，请耐心等待
vim /etc/my.cnf

[mysqld]
innodb_file_per_table

service mysqld start
mysql_secure_installation

Enter current password for root (enter for none):
Set root password? [Y/n]
Remove anonymous users? [Y/n]
Disallow root login remotely? [Y/n]
Remove test database and access to it? [Y/n]
Reload privilege tables now? [Y/n]

mysql -uroot -p
mysql> CREATE DATABASE zabbix CHARACTER SET utf8 COLLATE utf8_bin;
mysql> GRANT ALL PRIVILEGES ON zabbix.* TO zabbix@localhost IDENTIFIED BY 'zabbix';
mysql> show databases;
```
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| zabbix             |
+--------------------+
```
二、安装Apache，PHP，Zabbix-Web
Zabbix
3.0对PHP的要求最低为5.4，而CentOS6默认为5.3.3，完全不满足要求，故需要利用第三方源，将PHP升级到5.4以上，注意，不支持PHP7
```
rpm -ivh http://repo.webtatic.com/yum/el6/latest.rpm
yum install zabbix-web-mysql-3.0.0-1.el6.noarch.rpm zabbix-web-3.0.0-1.el6.noarch.rpm httpd php56w php56w-gd php56w-mysql
php56w-bcmath php56w-mbstring php56w-xml php56w-ldap

/etc/init.d/httpd restart
/etc/init.d/php restart
sed -i "s@# php_value date.timezone Europe/Riga@php_value date.timezone Asia/Shanghai@g" /etc/httpd/conf.d/zabbix.conf


cd /usr/share/zabbix-server-mysql-3.0.0
zcat create.sql.gz | mysql -uzabbix -pzabbix zabbix
```
三、安装zabbix-server
Zabbix-server就一个包，里面有server的SQL文件
```
yum  localinstall  zabbix-server-mysql-3.0.0-1.el6.x86_64.rpm
vi /etc/zabbix/zabbix_server.conf
DBHost=localhost
DBName=zabbix
DBUser=zabbix
DBPassword=zabbix

/etc/init.d/zabbix-server restart
```

四、Zabbix WEB界面配置
http://${IP}/zabbix
和之前版本一样，此处不再详解
