#!/bin/bash

python3 -m venv "$django_venv"

source "$django_venv/bin/activate"
echo "Virtual environment '$django_venv' has been created and activated. Requirements have been installed."
pip install -r requirement.txt

deactivate

