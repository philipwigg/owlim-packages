package { 'puppet-lint':
  provider => gem
}

package { 'epel-release':
  provider => 'rpm',
  source => 'https://anorien.csc.warwick.ac.uk/mirrors/epel/6/i386/epel-release-6-8.noarch.rpm'
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
  require => Package['epel-release']
}
