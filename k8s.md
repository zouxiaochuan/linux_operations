## print join command
```shell
kubeadm token create --print-join-command
```

## reboot node
```shell
# mark node as unscheduleable
kubectl cordon <node>
# remove all the running pods
kubectl drain <node> --ignore-daemonsets --delete-emptydir-data
# do your job here...

# mark node as scheduleable
kubectl uncordon <node>
# get node info
kubectl get node <node>
```


## flannel oom
```shell
kubectl patch ds -n=kube-system kube-flannel-ds -p '{"spec": {"template":{"spec":{"containers": [{"name":"kube-flannel", "resources": {"limits": {"cpu": "250m","memory": "550Mi"},"requests": {"cpu": "100m","memory": "100Mi"}}}]}}}}'
```

## mount ceph
```shell
# mount default file system
sudo mount -t ceph 127.0.0.1,localhost:/ /mnt/ceph/ -o name=admin,secret=admin
```

## renew certs
```shell
sudo kubeadm certs renew all
# then reboot master
```

## problem of "no route to" pod
```shell
# just restart kube-proxy on the machine that pod resides
```

## ceph problem: "given Volume ID already exists"
```shell
# restart provisioner
kubectl rollout restart deployment csi-cephfsplugin-provisioner
kubectl rollout restart deployment csi-rbdplugin-provisioner

# restart deamensets
kubectl rollout restart ds -n rook-ceph
```
