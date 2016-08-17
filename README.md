# reformed-nous

*a reformed brain*

See [here](http://reformed.tech/2016/07/developing-a-common-brain-for-our-systems/) for more details.

**Note:** this is a very early stage project and there are likely to be a large number of breaking changes before we hit v1.

We are still in the planning stages - this repo is more of a conversation starter than anything. We are planning on fleshing out a solid set of requirements and a plan to make it easy for people to contribute. Any help is very welcome! Please feel free to jump into the [issues](https://github.com/reformedforum/reformed-nous/issues) and contribute.

## Overall Vision

This application will provide a structure for theological resources. The big entities are people, books, and Scripture references, since these items drive much of the conversation within the Reformed theological community generally and at [Reformed Forum](http://reformedforum.org), specifically. Nearly every podcast episode or blog post references people, books, or Scripture references. At the same time, it’s hard to find resources given any one of these entities. Consider a few use cases:

* You’re studying Philippians 2:5–11 and are looking for resources that deal with the subject. You’d like to listen to podcasts and sermons, read blog posts, journal articles, or books that reference these verses.
* You’re listening to a podcast episode and someone mentioned a book. You’d like to buy that book and join in an online discussion about it. Perhaps you’re also interested in downloading a study guide to help you lead a discussion group on the book.
* Someone suggested you look into reading John Murray’s *Redemption Accomplished and Applied*. You search our site and find several places where you can buy new and used copies. You also notice a podcast episode devoted to the book, other books by John Murray, and an online discussion group currently reading the book together.
* You’d like to subscribe to an RSS feed for all of Sinclair Ferguson’s books, posts, conference addresses, and sermons.

We envision a database and application that allows us to structure all of Reformed Forum’s resources as well as trusted resources from around the web. In a way, this would be the brain behind a next-generation hybrid between [Monergism.com](http://www.monergism.com) and [SermonAudio.com](http://www.sermonaudio.com).

This application will also provide an API so that other applications may use the exposed data and functionality of this system.

## Concrete Requirements

**TODO**
 - 
 - 

## Data Schema

**TODO**

On a first pass, we should be able to import all the people and resources from Reformed Forum and be able to link out to related books, other resources and relevant scripture references.

## Application Stack

 - The django based api currently in this repo is more of a conversation starter than anything else. The language/framework used should be determined by those who will be contributing - open an issue and let's talk about it if you are interested!

## Far Future Ideas

 - Automatically index audio files (speech to text)
 - ???

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
