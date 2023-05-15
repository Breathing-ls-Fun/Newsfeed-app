#!/bin/bash

source env/bin/activate

cd /var/lib/jenkins/workspace/nf-app

echo "Running Tests"

python3 manage.py test
coverage run --source='.' manage.py test

echo "Finished Running Tests"

echo "Generating Covarage Report"

coverage report

echo "Finished Generating Covarage Report"