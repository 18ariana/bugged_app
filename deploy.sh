pip install -U pip
pip install -r requirements-base.txt
pip install -r requirements-extra.txt
./manage.py migrate
./manage.py loaddata fixture.json
echo 'Deploy DONE'
