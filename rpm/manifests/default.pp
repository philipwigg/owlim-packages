include epel

package { 'puppet-lint':
  provider => gem
}

service { 'iptables':
  ensure => stopped
}


package { [ 'autoconf',
            'automake',
            'binutils',
            'bison',
            'flex',
            'gcc',
            'gcc-c++',
            'gettext',
            'libtool',
            'make',
            'patch',
            'pkgconfig',
            'redhat-rpm-config',
            'rpm-build',
            'java-1.7.0-openjdk',
            'tomcat-native']:
  ensure => present,
  require => Class['epel']
}
