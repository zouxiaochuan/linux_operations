import sys
import os
from kubernetes import client, config

TARGET_NS = 'common'

if __name__ == '__main__':
    local_path = sys.argv[1]
    ceph_path = sys.argv[2]

    config.load_kube_config()
    v1 = client.CoreV1Api()
    pvcs = v1.list_namespaced_persistent_volume_claim(namespace=TARGET_NS)

    pvcs: client.V1PersistentVolumeClaimList
    for pvc in pvcs.items:
        name = pvc.metadata.name
        volume_name = pvc.spec.volume_name

        # print(volume_name)
        pv = v1.read_persistent_volume(
            name=volume_name)

        subvolume = pv.spec.csi.volume_attributes['subvolumeName']
        subvolume_path = os.path.join(ceph_path, subvolume)
        subfolders = os.listdir(subvolume_path)

        subfolders = [os.path.join(subvolume_path, sf) for sf in subfolders]
        subfolders = [sf for sf in subfolders if os.path.isdir(sf)]
        
        # print(subvolume_path)
        if len(subfolders) != 1:
            raise RuntimeError('folders under subvolume is not equal to 1')
            pass

        fullfolder = os.path.join(subvolume_path, subfolders[0])
        dst_folder = os.path.join(local_path, name)
        cmd = f'ln -s {fullfolder} {dst_folder}'
        print(cmd)
        retcd = os.system(cmd)
        if retcd != 0:
            raise RuntimeError(str(retcd))
        pass
    pass
