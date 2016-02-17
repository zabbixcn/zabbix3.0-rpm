Name:		zabbix
Version:	3.0.0
Release: 	1%{?alphatag:.%{alphatag}}%{?dist}
Summary:	The Enterprise-class open source monitoring solution
Group:		Applications/Internet
License:	GPLv2+
URL:		http://www.zabbix.com/
Source0:	zabbix-%{version}%{?alphatag:%{alphatag}}.tar.gz
Source1:	zabbix-web22.conf
Source2:	zabbix-web24.conf
Source3:	zabbix-logrotate.in
Source4:	zabbix-java-gateway.init
Source5:	zabbix-agent.init
Source6:	zabbix-server.init
Source7:	zabbix-proxy.init
Source10:	zabbix-agent.service
Source11:	zabbix-server.service
Source12:	zabbix-proxy.service
Source13:	zabbix-java-gateway.service
Source14:	zabbix_java_gateway-sysd
Source15:	zabbix-tmpfiles.conf
Patch0:		config.patch
Patch1:		fonts-config.patch
Patch2:		fping3-sourceip-option.patch

Buildroot:	%{_tmppath}/zabbix-%{version}-%{release}-root-%(%{__id_u} -n)

%define build_server 0%{!?_only_agent:1}
%if 0%{?_only_agent:1}
%define _unpackaged_files_terminate_build 0
%define _missing_doc_files_terminate_build 0
%endif

%if %{build_server}
BuildRequires:	mysql-devel
BuildRequires:	postgresql-devel
BuildRequires:	net-snmp-devel
BuildRequires:	openldap-devel
BuildRequires:	gnutls-devel
BuildRequires:	iksemel-devel
BuildRequires:	sqlite-devel
BuildRequires:	unixODBC-devel
BuildRequires:	curl-devel >= 7.13.1
BuildRequires:	OpenIPMI-devel >= 2
BuildRequires:	libssh2-devel >= 1.0.0
BuildRequires:	java-devel >= 1.6.0
BuildRequires:	libxml2-devel
%if 0%{?rhel} >= 7
BuildRequires:	systemd
%endif
%endif

%description
Zabbix is the ultimate enterprise-level software designed for
real-time monitoring of millions of metrics collected from tens of
thousands of servers, virtual machines and network devices.

%package agent
Summary:			Zabbix Agent
Group:				Applications/Internet
Requires:			logrotate
Requires(pre):		/usr/sbin/useradd
%if 0%{?rhel} >= 7
Requires(post):		systemd
Requires(preun):	systemd
Requires(preun):	systemd
%else
Requires(post):		/sbin/chkconfig
Requires(preun):	/sbin/chkconfig
Requires(preun):	/sbin/service
Requires(postun):	/sbin/service
%endif
Obsoletes:			zabbix

%description agent
Zabbix agent to be installed on monitored systems.

%package get
Summary:			Zabbix Get
Group:				Applications/Internet

%description get
Zabbix get command line utility

%package sender
Summary:			Zabbix Sender
Group:				Applications/Internet

%description sender
Zabbix sender command line utility

%if %{build_server}
%package server-mysql
Summary:			Zabbix server for MySQL or MariaDB database
Group:				Applications/Internet
Requires:			fping
%if 0%{?rhel} >= 7
Requires(post):		systemd
Requires(preun):	systemd
Requires(postun):	systemd
%else
Requires(post):		/sbin/chkconfig
Requires(preun):	/sbin/chkconfig
Requires(preun):	/sbin/service
Requires(postun):	/sbin/service
%endif
Provides:			zabbix-server = %{version}-%{release}
Provides:			zabbix-server-implementation = %{version}-%{release}
Obsoletes:			zabbix
Obsoletes:			zabbix-server

%description server-mysql
Zabbix server with MySQL or MariaDB database support.

%package server-pgsql
Summary:			Zabbix server for PostgresSQL database
Group:				Applications/Internet
Requires:			fping
%if 0%{?rhel} >= 7
Requires(post):		systemd
Requires(preun):	systemd
Requires(postun):	systemd
%else
Requires(post):		/sbin/chkconfig
Requires(preun):	/sbin/chkconfig
Requires(preun):	/sbin/service
Requires(postun):	/sbin/service
%endif
Provides:			zabbix-server = %{version}-%{release}
Provides:			zabbix-server-implementation = %{version}-%{release}
Obsoletes:			zabbix
Obsoletes:			zabbix-server
%description server-pgsql
Zabbix server with PostgresSQL database support.

%package proxy-mysql
Summary:			Zabbix proxy for MySQL or MariaDB database
Group:				Applications/Internet
Requires:			fping
%if 0%{?rhel} >= 7
Requires(post):		systemd
Requires(preun):	systemd
Requires(postun):	systemd
%else
Requires(post):		/sbin/chkconfig
Requires(preun):	/sbin/chkconfig
Requires(preun):	/sbin/service
Requires(postun):	/sbin/service
%endif
Provides:			zabbix-proxy = %{version}-%{release}
Provides:			zabbix-proxy-implementation = %{version}-%{release}
Obsoletes:			zabbix
Obsoletes:			zabbix-proxy

%description proxy-mysql
Zabbix proxy with MySQL or MariaDB database support.

%package proxy-pgsql
Summary:			Zabbix proxy for PostgreSQL database
Group:				Applications/Internet
Requires:			fping
%if 0%{?rhel} >= 7
Requires(post):		systemd
Requires(preun):	systemd
Requires(postun):	systemd
%else
Requires(post):		/sbin/chkconfig
Requires(preun):	/sbin/chkconfig
Requires(preun):	/sbin/service
Requires(postun):	/sbin/service
%endif
Provides:			zabbix-proxy = %{version}-%{release}
Provides:			zabbix-proxy-implementation = %{version}-%{release}
Obsoletes:			zabbix
Obsoletes:			zabbix-proxy

%description proxy-pgsql
Zabbix proxy with PostgreSQL database support.

%package proxy-sqlite3
Summary:			Zabbix proxy for SQLite3 database
Group:				Applications/Internet
Requires:			fping
%if 0%{?rhel} >= 7
Requires(post):		systemd
Requires(preun):	systemd
Requires(postun):	systemd
%else
Requires(post):		/sbin/chkconfig
Requires(preun):	/sbin/chkconfig
Requires(preun):	/sbin/service
Requires(postun):	/sbin/service
%endif
Provides:			zabbix-proxy = %{version}-%{release}
Provides:			zabbix-proxy-implementation = %{version}-%{release}
Obsoletes:			zabbix
Obsoletes:			zabbix-proxy

%description proxy-sqlite3
Zabbix proxy with SQLite3 database support.

%package java-gateway
Summary:			Zabbix java gateway
Group:				Applications/Internet
%if 0%{?rhel} >= 7
Requires:			java-headless >= 1.6.0
%else
Requires:			java >= 1.6.0
%endif
%if 0%{?rhel} >= 7
Requires(post):		systemd
Requires(preun):	systemd
Requires(postun):	systemd
%else
Requires(post):		/sbin/chkconfig
Requires(preun):	/sbin/chkconfig
Requires(preun):	/sbin/service
Requires(postun):	/sbin/service
%endif
Obsoletes:			zabbix

%description java-gateway
Zabbix java gateway

%package web
Summary:			Zabbix web frontend common package
Group:				Application/Internet
BuildArch:			noarch
Requires:			httpd
Requires:			php >= 5.4
Requires:			php-gd
Requires:			php-bcmath
Requires:			php-mbstring
Requires:			php-xml
Requires:			php-ldap
Requires:			dejavu-sans-fonts
Requires:			zabbix-web-database = %{version}-%{release}
Requires(post):		%{_sbindir}/update-alternatives
Requires(preun):	%{_sbindir}/update-alternatives

%description web
Zabbix web frontend common package

%package web-mysql
Summary:			Zabbix web frontend for MySQL
Group:				Applications/Internet
BuildArch:			noarch
Requires:			php-mysql
Requires:			zabbix-web = %{version}-%{release}
Provides:			zabbix-web-database = %{version}-%{release}

%description web-mysql
Zabbix web frontend for MySQL

%package web-pgsql
Summary:			Zabbix web frontend for PostgreSQL
Group:				Applications/Internet
BuildArch:			noarch
Requires:			php-pgsql
Requires:			zabbix-web = %{version}-%{release}
Provides:			zabbix-web-database = %{version}-%{release}

%description web-pgsql
Zabbix web frontend for PostgreSQL

%package web-japanese
Summary:			Japanese font settings for frontend
Group:				Applications/Internet
BuildArch:			noarch
Requires:			vlgothic-p-fonts
Requires:			zabbix-web = %{version}-%{release}
Requires(post):		%{_sbindir}/update-alternatives
Requires(preun):	%{_sbindir}/update-alternatives

%description web-japanese
Japanese font configuration for Zabbix web frontend
%endif

%prep
%setup0 -q -n zabbix-%{version}%{?alphatag:%{alphatag}}
%patch0 -p1
%patch1 -p1
%if 0%{?rhel} >= 7
%patch2 -p1
%endif

## remove font file
rm -f frontends/php/fonts/DejaVuSans.ttf

# remove .htaccess files
rm -f frontends/php/app/.htaccess
rm -f frontends/php/conf/.htaccess
rm -f frontends/php/include/.htaccess
rm -f frontends/php/local/.htaccess

# remove translation source files and scripts
find frontend/php/locale -name '*.po' | xargs rm -f
find frontend/php/locale -name '*.sh' | xargs rm -f

# traceroute command path for global script
sed -i -e 's|/usr/bin/traceroute|/bin/traceroute|' database/mysql/data.sql
sed -i -e 's|/usr/bin/traceroute|/bin/traceroute|' database/postgresql/data.sql
sed -i -e 's|/usr/bin/traceroute|/bin/traceroute|' database/sqlite3/data.sql

# change log directory for Java Gateway
sed -i -e 's|/tmp/zabbix_java.log|/var/log/zabbix/zabbix_java_gateway.log|g' src/zabbix_java/lib/logback.xml


%build

%if %{build_server}
build_flags="
	--enable-dependency-tracking
	--sysconfdir=/etc/zabbix
	--libdir=%{_libdir}/zabbix
	--enable-agent
	--enable-server
	--enable-proxy
	--enable-ipv6
	--enable-java
	--with-net-snmp
	--with-ldap
	--with-libcurl
	--with-openipmi
	--with-jabber
	--with-unixodbc
	--with-ssh2
	--with-libxml2
	--with-openssl
"

%configure $build_flags --with-mysql
make %{?_smp_mflags}
mv src/zabbix_server/zabbix_server src/zabbix_server/zabbix_server_mysql
mv src/zabbix_proxy/zabbix_proxy src/zabbix_proxy/zabbix_proxy_mysql

%configure $build_flags --with-postgresql
make %{?_smp_mflags}
mv src/zabbix_server/zabbix_server src/zabbix_server/zabbix_server_pgsql
mv src/zabbix_proxy/zabbix_proxy src/zabbix_proxy/zabbix_proxy_pgsql

%configure $build_flags --with-sqlite3
make %{?_smp_mflags}
mv src/zabbix_server/zabbix_server src/zabbix_server/zabbix_server_sqlite3
mv src/zabbix_proxy/zabbix_proxy src/zabbix_proxy/zabbix_proxy_sqlite3

touch src/zabbix_server/zabbix_server
touch src/zabbix_proxy/zabbix_proxy

%else
%configure \
	--enable-dependency-tracking \
	--sysconfdir=/etc/zabbix \
	--enable-agent \
	--enable-ipv6 \
	--with-openssl
make %{?_smp_mflags}
%endif


%install

rm -rf $RPM_BUILD_ROOT

# install
make DESTDIR=$RPM_BUILD_ROOT install

# install necessary directories
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/log/zabbix
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/run/zabbix

# install server and proxy binaries
%if %{build_server}
rm src/zabbix_server/zabbix_server_sqlite3
install -m 0755 -p src/zabbix_server/zabbix_server_* $RPM_BUILD_ROOT%{_sbindir}/
install -m 0755 -p src/zabbix_proxy/zabbix_proxy_* $RPM_BUILD_ROOT%{_sbindir}/
rm $RPM_BUILD_ROOT%{_sbindir}/zabbix_server
rm $RPM_BUILD_ROOT%{_sbindir}/zabbix_proxy

# delete unnecessary files from java gateway
rm $RPM_BUILD_ROOT%{_sbindir}/zabbix_java/settings.sh
rm $RPM_BUILD_ROOT%{_sbindir}/zabbix_java/startup.sh
rm $RPM_BUILD_ROOT%{_sbindir}/zabbix_java/shutdown.sh

# install scripts and modules directories
mkdir -p $RPM_BUILD_ROOT/usr/lib/zabbix
mv $RPM_BUILD_ROOT%{_datadir}/zabbix/alertscripts $RPM_BUILD_ROOT/usr/lib/zabbix
mv $RPM_BUILD_ROOT%{_datadir}/zabbix/externalscripts $RPM_BUILD_ROOT/usr/lib/zabbix
mkdir $RPM_BUILD_ROOT%{_libdir}/zabbix/modules

%if 0%{?rhel} >=7
mv $RPM_BUILD_ROOT%{_sbindir}/zabbix_java/lib/logback.xml $RPM_BUILD_ROOT/%{_sysconfdir}/zabbix/zabbix_java_gateway_logback.xml
rm $RPM_BUILD_ROOT%{_sbindir}/zabbix_java/lib/logback-console.xml
mv $RPM_BUILD_ROOT%{_sbindir}/zabbix_java $RPM_BUILD_ROOT/%{_datadir}/zabbix-java-gateway
install -m 0755 -p %{SOURCE14} $RPM_BUILD_ROOT%{_sbindir}/zabbix_java_gateway
%endif

# install frontend files
find frontends/php -name '*.orig' | xargs rm -f
cp -a frontends/php/* $RPM_BUILD_ROOT%{_datadir}/zabbix

# install frontend configuration files
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/zabbix/web
touch $RPM_BUILD_ROOT%{_sysconfdir}/zabbix/web/zabbix.conf.php
mv $RPM_BUILD_ROOT%{_datadir}/zabbix/conf/maintenance.inc.php $RPM_BUILD_ROOT%{_sysconfdir}/zabbix/web/

# drop config files in place
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d
%if 0%{?rhel} >= 7
install -m 0644 -p %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d/zabbix.conf
%else
install -m 0644 -p %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d/zabbix.conf
%endif
%endif

# install configuration files
mv $RPM_BUILD_ROOT%{_sysconfdir}/zabbix/zabbix_agentd.conf.d $RPM_BUILD_ROOT%{_sysconfdir}/zabbix/zabbix_agentd.d
mv $RPM_BUILD_ROOT%{_sysconfdir}/zabbix/zabbix_server.conf.d $RPM_BUILD_ROOT%{_sysconfdir}/zabbix/zabbix_server.d
mv $RPM_BUILD_ROOT%{_sysconfdir}/zabbix/zabbix_proxy.conf.d $RPM_BUILD_ROOT%{_sysconfdir}/zabbix/zabbix_proxy.d

install -dm 755 $RPM_BUILD_ROOT%{_docdir}/zabbix-agent-%{version}

install -m 0644 conf/zabbix_agentd/userparameter_mysql.conf $RPM_BUILD_ROOT%{_sysconfdir}/zabbix/zabbix_agentd.d
install -m 0644 conf/zabbix_agentd/userparameter_examples.conf $RPM_BUILD_ROOT%{_docdir}/zabbix-agent-%{version}

cat conf/zabbix_agentd.conf | sed \
	-e '/^# PidFile=/a \\nPidFile=%{_localstatedir}/run/zabbix/zabbix_agentd.pid' \
	-e 's|^LogFile=.*|LogFile=%{_localstatedir}/log/zabbix/zabbix_agentd.log|g' \
	-e '/^# LogFileSize=.*/a \\nLogFileSize=0' \
	-e '/^# Include=$/a \\nInclude=%{_sysconfdir}/zabbix/zabbix_agentd.d/' \
	> $RPM_BUILD_ROOT%{_sysconfdir}/zabbix/zabbix_agentd.conf

cat conf/zabbix_server.conf | sed \
	-e '/^# PidFile=/a \\nPidFile=%{_localstatedir}/run/zabbix/zabbix_server.pid' \
	-e 's|^LogFile=.*|LogFile=%{_localstatedir}/log/zabbix/zabbix_server.log|g' \
	-e '/^# LogFileSize=/a \\nLogFileSize=0' \
	-e '/^# AlertScriptsPath=/a \\nAlertScriptsPath=/usr/lib/zabbix/alertscripts' \
	-e '/^# ExternalScripts=/a \\nExternalScripts=/usr/lib/zabbix/externalscripts' \
	-e 's|^DBUser=root|DBUser=zabbix|g' \
	-e '/^# DBSocket=/a \\nDBSocket=%{_localstatedir}/lib/mysql/mysql.sock' \
	-e '/^# SNMPTrapperFile=.*/a \\nSNMPTrapperFile=/var/log/snmptrap/snmptrap.log' \
	> $RPM_BUILD_ROOT%{_sysconfdir}/zabbix/zabbix_server.conf

cat conf/zabbix_proxy.conf | sed \
	-e '/^# PidFile=/a \\nPidFile=%{_localstatedir}/run/zabbix/zabbix_proxy.pid' \
	-e 's|^LogFile=.*|LogFile=%{_localstatedir}/log/zabbix/zabbix_proxy.log|g' \
	-e '/^# LogFileSize=/a \\nLogFileSize=0' \
	-e '/^# ExternalScripts=/a \\nExternalScripts=/usr/lib/zabbix/externalscripts' \
	-e 's|^DBUser=root|DBUser=zabbix|g' \
	-e '/^# DBSocket=/a \\nDBSocket=%{_localstatedir}/lib/mysql/mysql.sock' \
	-e '/^# SNMPTrapperFile=.*/a \\nSNMPTrapperFile=/var/log/snmptrap/snmptrap.log' \
	> $RPM_BUILD_ROOT%{_sysconfdir}/zabbix/zabbix_proxy.conf

cat src/zabbix_java/settings.sh | sed \
	-e 's|^PID_FILE=.*|PID_FILE="/var/run/zabbix/zabbix_java.pid"|g' \
	-e '/^# TIMEOUT=/a \\nTIMEOUT=3' \
	> $RPM_BUILD_ROOT%{_sysconfdir}/zabbix/zabbix_java_gateway.conf

# install logrotate configuration files
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d
cat %{SOURCE3} | sed \
	-e 's|COMPONENT|server|g' \
	> $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/zabbix-server
cat %{SOURCE3} | sed \
	-e 's|COMPONENT|agentd|g' \
	> $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/zabbix-agent
cat %{SOURCE3} | sed \
	-e 's|COMPONENT|proxy|g' \
	> $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/zabbix-proxy

# install startup scripts
%if 0%{?rhel} >= 7
install -Dm 0644 -p %{SOURCE10} $RPM_BUILD_ROOT%{_unitdir}/zabbix-agent.service
install -Dm 0644 -p %{SOURCE11} $RPM_BUILD_ROOT%{_unitdir}/zabbix-server.service
install -Dm 0644 -p %{SOURCE12} $RPM_BUILD_ROOT%{_unitdir}/zabbix-proxy.service
install -Dm 0644 -p %{SOURCE13} $RPM_BUILD_ROOT%{_unitdir}/zabbix-java-gateway.service
%else
install -Dm 0755 -p %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/init.d/zabbix-java-gateway
install -Dm 0755 -p %{SOURCE5} $RPM_BUILD_ROOT%{_sysconfdir}/init.d/zabbix-agent
install -Dm 0755 -p %{SOURCE6} $RPM_BUILD_ROOT%{_sysconfdir}/init.d/zabbix-server
install -Dm 0755 -p %{SOURCE7} $RPM_BUILD_ROOT%{_sysconfdir}/init.d/zabbix-proxy
%endif

# install systemd-tmpfiles conf
%if 0%{?rhel} >= 7
install -Dm 0644 -p %{SOURCE15} $RPM_BUILD_ROOT%{_prefix}/lib/tmpfiles.d/zabbix-agent.conf
install -Dm 0644 -p %{SOURCE15} $RPM_BUILD_ROOT%{_prefix}/lib/tmpfiles.d/zabbix-server.conf
install -Dm 0644 -p %{SOURCE15} $RPM_BUILD_ROOT%{_prefix}/lib/tmpfiles.d/zabbix-proxy.conf
install -Dm 0644 -p %{SOURCE15} $RPM_BUILD_ROOT%{_prefix}/lib/tmpfiles.d/zabbix-java-gateway.conf
%endif

%if %{build_server}
# copy sql files for servers
docdir=$RPM_BUILD_ROOT%{_docdir}/zabbix-server-mysql-%{version}
install -dm 755 $docdir
cat database/mysql/schema.sql > $docdir/create.sql
cat database/mysql/images.sql >> $docdir/create.sql
cat database/mysql/data.sql >> $docdir/create.sql
gzip $docdir/create.sql

docdir=$RPM_BUILD_ROOT%{_docdir}/zabbix-server-pgsql-%{version}
install -dm 755 $docdir
cat database/postgresql/schema.sql > $docdir/create.sql
cat database/postgresql/images.sql >> $docdir/create.sql
cat database/postgresql/data.sql >> $docdir/create.sql
gzip $docdir/create.sql

# copy sql files for proxyes
docdir=$RPM_BUILD_ROOT%{_docdir}/zabbix-proxy-mysql-%{version}
install -dm 755 $docdir
cp database/mysql/schema.sql $docdir/schema.sql
gzip $docdir/schema.sql

docdir=$RPM_BUILD_ROOT%{_docdir}/zabbix-proxy-pgsql-%{version}
install -dm 755 $docdir
cp database/postgresql/schema.sql $docdir/schema.sql
gzip $docdir/schema.sql

docdir=$RPM_BUILD_ROOT%{_docdir}/zabbix-proxy-sqlite3-%{version}
install -dm 755 $docdir
cp database/sqlite3/schema.sql $docdir/schema.sql
gzip $docdir/schema.sql
%endif


%clean
rm -rf $RPM_BUILD_ROOT


%pre agent
getent group zabbix > /dev/null || groupadd -r zabbix
getent passwd zabbix > /dev/null || \
	useradd -r -g zabbix -d %{_localstatedir}/lib/zabbix -s /sbin/nologin \
	-c "Zabbix Monitoring System" zabbix
:

%post agent
%if 0%{?rhel} >= 7
%systemd_post zabbix-agent.service
%else
/sbin/chkconfig --add zabbix-agent || :
%endif

%if %{build_server}
%pre server-mysql
getent group zabbix > /dev/null || groupadd -r zabbix
getent passwd zabbix > /dev/null || \
	useradd -r -g zabbix -d %{_localstatedir}/lib/zabbix -s /sbin/nologin \
	-c "Zabbix Monitoring System" zabbix
:

%pre server-pgsql
getent group zabbix > /dev/null || groupadd -r zabbix
getent passwd zabbix > /dev/null || \
	useradd -r -g zabbix -d %{_localstatedir}/lib/zabbix -s /sbin/nologin \
	-c "Zabbix Monitoring System" zabbix
:

%pre proxy-mysql
getent group zabbix > /dev/null || groupadd -r zabbix
getent passwd zabbix > /dev/null || \
	useradd -r -g zabbix -d %{_localstatedir}/lib/zabbix -s /sbin/nologin \
	-c "Zabbix Monitoring System" zabbix
:

%pre proxy-pgsql
getent group zabbix > /dev/null || groupadd -r zabbix
getent passwd zabbix > /dev/null || \
	useradd -r -g zabbix -d %{_localstatedir}/lib/zabbix -s /sbin/nologin \
	-c "Zabbix Monitoring System" zabbix
:

%pre proxy-sqlite3
getent group zabbix > /dev/null || groupadd -r zabbix
getent passwd zabbix > /dev/null || \
	useradd -r -g zabbix -d %{_localstatedir}/lib/zabbix -s /sbin/nologin \
	-c "Zabbix Monitoring System" zabbix
:

%pre java-gateway
getent group zabbix > /dev/null || groupadd -r zabbix
getent passwd zabbix > /dev/null || \
	useradd -r -g zabbix -d %{_localstatedir}/lib/zabbix -s /sbin/nologin \
	-c "Zabbix Monitoring System" zabbix
:

%post server-mysql
%if 0%{?rhel} >= 7
%systemd_post zabbix-server.service
%else
/sbin/chkconfig --add zabbix-server
%endif
/usr/sbin/update-alternatives --install %{_sbindir}/zabbix_server \
	zabbix-server %{_sbindir}/zabbix_server_mysql 10
:

%post server-pgsql
%if 0%{?rhel} >= 7
%systemd_post zabbix-server.service
%else
/sbin/chkconfig --add zabbix-server
%endif
/usr/sbin/update-alternatives --install %{_sbindir}/zabbix_server \
	zabbix-server %{_sbindir}/zabbix_server_pgsql 10
:

%post proxy-mysql
%if 0%{?rhel} >= 7
%systemd_post zabbix-proxy.service
%else
/sbin/chkconfig --add zabbix-proxy
%endif
/usr/sbin/update-alternatives --install %{_sbindir}/zabbix_proxy \
	zabbix-proxy %{_sbindir}/zabbix_proxy_mysql 10
:

%post proxy-pgsql
%if 0%{?rhel} >= 7
%systemd_post zabbix-proxy.service
%else
/sbin/chkconfig --add zabbix-proxy
%endif
/usr/sbin/update-alternatives --install %{_sbindir}/zabbix_proxy \
	zabbix-proxy %{_sbindir}/zabbix_proxy_pgsql 10
:

%post proxy-sqlite3
%if 0%{?rhel} >= 7
%systemd_post zabbix-proxy.service
%else
/sbin/chkconfig --add zabbix-proxy
%endif
/usr/sbin/update-alternatives --install %{_sbindir}/zabbix_proxy \
	zabbix-proxy %{_sbindir}/zabbix_proxy_sqlite3 10
:

%post java-gateway
%if 0%{?rhel} >= 7
%systemd_post zabbix-java-gateway.service
%else
/sbin/chkconfig --add zabbix-java-gateway
%endif
:

%post web
/usr/sbin/update-alternatives --install %{_datadir}/zabbix/fonts/graphfont.ttf \
	zabbix-web-font %{_datadir}/fonts/dejavu/DejaVuSans.ttf 10
:

%post web-japanese
/usr/sbin/update-alternatives --install %{_datadir}/zabbix/fonts/graphfont.ttf \
	zabbix-web-font %{_datadir}/fonts/vlgothic/VL-PGothic-Regular.ttf 20
:
%endif

%preun agent
if [ "$1" = 0 ]; then
%if 0%{?rhel} >= 7
%systemd_preun zabbix-agent.service
%else
/sbin/service zabbix-agent stop >/dev/null 2>&1
/sbin/chkconfig --del zabbix-agent
%endif
fi
:

%if %{build_server}
%preun server-mysql
if [ "$1" = 0 ]; then
%if 0%{?rhel} >= 7
%systemd_preun zabbix-server.service
%else
/sbin/service zabbix-server stop >/dev/null 2>&1
/sbin/chkconfig --del zabbix-server
%endif
/usr/sbin/update-alternatives --remove zabbix-server \
	%{_sbindir}/zabbix_server_mysql
fi
:

%preun server-pgsql
if [ "$1" = 0 ]; then
%if 0%{?rhel} >= 7
%systemd_preun zabbix-server.service
%else
/sbin/service zabbix-server stop >/dev/null 2>&1
/sbin/chkconfig --del zabbix-server
%endif
/usr/sbin/update-alternatives --remove zabbix-server \
	%{_sbindir}/zabbix_server_pgsql
fi
:

%preun proxy-mysql
if [ "$1" = 0 ]; then
%if 0%{?rhel} >= 7
%systemd_preun zabbix-proxy.service
%else
/sbin/service zabbix-proxy stop >/dev/null 2>&1
/sbin/chkconfig --del zabbix-proxy
%endif
/usr/sbin/update-alternatives --remove zabbix-proxy \
%{_sbindir}/zabbix_proxy_mysql
fi
:

%preun proxy-pgsql
if [ "$1" = 0 ]; then
%if 0%{?rhel} >= 7
%systemd_preun zabbix-proxy.service
%else
/sbin/service zabbix-proxy stop >/dev/null 2>&1
/sbin/chkconfig --del zabbix-proxy
%endif
/usr/sbin/update-alternatives --remove zabbix-proxy \
	%{_sbindir}/zabbix_proxy_pgsql
fi
:

%preun proxy-sqlite3
if [ "$1" = 0 ]; then
%if 0%{?rhel} >= 7
%systemd_preun zabbix-proxy.service
%else
/sbin/service zabbix-proxy stop >/dev/null 2>&1
/sbin/chkconfig --del zabbix-proxy
%endif
/usr/sbin/update-alternatives --remove zabbix-proxy \
	%{_sbindir}/zabbix_proxy_sqlite3
fi
:

%preun java-gateway
if [ $1 -eq 0 ]; then
%if 0%{?rhel} >= 7
%systemd_preun zabbix-java-gateway.service
%else
/sbin/service zabbix-java-gateway stop >/dev/null 2>&1
/sbin/chkconfig --del zabbix-java-gateway
%endif
fi
:

%preun web
if [ "$1" = 0 ]; then
/usr/sbin/update-alternatives --remove zabbix-web-font \
	%{_datadir}/fonts/dejavu/DejaVuSans.ttf
fi
:

%preun web-japanese
if [ "$1" = 0 ]; then
/usr/sbin/update-alternatives --remove zabbix-web-font \
	%{_datadir}/fonts/vlgothic/VL-PGothic-Regular.ttf
fi
:
%endif

%postun agent
%if 0%{?rhel} >= 7
%systemd_postun_with_restart zabbix-agent.service
%else
if [ $1 -ge 1 ]; then
/sbin/service zabbix-agent try-restart >/dev/null 2>&1 || :
fi
%endif

%if %{build_server}
%postun server-mysql
%if 0%{?rhel} >= 7
%systemd_postun_with_restart zabbix-server.service
%else
if [ $1 -ge 1 ]; then
/sbin/service zabbix-server try-restart >/dev/null 2>&1 || :
fi
%endif

%postun server-pgsql
%if 0%{?rhel} >= 7
%systemd_postun_with_restart zabbix-server.service
%else
if [ $1 -ge 1 ]; then
/sbin/service zabbix-server try-restart >/dev/null 2>&1 || :
fi
%endif

%postun proxy-mysql
%if 0%{?rhel} >= 7
%systemd_postun_with_restart zabbix-proxy.service
%else
if [ $1 -ge 1 ]; then
/sbin/service zabbix-proxy try-restart >/dev/null 2>&1 || :
fi
%endif

%postun proxy-pgsql
%if 0%{?rhel} >= 7
%systemd_postun_with_restart zabbix-proxy.service
%else
if [ $1 -ge 1 ]; then
/sbin/service zabbix-proxy try-restart >/dev/null 2>&1 || :
fi
%endif

%postun proxy-sqlite3
%if 0%{?rhel} >= 7
%systemd_postun_with_restart zabbix-proxy.service
%else
if [ $1 -ge 1 ]; then
/sbin/service zabbix-proxy try-restart >/dev/null 2>&1 || :
fi
%endif

%postun java-gateway
%if 0%{?rhel} >= 7
%systemd_postun_with_restart zabbix-java-gateway.service
%else
if [ $1 -gt 1 ]; then
/sbin/service zabbix-java-gateway condrestart >/dev/null 2>&1 || :
fi
%endif
%endif

%files agent
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_docdir}/zabbix-agent-%{version}/
%config(noreplace) %{_sysconfdir}/zabbix/zabbix_agentd.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/zabbix-agent
%dir %{_sysconfdir}/zabbix/zabbix_agentd.d
%config(noreplace) %{_sysconfdir}/zabbix/zabbix_agentd.d/userparameter_mysql.conf
%attr(0755,zabbix,zabbix) %dir %{_localstatedir}/log/zabbix
%attr(0755,zabbix,zabbix) %dir %{_localstatedir}/run/zabbix
%{_sbindir}/zabbix_agentd
%{_mandir}/man8/zabbix_agentd.8*
%if 0%{?rhel} >= 7
%{_unitdir}/zabbix-agent.service
%{_prefix}/lib/tmpfiles.d/zabbix-agent.conf
%else
%{_sysconfdir}/init.d/zabbix-agent
%endif


%files get
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_bindir}/zabbix_get
%{_mandir}/man1/zabbix_get.1*

%files sender
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_bindir}/zabbix_sender
%{_mandir}/man1/zabbix_sender.1*

%if %{build_server}
%files server-mysql
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_docdir}/zabbix-server-mysql-%{version}/
%attr(0640,root,zabbix) %config(noreplace) %{_sysconfdir}/zabbix/zabbix_server.conf
%dir /usr/lib/zabbix/alertscripts
%dir /usr/lib/zabbix/externalscripts
%config(noreplace) %{_sysconfdir}/logrotate.d/zabbix-server
%attr(0755,zabbix,zabbix) %dir %{_localstatedir}/log/zabbix
%attr(0755,zabbix,zabbix) %dir %{_localstatedir}/run/zabbix
%{_mandir}/man8/zabbix_server.8*
%if 0%{?rhel} >= 7
%{_unitdir}/zabbix-server.service
%{_prefix}/lib/tmpfiles.d/zabbix-server.conf
%else
%{_sysconfdir}/init.d/zabbix-server
%endif
%{_sbindir}/zabbix_server_mysql

%files server-pgsql
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_docdir}/zabbix-server-pgsql-%{version}/
%attr(0640,root,zabbix) %config(noreplace) %{_sysconfdir}/zabbix/zabbix_server.conf
%dir /usr/lib/zabbix/alertscripts
%dir /usr/lib/zabbix/externalscripts
%config(noreplace) %{_sysconfdir}/logrotate.d/zabbix-server
%attr(0755,zabbix,zabbix) %dir %{_localstatedir}/log/zabbix
%attr(0755,zabbix,zabbix) %dir %{_localstatedir}/run/zabbix
%{_mandir}/man8/zabbix_server.8*
%if 0%{?rhel} >= 7
%{_unitdir}/zabbix-server.service
%{_prefix}/lib/tmpfiles.d/zabbix-server.conf
%else
%{_sysconfdir}/init.d/zabbix-server
%endif
%{_sbindir}/zabbix_server_pgsql

%files proxy-mysql
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_docdir}/zabbix-proxy-mysql-%{version}/
%attr(0640,root,zabbix) %config(noreplace) %{_sysconfdir}/zabbix/zabbix_proxy.conf
%dir /usr/lib/zabbix/externalscripts
%config(noreplace) %{_sysconfdir}/logrotate.d/zabbix-proxy
%attr(0755,zabbix,zabbix) %dir %{_localstatedir}/log/zabbix
%attr(0755,zabbix,zabbix) %dir %{_localstatedir}/run/zabbix
%{_mandir}/man8/zabbix_proxy.8*
%if 0%{?rhel} >= 7
%{_unitdir}/zabbix-proxy.service
%{_prefix}/lib/tmpfiles.d/zabbix-proxy.conf
%else
%{_sysconfdir}/init.d/zabbix-proxy
%endif
%{_sbindir}/zabbix_proxy_mysql

%files proxy-pgsql
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_docdir}/zabbix-proxy-pgsql-%{version}/
%attr(0640,root,zabbix) %config(noreplace) %{_sysconfdir}/zabbix/zabbix_proxy.conf
%dir /usr/lib/zabbix/externalscripts
%config(noreplace) %{_sysconfdir}/logrotate.d/zabbix-proxy
%attr(0755,zabbix,zabbix) %dir %{_localstatedir}/log/zabbix
%attr(0755,zabbix,zabbix) %dir %{_localstatedir}/run/zabbix
%{_mandir}/man8/zabbix_proxy.8*
%if 0%{?rhel} >= 7
%{_unitdir}/zabbix-proxy.service
%{_prefix}/lib/tmpfiles.d/zabbix-proxy.conf
%else
%{_sysconfdir}/init.d/zabbix-proxy
%endif
%{_sbindir}/zabbix_proxy_pgsql

%files proxy-sqlite3
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_docdir}/zabbix-proxy-sqlite3-%{version}/
%attr(0640,root,zabbix) %config(noreplace) %{_sysconfdir}/zabbix/zabbix_proxy.conf
%dir /usr/lib/zabbix/externalscripts
%config(noreplace) %{_sysconfdir}/logrotate.d/zabbix-proxy
%attr(0755,zabbix,zabbix) %dir %{_localstatedir}/log/zabbix
%attr(0755,zabbix,zabbix) %dir %{_localstatedir}/run/zabbix
%{_mandir}/man8/zabbix_proxy.8*
%if 0%{?rhel} >= 7
%{_unitdir}/zabbix-proxy.service
%{_prefix}/lib/tmpfiles.d/zabbix-proxy.conf
%else
%{_sysconfdir}/init.d/zabbix-proxy
%endif
%{_sbindir}/zabbix_proxy_sqlite3

%files java-gateway
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README
%config(noreplace) %{_sysconfdir}/zabbix/zabbix_java_gateway.conf
%config(noreplace) %{_sysconfdir}/zabbix/zabbix_java_gateway_logback.xml
%attr(0755,zabbix,zabbix) %dir %{_localstatedir}/log/zabbix
%attr(0755,zabbix,zabbix) %dir %{_localstatedir}/run/zabbix
%if 0%{?rhel} >= 7
%{_datadir}/zabbix-java-gateway
%{_sbindir}/zabbix_java_gateway
%{_unitdir}/zabbix-java-gateway.service
%{_prefix}/lib/tmpfiles.d/zabbix-java-gateway.conf
%else
%{_sbindir}/zabbix_java
%{_sysconfdir}/init.d/zabbix-java-gateway
%endif

%files web
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README
%dir %attr(0750,apache,apache) %{_sysconfdir}/zabbix/web
%ghost %attr(0644,apache,apache) %config(noreplace) %{_sysconfdir}/zabbix/web/zabbix.conf.php
%config(noreplace) %{_sysconfdir}/zabbix/web/maintenance.inc.php
%config(noreplace) %{_sysconfdir}/httpd/conf.d/zabbix.conf
%{_datadir}/zabbix

%files web-mysql
%defattr(-,root,root,-)

%files web-pgsql
%defattr(-,root,root,-)

%files web-japanese
%defattr(-,root,root,-)

%endif


%changelog
* Mon Feb 15 2016 Kodai Terashima <kodai.terashima@zabbix.com> - 3.0.0-1
- update to 3.0.0

* Thu Feb 11 2016 Kodai Terashima <kodai.terashima@zabbix.com> - 3.0.0rc2
- update to 3.0.0rc2
- add TIMEOUT parameter for java gateway conf

* Thu Feb 04 2016 Kodai Terashima <kodai.terashima@zabbix.com> - 3.0.0rc1
- update to 3.0.0rc1

* Sat Jan 30 2016 Kodai Terashima <kodai.terashima@zabbix.com> - 3.0.0beta2
- update to 3.0.0beta2

* Thu Jan 21 2016 Kodai Terashima <kodai.terashima@zabbix.com> - 3.0.0beta1
- update to 3.0.0beta1

* Thu Jan 14 2016 Kodai Terashima <kodai.terashima@zabbix.com> - 3.0.0alpha6
- update to 3.0.0alpla6
- remove zabbix_agent conf and binary

* Wed Jan 13 2016 Kodai Terashima <kodai.terashima@zabbix.com> - 3.0.0alpha5
- update to 3.0.0alpha5

* Fri Nov 13 2015 Kodai Terashima <kodai.terashima@zabbix.com> - 3.0.0alpha4-1
- update to 3.0.0alpha4

* Thu Oct 29 2015 Kodai Terashima <kodai.terashima@zabbix.com> - 3.0.0alpha3-2
- fix web-pgsql package dependency
- add --with-openssl option

* Mon Oct 19 2015 Kodai Terashima <kodai.terashima@zabbix.com> - 3.0.0alpha3-1
- update to 3.0.0alpha3

* Tue Sep 29 2015 Kodai Terashima <kodai.terashima@zabbix.com> - 3.0.0alpha2-3
- add IfModule for mod_php5 in apache configuration file
- fix missing proxy_mysql alternatives symlink
- chagne snmptrap log filename
- remove include dir from server and proxy conf

* Fri Sep 18 2015 Kodai Terashima <kodai.terashima@zabbix.com> - 3.0.0alpha2-2
- fix create.sql doesn't contain schema.sql & images.sql

* Tue Sep 15 2015 Kodai Terashima <kodai.terashima@zabbix.com> - 3.0.0alpha2-1
- update to 3.0.0alpha2

* Sat Aug 22 2015 Kodai Terashima <kodai.terashima@zabbix.com> - 2.5.0-1
- create spec file from scratch
- update to 2.5.0
