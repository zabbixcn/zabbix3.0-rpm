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
su - admin
#切换到admin运行以下命令
#echo "% _topdir  /home/admin/rpmbuild" >~/.rpmmacros  
#rpm -ivh zabbix-3.0.0-1.el7.src.rpm
#cd rpmbuild/SPECS
#wget https://raw.githubusercontent.com/zabbixcn/zabbix3.0-rpm/master/SPECS/zabbix.spec
#rpmbuild -ba zabbix-3.0.0.spec
#Wrote: /home/admin/rpmbuild/SRPMS/zabbix-3.0.0-1.el6.src.rpm
#Wrote: /home/admin/rpmbuild/RPMS/x86_64/zabbix-agent-3.0.0-1.el6.x86_64.rpm
#Wrote: /home/admin/rpmbuild/RPMS/x86_64/zabbix-get-3.0.0-1.el6.x86_64.rpm
#Wrote: /home/admin/rpmbuild/RPMS/x86_64/zabbix-sender-3.0.0-1.el6.x86_64.rpm
#Wrote: /home/admin/rpmbuild/RPMS/x86_64/zabbix-server-mysql-3.0.0-1.el6.x86_64.rpm
#Wrote: /home/admin/rpmbuild/RPMS/x86_64/zabbix-server-pgsql-3.0.0-1.el6.x86_64.rpm
#Wrote: /home/admin/rpmbuild/RPMS/x86_64/zabbix-proxy-mysql-3.0.0-1.el6.x86_64.rpm
#Wrote: /home/admin/rpmbuild/RPMS/x86_64/zabbix-proxy-pgsql-3.0.0-1.el6.x86_64.rpm
#Wrote: /home/admin/rpmbuild/RPMS/x86_64/zabbix-proxy-sqlite3-3.0.0-1.el6.x86_64.rpm
#Wrote: /home/admin/rpmbuild/RPMS/x86_64/zabbix-java-gateway-3.0.0-1.el6.x86_64.rpm
#Wrote: /home/admin/rpmbuild/RPMS/noarch/zabbix-web-3.0.0-1.el6.noarch.rpm
#Wrote: /home/admin/rpmbuild/RPMS/noarch/zabbix-web-mysql-3.0.0-1.el6.noarch.rpm
#Wrote: /home/admin/rpmbuild/RPMS/noarch/zabbix-web-pgsql-3.0.0-1.el6.noarch.rpm
#Wrote: /home/admin/rpmbuild/RPMS/noarch/zabbix-web-japanese-3.0.0-1.el6.noarch.rpm
