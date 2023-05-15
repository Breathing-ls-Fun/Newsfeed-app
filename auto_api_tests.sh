#!/bin/bash

source env/bin/activate

cd /var/lib/jenkins/workspace/nf-app

echo "Running News and Weather API Tests"

pytest

echo "Finished Running News and Weather API Tests"