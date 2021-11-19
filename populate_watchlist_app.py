import os
import django
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'moviedb.settings')
django.setup()

from django.contrib.auth.models import User
from watchlist_app.models import Movie

fakegen = Faker()


def populate(N=5):
    for _ in range(N):
        # create fake data for entry
        fake_url = fakegen.url()
        fake_about = fakegen.sentence()
        fake_name = fakegen.company()
        fake_bool = fakegen.boolean()

        # create new movie entry
        movie = Movie.objects.get_or_create(name=fake_name, website=fake_url, about=fake_about, active=fake_bool)[0]


def create_super_user():
    user = User.objects.create_superuser(username="me", password="1234", email="me@example.com")
    user.save()


def populate_user(N=5):
    for _ in range(N):
        name = fakegen.name()
        first_name = name.split(' ')[0]
        last_name = ' '.join(name.split(' ')[-1:])
        username = first_name[0].lower() + last_name.lower().replace(' ', '')
        user = User.objects.create_user(username, password=username)
        user.first_name = first_name
        user.last_name = last_name
        user.is_superuser = False
        user.is_staff = False
        user.email = username + "@" + last_name.lower() + ".com"
        user.save()


if __name__ == '__main__':
    print('populating script')
    create_super_user()
    populate(20)
    populate_user()
    print('populating complete')
