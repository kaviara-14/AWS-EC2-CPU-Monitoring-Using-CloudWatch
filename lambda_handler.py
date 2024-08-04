import boto3

def lambda_handler(event, context):
    # TODO implement

    client = boto3.client('sns')
    snsArn = 'your ARN'
    message = "Dear Team, This is to inform you that the CPU utilization has reached 50%. While this level is not critical, it’s advisable to monitor the situation to ensure there are no underlying issues affecting performance."

    response = client.publish(
        TopicArn = snsArn,
        Message = message ,
        Subject='"Alert: CPU Utilization reached 50%"'
    )
