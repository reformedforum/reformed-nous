#reformed-nous

reformed nous. Check out the project's [documentation](http://monty5811.github.io/reformed-nous/).

# Prerequisites
- [virtualenv](https://virtualenv.pypa.io/en/latest/)
- [postgresql](http://www.postgresql.org/)
- [redis](http://redis.io/)
- [travis cli](http://blog.travis-ci.com/2013-01-14-new-client/)
- [heroku toolbelt](https://toolbelt.heroku.com/)

# Initialize the project
Create and activate a virtualenv:

```bash
virtualenv env
source env/bin/activate
```
Install dependencies:

```bash
pip install -r requirements/local.txt
```
Create the database:

```bash
createdb reformed_nous
createuser
```
Initialize the git repository

```
git init
git remote add origin git@github.com:monty5811/reformed-nous.git
```

Migrate the database and create a superuser:
```bash
python reformed_nous/manage.py migrate
python reformed_nous/manage.py createsuperuser
```

Run the development server:
```bash
python reformed_nous/manage.py runserver
```
