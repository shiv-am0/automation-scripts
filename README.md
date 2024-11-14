# AWS Lambda Automation Scripts

Welcome to the **AWS Lambda Automation Scripts** repository! This repository is a collection of Python scripts for AWS Lambda, tailored for automation tasks commonly faced by DevOps engineers. I will be developing and pushing scripts along my journey of learning DevOps and Cloud technologies using AWS.

These scripts address real-world scenarios, helping automate various routine tasks that can improve productivity and reduce manual effort. As my learning progresses, I’ll continue adding more scripts covering a broad range of DevOps automation needs.

---

## Table of Contents

- [About](#about)
- [AWS Lambda Integration](#aws-lambda-integration)
- [Running Scripts Locally](#running-scripts-locally)
- [License](#license)

---

## About

This repository serves as a record of my learning process in DevOps and Cloud. It contains automation scripts in Python for AWS Lambda, focusing on tasks that help streamline operations and improve efficiency for DevOps teams. Each script is designed to perform a specific task, such as managing AWS resources or automating deployment pipelines.

The primary goals of this repository are to:
- Build practical experience with AWS cloud platform.
- Develop reusable automation scripts to solve real-world challenges.
- Showcase my growth and understanding in the DevOps field.

---

## AWS Lambda Integration

Some scripts are designed to be used as AWS Lambda functions. To use these scripts in AWS Lambda, follow these steps:

1. **Create a Lambda Function**:
   - Go to the AWS Management Console and open the [AWS Lambda Console](https://console.aws.amazon.com/lambda/).
   - Click on **Create Function**.
   - Choose **Author from scratch** and provide a name for your function.
   - Select **Python** as the runtime.
   - Set up the necessary execution role, ensuring it has permissions to access the AWS resources required by the script (e.g., EC2, S3).

2. **Copy the Script**:
   - Open the code editor in the Lambda console and paste the contents of the script file.

3. **Set Environment Variables**:
   - If the script requires any environment variables, add them in the **Configuration** section under **Environment variables**.

4. **Test the Function**:
   - Configure a test event if needed, or manually invoke the function.
   - Check the **CloudWatch Logs** for execution details and error handling.

---

## Running Scripts Locally

To run these scripts on your local machine, follow the steps below:

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/DevOps-Automation-Scripts.git
cd DevOps-Automation-Scripts
```

### 2. Set Up a Virtual Environment

It’s recommended to use a virtual environment to manage dependencies.

```bash
# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
# On macOS/Linux
source venv/bin/activate
# On Windows
venv\Scripts\activate
```

### 3. Install Dependencies

Install the necessary dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Configure AWS CLI

The scripts use `boto3` to interact with AWS services, so you’ll need to configure your AWS credentials. Run the following command to set up the AWS CLI:

```bash
aws configure
```

This command will prompt you to enter your:

* **AWS Access Key ID**
* **AWS Secret Access Key**
* **Default region name**
* **Default output format**

These credentials allow the scripts to access your AWS account securely.

### 5. Run the Script

Run any script directly using Python:

```bash
python script_name.py
```

---

## LICENSE

This repository is licensed under the MIT License. See the [LICENSE](/LICENSE) file for more details.
