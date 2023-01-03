import os
import subprocess


def makeDir(directory, parent_dir):
    path = os.path.join(parent_dir, directory)

    try:
        os.makedirs(path, exist_ok=True)
        print("Directory '%s' created successfully" % directory)
    except OSError as error:
        print("Directory '%s' can not be created" % directory)


def init(path):
    providerTemplate = open('terraform/templates/provider.tf.txt', 'r')
    provider = open(os.path.join(path, "provider.tf"), 'w')
    provider.write(providerTemplate.read())
    provider.close()
    providerTemplate.close()
    subprocess.run(["terraform", "init"])
    print("init completed")
