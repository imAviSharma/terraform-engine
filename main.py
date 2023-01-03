import os
from terraform import init

directory = "Avinash"
parent_dir = "/home/avinash/Downloads/python/tf-generator"

init.makeDir(directory, parent_dir)
init.init(os.path.join(parent_dir, directory))
