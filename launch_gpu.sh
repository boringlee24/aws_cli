#!/bin/bash


# launch gpu
aws ec2 run-instances --image-id ami-09d8149cb9ac749cf --count 1 --instance-type $1 --key-name baolin_key --security-group-ids launch-wizard-54

