owlim-packages
==============

# Introduction

 - Build operating system packages for the OWLIM-Enterprise triple-store from Ontotext.
 - Ships with useful init scripts and default configuration.
 - A simple way to get a local OWLIM development environment up and running.

# Building the RPM

#### Prerequisites

You need to obtain three files from Ontotext and place them inside the rpm/rpmbuild/SOURCES directory

They files you will need are:-

    openrdf-workbench-7.4.38.war
    openrdf-sesame-7.4.38.war
    owlim.license

The version number of OWLIM-Enterprise you receive may be different. You will find the .war files inside the OWLIM .zip file you receive or from the Ontotext Maven repository.

Update `rpm/rpmbuild/SPEC/owlim-enterprise.spec` and change the `Version:` tag to match the version of Owlim-Enterprise you have.

If you want to use the Vagrant VM to build the packages or to use for OWLIM, you will need:-
 - Vagrant (https://www.vagrantup.com/)
 - VirtualBox (https://www.virtualbox.org/)

#### Build and install the RPM

    git clone git@github.com:philipwigg/owlim-packages.git
    cd owlim-packages/rpm
    vagrant up
    [Wait for the VM start up and to provision]
    vagrant ssh
    [You are now logged into your Vagrant VM]
    rpmbuild -bb rpmbuild/SPECS/owlim-enterprise.spec
    sudo rpm -i rpmbuild/RPMS/noarch/owlim-enterprise-5.4.7348-1.noarch.rpm

That's it! You can now start using OWLIM-Enterprise by browsing the Workbench URL below.

You will find the .rpm in the `~vagrant/rpmbuild/RPMS/noarch/` directory on your Vagrant VM.

Because this is a Vagrant shared folder, it's there inside `owlim-packages/rpm/rpmbuild/RPMS/noarch/` on your local machine too.

# Configuration and URLs

The packages install OWLIM-Enterprise using Tomcat as a container.

It will download the latest version of Tomcat from the internet during the build.

It also grabs a JMX Brower from EJTools which I find very useful, along with the Probe monitoring application.

#### Default URLs

Workbench - http://192.168.33.10:8080/openrdf-workbench/<br>
JMX Browser - http://192.168.33.10:8080/jmx/<br>
Probe - http://192.168.33.10:8080/probe/

#### Default File Locations

OWLIM Tomcat Directory - `/opt/tomcat/owlim-enterprise`<br>
OWLIM Data Directory - `/opt/owlim-data/owlim-enterprise`<br>
Sesame Logs Directory - `/opt/owlim-data/owlim-enterprise/openrdf-sesame/logs`<br>
OWLIM JVM Options - `/etc/sysconfig/owlim-enterprise`<br>
OWLIM init script - `/etc/init.d/owlim-enterprise`

#### Stopping and starting

Olwim is configured with an SysV init script and added a service.

    sudo service owlim-enterprise stop
    sudo service owlim-enterprise start
    sudo service owlim-enterprise restart

The init script can be configured to send a SIGKILL to OWLIM if it doesn't shut down within a configurable time limit. This can be useful if in development or C.I. environments.

Take a look inside `/etc/init.d/owlim-enterprise` to set these options.
