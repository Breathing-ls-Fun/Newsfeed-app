#!/bin/bash

sudo cp -rf app.conf /etc/nginx/sites-available/app
chmod 755 /var/lib/jenkins/workspace/nf-app-45600

sudo ln -s /etc/nginx/sites-available/app /etc/nginx/sites-enabled
sudo nginx -t

sudo systemctl start nginx
sudo systemctl restart nginx
sudo systemctl enable nginx

echo "Nginx has been started"

sudo systemctl status nginx