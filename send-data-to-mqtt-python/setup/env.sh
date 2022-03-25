sudo apt-get update
sudo apt-get install -y python3.7
sudo apt-get install -y python3-pip
sudo apt-get install -y libpq-dev python-dev
sudo apt-get install -y postgresql-client
sudo timedatectl set-timezone Asia/Kolkata
pip3 install virtualenv
sudo apt-get install -y curl

chmod -R 777 setup/*.sh

python3.7 -m virtualenv venv
source venv/bin/activate
pip install -r setup/requirements.txt
pip3 install -r setup/requirements.txt
