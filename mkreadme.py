import os
import glob
from scripts.mktree import DisplayablePath
from pathlib import Path
from jinja2 import Template, Environment, FileSystemLoader

# Get Repo name
dir_path = os.path.dirname(os.path.realpath(__file__))
repo_name = os.path.basename(os.path.normpath(dir_path)).replace("_"," ")

# Load template file
file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)
template = env.get_template('README.md.j2')

# Get technos paths
techno_paths = []
techno_paths = glob.glob('./datasets/*/')

# Get datasets
datasets = []
for path in techno_paths:
  for dataset in os.listdir(path):
    techno = os.path.basename(os.path.normpath(path))
    datasets.append(dict({'techno': techno, 'dataset': dataset, 'path': path+dataset}))

#for dataset in datasets:
#  print(dataset['dataset'])

# Create tree list of current directory
tree = []
paths = DisplayablePath.make_tree(Path('.'), criteria=lambda path: True if path.name not in ('.git',  '__pycache__', '.gitkeep') else False)
for path in paths:
  tree.append(path.displayable())

# Render from template
output = template.render(repo_name=repo_name,ndatasets=len(datasets),datasets=datasets,tree=tree)
print(output)
