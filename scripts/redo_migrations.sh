mysqladmin -u root drop coc
mysqladmin -u root create coc
./manage.py migrate
./manage.py createsuperuser
