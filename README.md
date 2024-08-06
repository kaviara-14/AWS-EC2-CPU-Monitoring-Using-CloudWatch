# AWS-EC2-CPU-Monitoring-Using-CloudWatch

Hosted a Nodejs application in EC2 Instance with Auto scaling and Application Load balancer attached on it. And Monitored the CPU utilization of the EC2 Instance using CloudWatch alarm,If the CPU utilization exceeds more than 65%, An alarm will be triggered to dynamically scales the number of Instance with the help of target tracking policy and also it invokes the lambda function to send a mail Notification using SNS topic.

**AWS Services :** EC2 Instance, Auto Scaling Groups, Application Load Balancer, VPC, CloudWatch, Lambda, SNS Topic

## Project Description

### 1. Create an EC2 Instance
Host the Node.js application on scalable Amazon EC2 instances, configured with a launch template or configuration. Ensure the application is deployed and accessible via the Application Load Balance

### 2. Create an Application Load Balancer (ALB)
Distribute incoming traffic across multiple EC2 instances to ensure high availability and load balancing. Configure listeners and target groups to route traffic efficiently.

### 3. Create Auto Scaling Group (ASG) 
Automatically adjust the number of EC2 instances based on CPU utilization metrics from CloudWatch. Set up target tracking policies to maintain performance and cost-efficiency.

### 4. For increasing the CPU Utilization use this commands

    sudo dnf update<br>
    sudo dnf install stress-ng -y<br>
    sudo yum install stress -y<br>
    stress -c 4

### 5. Create CloudWatch Alarm
Create a Alarm which Monitor CPU utilization of EC2 instances and it triggers whenever thresholds exceed 65%.And this also will invoke a Lambda function.

### 6. Create a Lambda Function
This Lambda execute code in response to CloudWatch alarms to send email notifications via SNS. Configure permissions and triggers for real-time alerts

### 7. Create SNS Topic
Manage and distribute email notifications for alarms triggered by CloudWatch. Create a topic and subscribe email addresses to receive alerts.


