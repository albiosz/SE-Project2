#! /bin/bash

# 1. Build the application locally, since building in the dockerfile is not working
# the .jar file from ./target directory is used

# Push the image to the ECR repository
aws ecr get-login-password --region eu-central-1 | docker login --username AWS --password-stdin 182399689800.dkr.ecr.eu-central-1.amazonaws.com
docker build -t currency-converter-grpc .
docker tag currency-converter-grpc:latest 182399689800.dkr.ecr.eu-central-1.amazonaws.com/currency-converter-grpc:latest
docker push 182399689800.dkr.ecr.eu-central-1.amazonaws.com/currency-converter-grpc:latest

# Update the service to use the new image
aws ecs update-service --cluster se-project --service currency-converter-grpc --force-new-deployment

# Wait for deployment to complete
aws ecs wait services-stable --cluster se-project --services currency-converter-grpc

# Get public IP address of the new service
TASK_ARNS=$(aws ecs list-tasks --cluster se-project --service-name currency-converter-grpc --query "taskArns" --output text)
ENI_IDS=$(aws ecs describe-tasks --cluster se-project --tasks $TASK_ARNS --query "tasks[].attachments[].details[?name=='networkInterfaceId'].value" --output text)
for ENI_ID in $ENI_IDS; do
  IP=$(aws ec2 describe-network-interfaces --network-interface-ids $ENI_ID --query "NetworkInterfaces[].Association.PublicIp" --output text)
  echo "New deployed service is available at: $IP:8081"
done
