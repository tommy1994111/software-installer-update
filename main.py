# -*- coding: utf8 -*-
import json
import os.path
import subprocess # run code from path
import logging # replace print()
import platform # identify OS
# import pickle # TODO: Evaluate that if necessary

META_DATA = json.load(open(os.path.join(".", "meta.json"), "r"))
CODE_DIRECTORY = os.path.join(".", "code")
DOWNLOAD_DIRECTORY = os.path.join(".", "software")
if platform.system() == "Windows":
    RUN_PYTHON_COMMAND = META_DATA['settings']['windows']
elif platform.system() == "Darwin": # macOS
    RUN_PYTHON_COMMAND = META_DATA['settings']['macOS']

def main():
    for software in META_DATA['softwares']:
        logging.warning(software['name'])
        codePath = os.path.join(CODE_DIRECTORY, software['codePath'])
        downloadPath = os.path.join(
            DOWNLOAD_DIRECTORY, *software['downloadPath'])
            # * means "take off the []"
        subprocess.run(RUN_PYTHON_COMMAND + [codePath, downloadPath])

if __name__ == "__main__":
    main()
