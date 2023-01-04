import os
from terraform import init

from dotenv import dotenv_values

print("Enter directory name (fileName)::", end=" ")
directory = input()
parent_dir = os.environ.get("parent_dir") or ""

print("Enter cloud vender name (aws,gcp,azure) ::", end=" ")
cloud_provider = input().lower()

init.start(parent_dir, directory, cloud_provider)
