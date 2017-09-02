#! /bin/sh

chmod 777 /var/run/
/etc/init.d/quagga restart
/etc/init.d/lldpd restart
/etc/init.d/ssh restart
