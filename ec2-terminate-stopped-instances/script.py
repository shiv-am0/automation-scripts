import boto3
import logging

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    ec2_client = boto3.client("ec2")
    
    try:
        # Describe EC2 instances with a filter for stopped instances
        response = ec2_client.describe_instances(
            Filters=[
                {"Name": "instance-state-name", "Values": ["stopped"]}
            ]
        )
        
        # Collect instance IDs of stopped instances
        stopped_instances = [
            instance["InstanceId"]
            for reservation in response["Reservations"]
            for instance in reservation["Instances"]
        ]
        
        if stopped_instances:
            # Terminate stopped instances
            terminate_response = ec2_client.terminate_instances(
                InstanceIds=stopped_instances
            )
            logger.info(f"Terminated instances: {stopped_instances}")
        else:
            logger.info("No stopped instances found.")
    
    except Exception as e:
        logger.error(f"Error terminating instances: {str(e)}")
