#!/usr/bin/env bash
# Sets up web server for deployment of web_static
sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx
sudo mkdir -p data/web_static/releases/test
sudo mkdir -p data/web_static/shared
sudo touch data/web_static/releases/test/index.html
sudo echo "<html>\n\t<head></head>\n\t<body>Testing</body>\n</html>" | sudo tee /data/web_static/releases/test/index.html
sudo mkdir -p data/web_static/current
sudo ln -sfn data/web_static/releases/test data/web_static/current
sudo chown -hR ubuntu:ubuntu /data
# editing nginx
find='^\tlocation / {'
replace='\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n\n\tlocation / {'
sudo sed -i  "s@${find}@${replace}@" /etc/nginx/sites-available/default
sudo service nginx restart
exit 0
