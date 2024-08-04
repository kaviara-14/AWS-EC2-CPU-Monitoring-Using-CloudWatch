import boto3

def lambda_handler(event, context):
    # TODO implement

    client = boto3.client('sns')
    snsArn = 'arn:aws:sns:us-east-1:992382388720:snsMail'
    message = "This is a test notification."

    response = client.publish(
        TopicArn = snsArn,
        Message = message ,
        Subject='Hello'
    )