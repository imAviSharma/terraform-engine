#!/bin/bash

cd $1

echo "Starting the Terraform init process..."
# Initialize Terraform
terraform init
echo "Terraform init process complete."


