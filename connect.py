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

instances = ['t2.xlarge', 't3.xlarge']

#Path(f'../logs/simulator/{instance}').mkdir(parents=True, exist_ok=True)
#Path(f'../logs_load/simulator/{instance}').mkdir(parents=True, exist_ok=True)
cwd = '.'
cmd = f'./describe.sh > instance.json'
subprocess.check_call([cmd], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, cwd = cwd)
time.sleep(1)

with open('instance.json') as f:
    describe = json.load(f)

ins = 't2.xlarge'
for item in describe:
    if item[0][1] == ins:
        addr = item[0][-1]

        conn = Connection(
        host=addr,
        user='ubuntu',
        connect_kwargs={
        "key_filename": "/home/ubuntu/.ssh/baolin_key.pem",
        },)
        conn.run('tmux new-session -d -s 0 "cd /home/ubuntu/GIT/cloud_inf/models && sleep 10 && cp readme.txt abc.txt"')

# allocating for each instance
for ins in instances:
    cmd = f'./launch.sh {ins}'
    print(cmd)
    subprocess.check_call([cmd], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, cwd = cwd)
    time.sleep(1)

