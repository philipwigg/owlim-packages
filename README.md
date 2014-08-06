owlim-packages
==============

Create .rpm and .deb files for the Owlim-Enterprise Triplestore from Ontotext.

# Introduction

 - Build operating system packages for the Owlim triple-store from Ontotext.
 - Ships with useful init scripts and default configuration.
 - A simple way to get a local Owlim development environment up and running.


# Building the RPM

#### Prerequisites

You need to obtain three files from Ontotext and place them inside the rpm/rpmbuild/SOURCES directory

They files you will need are:-

    openrdf-workbench-7.4.38.war
    openrdf-sesame-7.4.38.war
    owlim.license

Update `rpm/rpmbuild/SPEC/owlim-enterprise.spec` and change the `Version:` tag to match the version of Owlim-Enterprise you have.

#### Build and install the RPM

    git clone git@github.com:philipwigg/owlim-packages.git
    cd owlim-package/rpm
    vagrant up
    [Wait for the VM start up and to provision]
    vagrant ssh
    [You are now logged into your Vagrant VM]
    rpmbuild -bb rpmbuild/SPECS/owlim-enterprise.spec
    sudo rpm -i rpmbuild/RPMS/noarch/owlim-enterprise-5.4.7348-1.noarch.rpm

That's it! You can now start using Owlim-Enterprise by browsing the Workbench URL below.

You will find the .rpm in the `~vagrant/rpmbuild/RPMS/noarch/` directory on your Vagrant VM.

Because this is a Vagrant shared folder, it's there inside `owlim-packages/rpm/rpmbuild/RPMS/noarch/` on your local machine too.

# Configuration and URLs

The packages install Owlim-Enterprise using Tomcat as a container.

It will download the latest version of Tomcat from the internet during the build.

It also grabs a JMX Brower from EJTools which I find very useful, along with the Probe monitoring application.

#### Default URLs

Workbench - http://192.168.33.10:8080/openrdf-workbench/<br>
JMX Browser - http://192.168.33.10:8080/jmx/<br>
Probe - http://192.168.33.10:8080/probe/

#### Default File Locations

Owlim Tomcat Directory - `/opt/tomcat/owlim-enterprise`<br>
Owlim Data Directory - `/opt/owlim-data/owlim-enterprise`<br>
Owlim JVM Options - `/etc/sysconfig/owlim-enterprise`
