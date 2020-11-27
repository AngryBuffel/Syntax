import json
import boto3
import requests

class Engine():
    def __init__(self, inst_name, dns_name, status, job_id):
        self.inst_name = inst_name
        self.dns_name = dns_name
        self.status = status
        self.job_id = job_id
    def start(self):
        ec2.start_instances(InstanceIds=[self.inst_name],DryRun=False)
        return print('Started instance:'+self.inst_name+', ')
    def stop(self):
        ec2.stop_instances(InstanceIds=[self.inst_name],DryRun=False)
        return print('Stopped instance:'+self.inst_name+', ')

def fme_api_call(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return response.json()
        
def build_engines(aws_response,fme_dict):
    idx = 0
    engines_dict = {}
    for reservation in aws_response['Reservations']:
        for instance in reservation['Instances']:
            if instance['State']['Name'] == 'running':
                engines_dict['engine'+str(idx)]= Engine(instance['InstanceId'], \
                    instance['PrivateDnsName'], instance['State']['Name'],fme_dict[instance['PrivateDnsName']])
                idx += 1
            else:
                engines_dict['engine'+str(idx)]= Engine(instance['InstanceId'],  \
                    instance['PrivateDnsName'], instance['State']['Name'],None)
                idx += 1
    return engines_dict

def start_stop_engine(engine_N,fme_queue):
    if fme_queue['totalCount'] == 0:
        if engine_N.job_id == -1:
            engine_N.stop()
        elif engine_N.status == 'stopped':
            print('No action taken, instance: '+engine_N.inst_name+' is already stopped.')
        else:
            print('No action taken, instance: '+engine_N.inst_name+' is busy.\nNo items in queue.')
    else:
        if engine_N.status == 'stopped':
            engine_N.start()
        else:
            print('No action taken, instance: '+engine_N.inst_name+' is busy.\nThere are items in queue.')
    return None

region = 'us-east-1'
vpc_endpoint = 'url'
ec2 = boto3.client('ec2', region_name=region, endpoint_url=vpc_endpoint)
url_engine_status = 'url'
url_jobqueue = 'url'
custom_filter = [{'Name':'tag:fme_resource', 'Values': ['engine']}]

def engine_check(event=None, context=None):
    fme_response = fme_api_call(url_engine_status)
    fme_queue = fme_api_call(url_jobqueue)
    aws_response = ec2.describe_instances(Filters=custom_filter)
    fme_dict = {}
    for item in fme_response['items']:
        fme_dict[item['hostName']]=item['currentJobID']
    engines = build_engines(aws_response,fme_dict)
    for engine in engines:
        start_stop_engine(engines[engine],fme_queue)
