yum install -y git rpm-build gcc make mysql-devel openldap-devel libssh2-devel net-snmp-devel curl-devel unixODBC-devel OpenIPMI-devel java-devel postgresql-devel gnutls-devel sqlite-devel libxml2-devel
git clone  https://github.com/zabbixcn/curl-rpm.git
cd curl-rpm/RPMS
rpm -Uvh curl-7.29.0-25.el6.x86_64.rpm libcurl-7.29.0-25.el6.x86_64.rpm libcurl-devel-7.29.0-25.el6.x86_64.rpm
rpm -ivh http://repo.zabbix.com/non-supported/rhel/6/x86_64/iksemel-1.4-2.el6.x86_64.rpm
rpm -ivh http://repo.zabbix.com/non-supported/rhel/6/x86_64/iksemel-devel-1.4-2.el6.x86_64.rpm
rpm -ivh http://repo.zabbix.com/non-supported/rhel/6/x86_64/iksemel-utils-1.4-2.el6.x86_64.rpm
wget http://repo.zabbix.com/zabbix/3.0/rhel/7/SRPMS/zabbix-3.0.0-1.el7.src.rpm
adduser admin
cp zabbix-3.0.0-1.el7.src.rpm /home/admin
