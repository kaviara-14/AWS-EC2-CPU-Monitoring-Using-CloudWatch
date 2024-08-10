# AWS-EC2-CPU-Monitoring-Using-CloudWatch

Hosted a Nodejs application in EC2 Instance with Auto scaling and Application Load balancer attached on it. And Monitored the CPU utilization of the EC2 Instance using CloudWatch alarm,If the CPU utilization exceeds more than 65%, An alarm will be triggered to dynamically scales the number of Instance with the help of target tracking policy and also it invokes the lambda function to send a mail Notification using SNS topic.

### AWS Services : EC2 Instance, Auto Scaling Groups, Application Load Balancer, VPC, CloudWatch, Lambda, SNS Topic

## Project Description

### 1. Create an EC2 Instance
EC2 virtual servers host the Node.js application.Each EC2 instance is configured with the necessary environment for running the Node.js application. This includes installing Node.js, necessary libraries, and setting up the application server.

### 2. Create an Application Load Balancer (ALB)
The Application Load Balancer distributes incoming HTTP/HTTPS traffic across multiple EC2 instances to ensure even load distribution and enhance application availability. The ALB is set up with target groups that include the EC2 instances. It listens for incoming traffic on specified ports (e.g., HTTP on port 80) and routes requests to the appropriate instances based on load balancing algorithms.

### 3. Create Auto Scaling Group (ASG) 
Auto Scaling Group manages the number of EC2 instances dynamically based on the current load and predefined policies.We defined the Target Tracking Policy ,it maintains a specified average CPU utilization (e.g., 65%) by automatically scaling the number of EC2 instances. For instance, if CPU utilization exceeds 65%, the ASG will launch additional instances.


### 4. For increasing the CPU Utilization use this commands
Go to CLI executes this commands

    sudo dnf update<br>
    sudo dnf install stress-ng -y<br>
    sudo yum install stress -y<br>
    stress -c 4

### 5. Create CloudWatch Alarm
CloudWatch Provides monitoring and management of AWS resources and applications.The CloudWatch alarm is configured to trigger when the CPU utilization exceeds 65% for a specified period. The alarm is set to initiate scaling actions and invoke a Lambda function for notifications.

### 6. Create a Lambda Function
Lambda Function executes code in response to CloudWatch alarm triggers.It is created to handle notification tasks. It receives the alarm trigger and processes it to send an email notification.

### 7. Create SNS Topic
Simple Notification Service handles the distribution of notifications to subscribers.An SNS topic is created, and email subscriptions are added. The Lambda function publishes a message to this SNS topic whenever the CloudWatch alarm is triggered. This results in an email notification being sent to the subscribed recipients

