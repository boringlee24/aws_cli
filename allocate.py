import sys
import pdb
import subprocess
import json
import os
import argparse
#import psutil
import time
#import datetime
#from pathlib import Path

instances = ['t2.xlarge', 't3.xlarge', 't3a.xlarge', 'm4.xlarge', 'm5.xlarge', 'm5a.xlarge', 'm5n.xlarge', 'c4.2xlarge', 'c5.2xlarge', 'c5a.2xlarge', 'c5n.2xlarge', 'r4.large', 'r5.large', 'r5a.large', 'r5n.large']

#Path(f'../logs/simulator/{instance}').mkdir(parents=True, exist_ok=True)
#Path(f'../logs_load/simulator/{instance}').mkdir(parents=True, exist_ok=True)

# allocating for each instance
for ins in instances:
    cwd = '.'
    cmd = f'./launch.sh {ins}'
    print(cmd)
    subprocess.check_call([cmd], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, cwd = cwd)
    time.sleep(1)

