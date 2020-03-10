# Serverless Video Metadata Extractor

Media processing applications often need information about what’s in audio and video files before they can do anything with those files. Video providers use it to get technical metadata about video codecs, frame rates, audio channels, duration, and more.

  ![Miztiik Serverless Video Metadata Extractor](images/serverless-video-metadata-processor-arch-00.png)

  Follow this article in **[Youtube](https://www.youtube.com/c/ValaxyTechnologies)**

1. ## Prerequisites

    This demo, instructions, scripts and cloudformation template is designed to be run in `us-east-1`. With few modifications you can try it out in other regions as well(_Not covered here_).

    - AWS CLI pre-configured - [Get help here](https://youtu.be/TPyyfmQte0U)
    - **Optional** AWS CDK Installed & Configured - [Get help here](https://www.youtube.com/watch?v=MKwxpszw0Rc)

1. ## ⚙️ Setting up the environment

    - Get the application code

        ```bash
        git clone https://github.com/miztiik/fargate-chat-app.git
        cd fargate-chat-app
        ```

1. ## 🚀 Deployment using AWS CDK

    If you have AWS CDK installed you can close this repository and deploy the stack with,

    ```bash
    # If you DONT have cdk installed
    npm install -g aws-cdk

    # Make sure you in root directory
    cd fargate-chat-app
    source .env/bin/activate
    pip install -r requirements.txt
    ```

    The very first time you deploy an AWS CDK app into an environment _(account/region)_, you’ll need to install a `bootstrap stack`, Otherwise just go aheadand   deploy using `cdk deploy`

    ```bash
    cdk bootstrap
    cdk deploy *
    ```

1. ### Method 1: Using AWS CDK

      If you have AWS CDK installed you can close this repository and deploy the stack with,

        ```bash
        # If you DONT have cdk installed
        npm install -g aws-cdk

        git clone https://github.com/miztiik/security-automation-remediate-weak-s3-policy.git
        cd security-automation-remediate-weak-s3-policy
        source .env/bin/activate
        pip install -r requirements.txt
        ```

      The very first time you deploy an AWS CDK app into an environment _(account/region)_, you’ll need to install a `bootstrap stack`, Otherwise just go aheadand   deploy using `cdk deploy`

        ```bash
        cdk bootstrap
        cdk deploy
        ```

1. ### Method 2: Using AWS CloudFormation

      Look for the cloudformation template here: `cdk.out` directory, _From the CLI,_

        ```sh
        aws cloudformation deploy \
            --template-file ./cdk.out/security-automation-remediate-weak-s3-policy.template.json \
            --stack-name "MiztiikAutomationStack" \
            --capabilities CAPABILITY_IAM
        ```

1. ## 🔬 Test the app

    The `cdk deploy` command should provide you the application load balancer url to access the web app. _You can get the same from cloudformation outputs or in the ALB page.

    You should be seeing something like this,
    ![Server Chat App using Fargate](images/miztiik-fargate-chat-app_00.png)

1. ## Testing the solution

    Upload a video to S3 Bucket, Wait for the video metadata results or check the cloudatch logs

    ![miztiik_security_automation_remediate_weak_s3_policy](images/miztiik_security_automation_remediate_weak_s3_policy_failure_00.png)

1. ## 🧹 CleanUp

    If you want to destroy all the resources created by the stack, Execute the below command to delete the stack, or _you can delete the stack from console as well_

    - _Any other customer resources, you have created for this demo_

    ```bash
    # Delete from cdk
    cdk destroy

    # Delete the CF Stack
    aws cloudformation delete-stack \
        --stack-name "MiztiikAutomationStack" \
        --region "${AWS_REGION}"
    ```

    This is not an exhaustive list, please carry out other necessary steps as maybe applicable to your needs.

## 👋 Buy me a coffee

Buy me a coffee ☕ through [Paypal](https://paypal.me/valaxy), _or_ You can reach out to get more details through [here](https://youtube.com/c/valaxytechnologies/about).

### 📚 References

1. [Source Repo](https://aws.amazon.com/blogs/media/running-mediainfo-as-an-aws-lambda-function)

1. [Stackoverflow oserror-libmediainfo-so](https://stackoverflow.com/questions/52516828/oserror-libmediainfo-so-0-cannot-open-shared-object-file-no-such-file-or-dire)

### ℹ️ Metadata

**Level**: 300
