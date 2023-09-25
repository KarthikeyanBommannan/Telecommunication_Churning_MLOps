import os
import argparse
import yaml
import logging


def read_params(config_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config
def main(config_path, datasource):
    config = read_params(config_path)
    print(config)


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    default_file_path = os.path.join("config", "params.yaml")
    args.add_argument("--config", default = default_file_path)
    args.add_argument("datasource", default = None)
    
    parsed_args = args.parse_args()
    main(config_path=parsed_args.config, datasource=parsed_args.datasource)
    read_params()
    
    
    # print(parsed_args.config,parsed_args.datasource)
    
 