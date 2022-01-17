## reboot node
```shell
# mark node as unscheduleable
kubectl cordon <node>
# remove all the running pods
kubectl drain <node> --ignore-daemonsets
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
