#!/usr/bin/env bash

virtualenv -p python3 venv

source venv/bin/activate

pip install -r requirements.txt

git clone https://github.com/alexandrevicenzi/Flex themes/Flex
git clone --recursive https://github.com/getpelican/pelican-plugins
