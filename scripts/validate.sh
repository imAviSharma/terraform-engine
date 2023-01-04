#!/bin/bash

cd $1

echo "Starting the Terraform validate process..."
# Terraform validate
terraform validate
echo "Terraform validate process complete."

