import sys
import os
from tqdm import tqdm
import time


if __name__ == '__main__':
    filename = sys.argv[1]
    target_path = sys.argv[2]

    packages = []
    failed = []
    with open(filename, 'r') as f:
        for line in f:
            name, version, hashv = line.strip().split()
            pkg_filename = '{}-{}-{}.tar.bz2'.format(name, version, hashv)
            target_file = os.path.join(target_path, pkg_filename)
            if os.path.exists(target_file):
                continue

            url = f'https://anaconda.org/anaconda/{name}/{version}/download/win-64/{pkg_filename}'
            os.system('wget -O {} {}'.format(target_file, url))
            print(os.path.getsize(target_file))
            if os.path.getsize(target_file) == 0:
                
                os.system('wget -O {} {}'.format(target_file, url.replace('win-64', 'noarch')))

                if os.path.getsize(target_file) == 0:
                    failed.append(line)
                    pass
                pass
            time.sleep(3)
            pass
        pass

    print(failed)
    pass