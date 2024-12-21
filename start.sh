if [ -z $SOURCE_CODE ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Soutick09/rg.git /rg
else
  echo "Cloning Custom Repo from $SOURCE_CODE "
  git clone $SOURCE_CODE /rg
fi
cd /rg
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 main.py
