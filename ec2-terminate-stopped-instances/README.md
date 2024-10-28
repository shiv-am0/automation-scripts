# EC2 Terminate Stopped Instances

## Intro
This AWS Lambda function, written in Python, uses the AWS SDK (`boto3`) to identify and terminate any EC2 instances that are in a **stopped** state. By terminating stopped instances, this script helps optimize cloud resource usage and reduce unnecessary costs. The script is designed to run as a scheduled Lambda function, allowing for automatic and regular cleanup of stopped instances.

## Real World Use Case
In many AWS environments, EC2 instances are often stopped but not terminated, leading to potential wastage of cloud resources. While stopped instances don't incur compute charges, they still retain attached EBS volumes and associated resources that might incur costs. This Lambda function can be scheduled to run periodically, ensuring that any instance left in a stopped state is automatically terminated, minimizing expenses and freeing up resources.

## Functions Used
The script relies on the following main functions from the `boto3` library:

1. **`describe_instances`**: Retrieves details about EC2 instances, including their IDs and states. This is filtered to only return instances in a `stopped` state.

2. **`terminate_instances`**: Terminates the EC2 instances identified as `stopped`. This action permanently deletes the instance.

### Script Logic:
- The `describe_instances` call filters instances by the `stopped` state, collecting their instance IDs.
- The `terminate_instances` call then terminates each stopped instance, releasing associated resources.
- **Logging** is used to track which instances are terminated or if no stopped instances are found.

## Running the Script in AWS Lambda

### 1. Create the Lambda Function
- Go to the AWS Lambda Console and click on **Create function**.
- Set the runtime to **Python 3.x** and choose the **Create a new role with basic Lambda permissions** option.
- Click **Create function**.

### 2. Add Permissions
Assign an IAM role to your Lambda function with the following permissions:
- `ec2:DescribeInstances` – to retrieve instance information.
- `ec2:TerminateInstances` – to terminate stopped instances.

### 3. Add the Code
- Add the code into the **Code** tab of the Lambda function.
- Configure the necessary IAM role with EC2 permissions, and set up a trigger using Amazon CloudWatch Events.

---

Feel free to explore and modify this script to fit additional scenarios as needed, and keep your AWS environment optimized!
