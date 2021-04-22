#!/bin/bash

aws ec2 describe-instances --filters "Name=instance-state-name,Values=pending,running" --query Reservations[*].Instances[*].[InstanceId,InstanceType,State,PublicDnsName]
