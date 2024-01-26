import os
import sys
from mlflow_project import logger
import yaml
from pathlib import Path

def read_yaml(yamlfilepath:Path):
    '''
    Description: This function reads the yaml file and return its content

    Args: File path with Yaml file name

    Error: Value error when file is empty

    Result: Content of the YAML file

    '''
    try:
        with open(yamlfilepath) as yaml_file:
            yaml_content =yaml.safe_load(yaml_file)
            logger.info('Yaml file {yamlfilepath} Read Successfully')
    except Exception as e:
        raise e

def create_directories(directorypath:list, verbose = True):
    '''
    Decriptions: Creates directories for the path passed

    Args: Path of the directory

    Error: Raises None
    '''
    for path in directorypath:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f'Directory created at: {directorypath}')



