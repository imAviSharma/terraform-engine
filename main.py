import os
from terraform import init
from dotenv import load_dotenv
load_dotenv()

print("Enter directory name (fileName)::",end=" ")
directory = input()
parent_dir =os.environ.get("parent_dir")

print("Enter cloud vender name (aws,gcp,azure) :: ",end=" ")
cloud_provider = input().lower()

init.makeDir(directory, parent_dir)
init.start(os.path.join(parent_dir, directory),directory,cloud_provider)