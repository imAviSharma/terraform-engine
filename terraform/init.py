import os
import subprocess


def makeDir(directory, parent_dir):
    path = os.path.join(parent_dir, directory)

    try:
        os.makedirs(path, exist_ok=True)
        print("Directory '%s' created successfully" % directory)
    except OSError as error:
        print("Directory '%s' can not be created" % directory)


def start(path:str,directory:str,cloud_provider:str):
    try:
        providerTemplate = open('terraform/templates/provider.tf.txt', 'r')
        provider = open(os.path.join(path, "provider.tf"), 'w')
        provider.write(providerTemplate.read())
        provider.write("\n")
        # Kubernetes
        kubernetes_required_provider = open('terraform/templates/Kubernetes/required_providers.tf.txt', 'r')
        provider.write(kubernetes_required_provider.read())
        provider.write("\n\n")

        if cloud_provider=="aws":
            aws_required_provider = open('terraform/templates/AWS/required_providers.tf.txt', 'r')
            provider.write(aws_required_provider.read())
            provider.write("\n  }\n}\n")
            aws_provider = open('terraform/templates/AWS/provider.tf.txt', 'r')
            provider.write(aws_provider.read())
            provider.write("\n")
            aws_required_provider.close()
            print("Added aws...")

        elif cloud_provider=="gcp":
            gcp_required_provider = open('terraform/templates/GCP/required_providers.tf.txt', 'r')
            provider.write(gcp_required_provider.read())
            provider.write("\n  }\n}\n")
            gcp_provider = open('terraform/templates/GCP/provider.tf.txt', 'r')
            provider.write(gcp_provider.read())
            provider.write("\n")
            gcp_required_provider.close()
            print("Added gcp...")

        elif cloud_provider=="azure":
            azure_required_provider = open('terraform/templates/GCP/required_providers.tf.txt', 'r')
            provider.write(azure_required_provider.read())
            provider.write("\n  }\n}\n")
            azure_provider = open('terraform/templates/Azure/provider.tf.txt', 'r')
            provider.write(azure_provider.read())
            provider.write("\n")
            azure_required_provider.close()
            print("Added azure...")
        else:
            provider.write("\n}\n }\n")
            print("No cloud provider")

        kubernetes_provider_config = open('terraform/templates/Kubernetes/provider.tf.txt')
        provider.write(kubernetes_provider_config.read())
        provider.close()
        providerTemplate.close()
    except Exception as e:
        print("Error ",e.args)

    subprocess.run(["./scripts/init.sh", directory])
    print("init completed")