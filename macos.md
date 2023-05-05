memory leak when using matplotlib on macos:
put matplotlib in background
```python
import matplotlib
matplotlib.pyplot.switch_backend('Agg')
```

process leak when using ray:
make dataloader with worker number 0

termal state:
```shell
sudo powermetrics --samplers thermal
```

bypass xprotect 
```shell
codesign --force --deep --sign - <your executable or app>
```