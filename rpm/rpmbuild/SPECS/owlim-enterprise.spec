%define __os_install_post %{nil}
Name: 		owlim-enterprise
Version: 	5.4.7348 
Release: 	1 
Summary: 	Owlim Enterprise Edition from Ontotext
Group: 		System Environment/Daemons
License: 	Copyright Ontotext AD. 
Url:		http://www.ontotext.com
Source0:	http://www.mirrorservice.org/sites/ftp.apache.org/tomcat/tomcat-7/v7.0.55/bin/apache-tomcat-7.0.55.tar.gz
Source1:	openrdf-workbench-%{version}.war 
Source2: 	openrdf-sesame-%{version}.war
Source3:	http://downloads.sourceforge.net/project/ejtools/JMX/1.2.0/jmx.browser-1.2.0.war
Source4:	https://psi-probe.googlecode.com/files/probe-2.3.3.zip	
AutoReqProv:    no

Requires: 	tomcat-native

BuildRoot: 	%{_tmppath}/%{name}-%{version}-build
BuildArch: 	noarch

%define tomcat_version 7.0.55
%define tomcat_url http://www.mirrorservice.org/sites/ftp.apache.org/tomcat/tomcat-7/v%{tomcat_version}/bin/apache-tomcat-%{tomcat_version}.tar.gz

%description
OWLIM-Enterprise is a replication cluster infrastructure based on OWLIM-SE. It offers industrial strength resilience and linearly scalable parallel query performance, with support for load-balancing and automatic fail-over.

%prep
if [ ! -e %{_sourcedir}/apache-tomcat-%{tomcat_version}.tar.gz ]
then
        wget %{tomcat_url} -P %{_sourcedir}
fi

if [ ! -e %{_sourcedir}/jmx.browser-1.2.0.war ]
then
        wget http://downloads.sourceforge.net/project/ejtools/JMX/1.2.0/jmx.browser-1.2.0.war -P %{_sourcedir}
fi

if [ ! -e %{_sourcedir}/probe-2.3.3.zip ]
then
        wget https://psi-probe.googlecode.com/files/probe-2.3.3.zip  -P %{_sourcedir}
fi

%{__unzip} -o %{_sourcedir}/probe-2.3.3.zip probe.war -d %{_sourcedir}

%install
%{__rm} -rf %{buildroot}
%{__mkdir} -p %{buildroot}/opt/tomcat/%{name}

%{__tar} -C %{buildroot}/opt/tomcat/%{name} -zxvf %{_sourcedir}/apache-tomcat-7.0.55.tar.gz --strip-components 1
%{__mkdir} -p %{buildroot}/etc/init.d/
%{__mkdir} -p %{buildroot}/opt/owlim-data/%{name}
%{__mkdir} -p %{buildroot}/var/run/%{name}
%{__mkdir} -p %{buildroot}/opt/stage/%{name}
%{__mkdir} -p %{buildroot}/etc/sysconfig

install %{_sourcedir}/openrdf-*-%{version}.war %{_sourcedir}/jmx.browser-1.2.0.war %{buildroot}/opt/stage/%{name}/
install %{_sourcedir}/probe.war %{buildroot}/opt/tomcat/%{name}/webapps/
install %{_sourcedir}/%{name}-sysconfig %{buildroot}/etc/sysconfig/%{name}
install %{_sourcedir}/%{name}-initscript %{buildroot}/etc/init.d/%{name}
install %{_sourcedir}/owlim.license %{buildroot}/etc/

%{__rm} -rf %{buildroot}/opt/tomcat/%{name}/webapps/{docs,examples,ROOT}

%clean
%{__rm} -rf %{buildroot}

%pre
if [ "$1" = "1" ]; then
    # Perform tasks to prepare for the initial installation
    getent group tomcat > /dev/null || groupadd -r tomcat
    getent passwd tomcat > /dev/null || useradd -m -r -g tomcat tomcat
elif [ "$1" = "2" ]; then
    # Perform whatever maintenance must occur before the upgrade begins
    service %{name} stop
    echo Removing contents of temp and work directories ...
    rm -rf /opt/tomcat/%{name}/{temp/*,work/*}
fi

%post
ln -vs /opt/stage/%{name}/jmx.browser-1.2.0.war /opt/tomcat/%{name}/webapps/jmx.war
ln -vs /opt/stage/%{name}/openrdf-workbench-%{version}.war /opt/tomcat/%{name}/webapps/openrdf-workbench.war
ln -vs /opt/stage/%{name}/openrdf-sesame-%{version}.war /opt/tomcat/%{name}/webapps/openrdf-sesame.war
chkconfig --add %{name}
echo Turning chkconfig on ...
chkconfig %{name} on
chkconfig %{name} --list
service %{name} start
%preun
if [ "$1" = "0" ] ; then
service %{name} stop 
chkconfig --del %{name}
fi

%files
%defattr(-,tomcat,tomcat,-)
/opt/tomcat/%{name}/bin
%config /opt/tomcat/%{name}/conf
/opt/tomcat/%{name}/lib
/opt/tomcat/%{name}/LICENSE
/opt/tomcat/%{name}/logs
/opt/tomcat/%{name}/NOTICE
/opt/tomcat/%{name}/RELEASE-NOTES
/opt/tomcat/%{name}/RUNNING.txt
/opt/tomcat/%{name}/temp
/opt/tomcat/%{name}/webapps
/opt/tomcat/%{name}/work
/opt/owlim-data/%{name}
/opt/stage/%{name}
/etc/sysconfig/%{name}
/var/run/%{name}
%attr(0600,tomcat,tomcat) /etc/owlim.license
%attr(0755,root,root) /etc/init.d/%{name}

%changelog
* Sun Aug 3 2014 phil@postdata.co.uk
First commit.
