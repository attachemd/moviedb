import os
import django
from faker import Faker

from watchlist_app.models import Movie

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'moviedb.settings')

django.setup()

fakegen = Faker()


def populate(N=5):
    for entry in range(N):
        # create fake data for entry
        fake_url = fakegen.url()
        fake_about = fakegen.lorem()
        fake_name = fakegen.company()

        # create new movie entry
        movie = Movie.objects.get_or_create(name=fake_name, website=fake_url, about=fake_about)[0]


if __name__ == '__main__':
    print('populating script')
    populate(20)
    print('populating complete')
