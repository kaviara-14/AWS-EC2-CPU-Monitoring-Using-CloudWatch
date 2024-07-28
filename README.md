# AWS-EC2-CPU-Monitoring-Using-CloudWatch

Hosted a Nodejs application in EC2 Instance with Auto scaling and Application Load balancer attached on it. And Monitored the CPU utilization of the EC2 Instance using CloudWatch alarm,If the CPU utilization exceeds more than 65%, An alarm will be triggered to dynamically scales the number of Instance with the help of target tracking policy and also it invokes the lambda function to send a mail Notification using SNS topic.

**AWS Services :** EC2 Instance, Auto Scaling Groups, Application Load Balancer, VPC, CloudWatch, Lambda, SNS Topic
