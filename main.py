# -*- coding: utf-8 -*-
import json
import os.path
import subprocess  # 從路徑(字串)執行程式碼
import logging  # 取代 print()
import platform  # 辨認作業系統
# import pickle # TODO: 評估此必要性

META_DATA = json.load(open(os.path.join(".", "meta.json"), "r"))
CODE_DIRECTORY = os.path.join(".", "code")
DOWNLOAD_DIRECTORY = os.path.join(".", "software")
if platform.system() == "Windows":
    RUN_PYTHON_COMMAND = META_DATA['settings']['windows']
elif platform.system() == "Darwin":  # macOS
    RUN_PYTHON_COMMAND = META_DATA['settings']['macOS']


def main():
    for software in META_DATA['softwares']:
        logging.warning(software['name'])
        codePath = os.path.join(CODE_DIRECTORY, software['codePath'])
        downloadPath = os.path.join(
            DOWNLOAD_DIRECTORY, *software['downloadPath'])
        # * 代表將list去除掉 "[", "]"
        # some_function(*[parameter1, parameter2]) == some_function(parameter1, parameter2)
        subprocess.run(RUN_PYTHON_COMMAND + [codePath, downloadPath])


if __name__ == "__main__":
    main()
