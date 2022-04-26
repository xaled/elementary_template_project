#!/bin/sh

pip install --upgrade --no-cache-dir -r requirements.txt;
pip install --upgrade --no-cache-dir gunicorn;
gunicorn -w4 -b 0.0.0.0:5000 $MODULE_NAME:app