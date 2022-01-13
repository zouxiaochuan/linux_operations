## reboot node
//mark node as unscheduleable
kubectl cordon \<node\> <br>
//remove all the running pods
kubectl drain \<node\> --ignore-daemonsets<br>
//do your job here...

//mark node as scheduleable
kubectl uncordon \<node\> <br>
//get node info
kubectl get node \<node\> <br>