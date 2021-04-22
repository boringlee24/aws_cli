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
from fabric import Connection

instances = ['t2.xlarge', 't3.xlarge', 't3a.xlarge', 'm4.xlarge', 'm5.xlarge', 'm5a.xlarge', 'm5n.xlarge', 'c4.2xlarge', 'c5.2xlarge', 'c5a.2xlarge', 'c5n.2xlarge', 'r4.large', 'r5.large', 'r5a.large', 'r5n.large']

#Path(f'../logs/simulator/{instance}').mkdir(parents=True, exist_ok=True)
#Path(f'../logs_load/simulator/{instance}').mkdir(parents=True, exist_ok=True)
cwd = '.'
cmd = f'./describe.sh > instance.json'
subprocess.check_call([cmd], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, cwd = cwd)
time.sleep(1)

with open('instance.json') as f:
    describe = json.load(f)

for ins in instances:
    for item in describe:
        if item[0][1] == ins:
            addr = item[0][-1]
            ins_id = item[0][0] 
            conn = Connection(
            host=addr,
            user='ubuntu',
            connect_kwargs={
            "key_filename": "/home/ubuntu/.ssh/baolin_key.pem",
            },)
            # first push, then terminate
            try:
                conn.run(f'python git_push.py {ins}')
            except:
                print(f'push failed for {ins}, not finished')
                pass
            else:
                print(f'push succedded for {ins}, terminating instance')
                cmd = f'./terminate.sh {ins_id}'
                subprocess.check_call([cmd], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, cwd = cwd)
            break
