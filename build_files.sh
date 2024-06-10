# build_files.sh
apt-get update
apt-get install -y python3-pip python3-venv
python3 -m venv myenv
source myenv/bin/activate
pip install -r requirements.txt
