import os
from pathlib import Path
import logging #to log all the information

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')#only msgs with severity level of 'INFO' or higher would be processed
#format displays the actual time when log msg was created and the log msg

project_name="textSummarizer"

list_of_files=[ #here we write CI/CD related YAML files
    ".github/workflows/.gitkeep", #.github, then folder, then a file to track changes
    f"src/{project_name}/__init__.py", #whenever we do installation of local packages, it will look for the constructor file...the constructor file folder is considered as the local package
    f"src/{project_name}/components/__init__.py",#inside components folder we have another constructor file
    f"src{project_name}/utils/common.py" #inside common file we write all out utilities
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",#helps in local package setup
    "research/trails.ipynb"#helps in notebook experiments

]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)

    if filedir!= "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")

        if(not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
            with open(filepath,'w') as f:
                pass #I only wanna create file
            logging.info(f"Creating empty file {filepath}")
        else:
            logging.info(f"{filename} already exists")
           






