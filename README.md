for run locally execute these:

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Then go to this address on browser:
```
http://127.0.0.1:8000/
```

For add product or manage users first create superuser with this command:
```bash
python manage.py createsuperuser
```

The Login in this page:
```
http://127.0.0.1:8000/admin
```