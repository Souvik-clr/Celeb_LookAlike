# to store all the repetative functions used all over project
import yaml
import os
import logging

# to read yaml file(which contain all necessaryfile location)
def read_yaml(path_to_file: str) -> dict:
    with open(path_to_file) as yaml_file:
        content = yaml.safe_load(yaml_file)
    return content

# to create directory
def create_directory(dirs: list):
    for dir_path in dirs:
        os.makedirs(dir_path, exist_ok=True)
        logging.info(f"Directory is create at {dir_path}")