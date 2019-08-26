import boto3

ec2 = boto3.resource('ec2')

def lambda_handler(event, context):
    for instance in ec2.instances.all():
        for tag in (instance.tags or []):
            if tag['Key'] == 'Hibernate' and \
            tag['Value'] == 'True':
                instance.stop()
                print('Hibernating Instance: ' + instance.id)
                break
