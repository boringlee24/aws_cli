#!/bin/bash

# launch cpu
aws ec2 run-instances --image-id ami-0dc5fb31ca925d1f0 --count 1 --instance-type $1 --key-name baolin_key --security-group-ids launch-wizard-54

# launch gpu
#aws ec2 run-instances --image-id ami-03306fea7e787b838 --count 1 --instance-type $1 --key-name baolin_key --security-group-ids launch-wizard-54

