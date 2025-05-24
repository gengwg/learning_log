Start a new app:

```sh
$ python manage.py startapp users
$ tree users/
users/
├── admin.py
├── apps.py
├── __init__.py
├── migrations
│   └── __init__.py
├── models.py
├── tests.py
└── views.py

2 directories, 7 files
```

Activate the virtual env:

```bash
source ll_env/bin/activate
```

Start the server:

```bash
python manage.py runserver
```

Start Django shell:

```sh
$ python manage.py shell
>>> from django.contrib.auth.models import User
>>> User.objects.all()
<QuerySet [<User: ll_admin>, <User: abc>]>
>>> for user in User.objects.all():
...     print(user.username, user.id)
...
ll_admin 1
abc 2
```

Migrate the database:

```sh
$ python manage.py makemigrations learning_logs
It is impossible to add a non-nullable field 'owner' to topic without specifying a default. This is because the database needs something to populate existing rows.
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit and manually define a default value in models.py.
Select an option: 1
Please enter the default value as valid Python.
The datetime and django.utils.timezone modules are available, so it is possible to provide e.g. timezone.now as a value.
Type 'exit' to exit this prompt
>>> 1
Migrations for 'learning_logs':
  learning_logs/migrations/0004_topic_owner.py
    + Add field owner to topic

$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, learning_logs, sessions
Running migrations:
  Applying learning_logs.0004_topic_owner... OK
```
