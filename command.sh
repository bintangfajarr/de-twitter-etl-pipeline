sudo apt-get update
sudo apt install python3-pip
sudo apt install -y python3-venv python3-full
python3 -m venv venv
source venv/bin/activate
pip install tweepy pandas python-dotenv s3fs apache-airflow