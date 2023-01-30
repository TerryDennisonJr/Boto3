#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Terry Dennison Jr.
# Purpose: Create an AWS ec2 instance with Python

def deploy():

    import yaml
    import boto3
    import os

    # creation of boto3 resource for key
    ec2 = boto3.resource('ec2')

    # create a file to store the key locally
    outfile = open('ec2-keypair.pem', 'w')

    # call the boto ec2 function to create a key pair
    key_pair = ec2.create_key_pair(KeyName='ec2-keypair')

    # capture the key and store it in a file
    KeyPairOut = str(key_pair.key_material)
    #print(KeyPairOut)
    outfile.write(KeyPairOut)
    
    # sets permissions of .pem file to 444
    os.chmod('path_to_.pem_file', 0o444)

    # extraction of YAML file and setting of YAML file location
    with open(r'path_to.yaml_file') as file:

        server_specs = yaml.safe_load(file)
        
        # iterate through yaml file for items
        for spec, config in server_specs.items():
            print(spec, ":", config)

        ami = config['ami_type']
        instance_type = config['instance_type']
        ec2_Min = config['min_count']
        ec2_Max = config['max_count']

        print('\nData extracted from YAML file...')
        
        # creation of aAWS ec2 instance with items from Yaml file
        instances = ec2.create_instances(
            ImageId=ami,
            MinCount=ec2_Min,
            MaxCount=ec2_Max,
            InstanceType=instance_type,
            KeyName='ec2-keypair'
        )

# run deploy function        
deploy()
