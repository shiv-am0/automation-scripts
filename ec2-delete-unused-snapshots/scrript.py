import boto3

# Initialize a boto3 EC2 client
ec2 = boto3.client('ec2')

def get_snapshots():
    """
    Get all snapshots owned by the account.
    """
    try:
        snapshots = ec2.describe_snapshots(OwnerIds=['self'])['Snapshots']
        return snapshots
    except Exception as e:
        print(f"Failed to retrieve snapshots: {e}")
        return []

def get_volumes():
    """
    Get all volumes and store the volume ids.
    """
    try:
        volumes = ec2.describe_volumes()['Volumes']
        used_snapshots = []
        for volume in volumes:
            if 'SnapshotId' in volume:
                used_snapshots.append(volume['SnapshotId'])
        return used_snapshots
    except Exception as e:
        print(f"Failed to retrieve volumes: {e}")
        return []

def delete_unused_snapshots():
    """
    Delete all snapshots that are not associated with any volumes.
    """
    snapshots = get_snapshots()
    used_snapshots = get_volumes()

    for snapshot in snapshots:
        snapshot_id = snapshot['SnapshotId']
        if snapshot_id not in used_snapshots:
            try:
                ec2.delete_snapshot(SnapshotId=snapshot_id)
                print(f"Deleted snapshot: {snapshot_id}")
            except Exception as e:
                print(f"Error deleting snapshot {snapshot_id}: {e}")

def lambda_handler(event, context):
    """
    AWS Lambda entry point.
    """
    print("Starting unused snapshot cleanup process")
    delete_unused_snapshots()
    print("Unused snapshot cleanup process completed")
    return {
        'statusCode': 200,
        'body': 'Unused snapshot cleanup completed successfully'
    }
