# make changes to our configuration file using puppet

exec {'/etc/ssh/sshd_config':
 path    => '/etc/ssh/sshd_config'
 ensure  => 'PasswordAuthentication no'
 }
