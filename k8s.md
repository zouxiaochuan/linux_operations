## reboot node
\#mark node as unscheduleable<br>
kubectl cordon \<node\> <br>
\#remove all the running pods<br>
kubectl drain \<node\> --ignore-daemonsets<br>
\#do your job here... <br>

\#mark node as scheduleable <br>
kubectl uncordon \<node\> <br>
\#get node info <br>
kubectl get node \<node\> <br>
