upgrade kernel
```shell
uname -r # display current version
sudo apt-get update
sudo apt-get dist-upgrade
```

create sudo user
```shell
sudo adduser yourname
sudo usermod -aG sudo yourname
```

search log
```shell
sudo journalctl --since "1 hour ago"
/var/log/syslog
cat /var/log/auth.log | grep sudo
```

stop ubuntu auto started service
```shell
sudo systemctl mask motd-news motd-news.timer snapd ModemManager fwupd-refresh.timer fwupd-refresh fwupd apt-daily-upgrade.timer apt-daily.timer snapd.snap-repair.timer snapd.snap-repair apt-daily apt-daily-upgrade uplugplay rshim unattended-upgrades
```

repair gpu driver after reboot
```shell
gpu_ver=$(cut -d'-' -f2 <<< `ls /usr/src | grep nvidia`)
sudo apt-get install dkms
sudo dkms install -m nvidia -v $gpu_ver
```

repair apt error of NO_PUBKEY: XXX
```shell
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys XXX
```

remove all mapper devices
```shell
sudo dmsetup remove_all
```

use nmcli to change ip address
```shell
nmcli con modify <interface> ipv4.method manual
nmcli con modify <interface> ipv4.address 192.168.1.100/24
nmcli con down <interface>
nmcli con up <interface>
```

download apt packages
```shell
apt reinstall --download-only -o Dir::Cache::archives="/root/packages/deb/" <your packages>
```
