package { 'puppet-lint':
  provider => gem
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
            'rpm-build' ]:
  ensure=> present
}
