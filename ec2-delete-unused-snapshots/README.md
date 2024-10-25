# Delete Unassociated Snapshots (AWS)

## Introduction

The **Delete Unassociated Snapshots** script is a Python automation tool using the AWS SDK (Boto3) to identify and delete EBS snapshots that are not associated with any active volume. This script is particularly useful for managing costs and optimizing AWS resources by removing redundant EBS snapshots that are no longer in use.

The script functions by:
1. Scanning for all available EBS snapshots within a specific AWS account.
2. Identifying snapshots that are not associated with any active EC2 volume or snapshots with volumees not mounted to any EC2 instance.
3. Deleting these unassociated snapshots to free up storage and reduce unnecessary costs.

## Real-World Use Case

In large cloud environments, unused EBS snapshots can accumulate over time due to actions such as terminating instances, detaching volumes, or routine backups. These orphaned snapshots can lead to unnecessary storage costs. Regularly running this script ensures that only useful, associated snapshots are retained, helping keep the cloud environment cost-effective and clean.

## Functions Used

### 1. `boto3.client('ec2')`
   - **Description**: Initializes the EC2 client using Boto3, AWS's SDK for Python. The client is used to interact with various EC2 resources.
   - **Role in Script**: Allows the script to connect to AWS EC2 services and query for available snapshots and associated volumes.

### 2. `describe_snapshots()`
   - **Description**: Retrieves a list of EBS snapshots owned by the AWS account.
   - **Role in Script**: Used to fetch all snapshots to assess whether each snapshot is associated with any volume. Filters are applied to specify snapshots owned by the account.

### 3. `describe_volumes()`
   - **Description**: Retrieves a list of volumes, including details about associated snapshots.
   - **Role in Script**: Helps determine if snapshots are actively associated with any EC2 volume. The script compares this information against the snapshot list to identify unassociated snapshots.

### 4. `delete_snapshot(SnapshotId=snapshot_id)`
   - **Description**: Deletes the specified snapshot by ID.
   - **Role in Script**: Once unassociated snapshots are identified, this function is used to delete each orphaned snapshot, freeing up storage resources.

## Running the Script in AWS Lambda

This script can be easily adapted for AWS Lambda to automate the deletion of unassociated snapshots on a schedule (e.g., daily, weekly). Just upload the script in Lambda, configure the necessary IAM role with EC2 permissions, and set up a trigger using Amazon CloudWatch Events.

---

Feel free to explore and modify this script to fit additional scenarios as needed, and keep your AWS environment optimized!
