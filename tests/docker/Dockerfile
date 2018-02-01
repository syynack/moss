FROM debian:jessie

RUN apt-get update
RUN apt-get --assume-yes install quagga lldpd python python-pip git pkg-config bash-completion vim openssh-server net-tools

WORKDIR /etc/moss
ADD run-services.sh /etc/moss/
ADD debian.conf /etc/quagga/debian.conf
ADD daemons /etc/quagga/daemons

RUN touch /etc/quagga/bgpd.conf
RUN touch /etc/quagga/ospf6d.conf
RUN cp /usr/share/doc/quagga/examples/zebra.conf.sample /etc/quagga/zebra.conf
RUN cp /usr/share/doc/quagga/examples/vtysh.conf.sample /etc/quagga/vtysh.conf
RUN cp /usr/share/doc/quagga/examples/ospf6d.conf.sample /etc/quagga/ospf6d.conf
RUN cp /usr/share/doc/quagga/examples/bgpd.conf.sample /etc/quagga/bgpd.conf

RUN chown quagga.quaggavty /etc/quagga/*.conf
RUN chmod 640 /etc/quagga/*.conf
RUN chmod 777 /var/run/
RUN sed -i 's/#net.ipv6.conf.all.forwarding=1/net.ipv6.conf.all.forwarding=1/g' /etc/sysctl.conf
RUN sed -i 's/#net.ipv4.ip_forward=1/net.ipv4.ip_forward=1/g' /etc/sysctl.conf
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/g' /etc/ssh/sshd_config
EXPOSE 23
