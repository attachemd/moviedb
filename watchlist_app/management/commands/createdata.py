import random

from django.core.management import BaseCommand
from faker import Faker

from django.contrib.auth.models import User
from core.models import WatchListModel, StreamPlatformModel, ReviewModel

from colorama import Fore, Back, Style

fakegen = Faker()


def populate(N=5):
    user = User.objects.get(username__iexact='me')
    for _ in range(20):
        # create new movie entry
        platform = StreamPlatformModel.objects.get_or_create(
            name=fakegen.company(),
            website=fakegen.url(),
            about=fakegen.sentence(),
        )[0]

    for _ in range(N):
        stream_platform_id = random.randint(1, 20)
        platform = StreamPlatformModel.objects.filter(
            id=stream_platform_id
        )
        # print(Fore.BLACK + Back.YELLOW + "platform[0] :" + Style.RESET_ALL)
        # print(platform[0])
        # create new movie entry
        movie = WatchListModel.objects.get_or_create(
            title=fakegen.company(),
            platform=platform[0],
            website=fakegen.url(),
            storyline=fakegen.sentence(),
            active=fakegen.boolean()
        )[0]

    for _ in range(N):
        watch_list_id = random.randint(1, 20)
        watchlist = WatchListModel.objects.filter(
            id=watch_list_id
        )[0]
        rating = random.randint(1, 5)
        # print(Fore.BLACK + Back.YELLOW + "platform[0] :" + Style.RESET_ALL)
        # print(platform[0])
        # create new movie entry
        if watchlist.num_rating == 0:
            watchlist.avg_rating = rating
        else:
            watchlist.avg_rating = (watchlist.avg_rating + rating)/2

        watchlist.num_rating = watchlist.num_rating + 1
        watchlist.save()
        review = ReviewModel.objects.get_or_create(
            rating=rating,
            user=user,
            watchlist=watchlist,
            description=fakegen.text(),
            active=fakegen.boolean()
        )[0]


def create_super_user():
    user = User.objects.create_superuser(
        username="me",
        password="1234",
        email="me@example.com"
    )
    user.save()


def populate_user(N=5):
    User.objects.create_user('sli', password='sli', email='sli@example.com')
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


class Command(BaseCommand):
    help = "Command information"

    def handle(self, *args, **kwargs):
        print('populating script')
        create_super_user()
        populate(20)
        populate_user()
        print('populating complete')
