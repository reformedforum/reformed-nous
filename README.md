# reformed-nous

*a reformed brain*

See [here](http://reformed.tech/2016/07/developing-a-common-brain-for-our-systems/) for more details.

**Note:** this is a very early stage project and there are likely to be a large number of breaking changes before we hit v1.

## Setting up a Local Environment

### Prerequisites
- [virtualenv](https://virtualenv.pypa.io/en/latest/)
- [postgresql](http://www.postgresql.org/)

### Setup
Clone the repo:
```bash
git clone https://github.com/reformedforum/reformed-nous.git
```

Create and activate a virtualenv:

```bash
cd reformed-nous
python3 -m venv venv # you may need to add --without-pip and then install pip on some versions of Ubuntu
. venv/bin/activate
```
Install dependencies:

```bash
pip install -r requirements/local.txt
```
Create the database:

```bash
createdb reformed_nous
createuser --interactive -P
# setup a "nous" user with the password "reformed-nous", or set DATABASE_URL with your user, pass and db
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

Now open localhost:8000 in your web browser to get started.
The admin panel can be found at `/admin/` where you can add some dummy data to get started.

### Running test suite

```bash
py.test reformed_nous
```
