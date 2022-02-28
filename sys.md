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
sudo systemctl mask motd-news motd-news.timer snapd ModemManager fwupd-refresh.timer fwupd-refresh fwupd apt-daily-upgrade.timer apt-daily.timer snapd.snap-repair.timer snapd.snap-repair apt-daily apt-daily-upgrade uplugplay rshim
```

repair gpu driver after reboot
```shell
gpu_ver=$(cut -d'-' -f2 <<< `ls /usr/src | grep nvidia`)
sudo apt-get install dkms
sudo dkms install -m nvidia -v $gpu_ver
```
