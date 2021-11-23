import factory
from django.utils import timezone
from faker import Faker
from datetime import datetime
from core.models import WatchListModel

faker = Faker()


class WatchListFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = WatchListModel

    title = faker.company()
    storyline = faker.sentence()
    website = faker.url()
    active = faker.boolean()
    # created = datetime.now().strftime("%A, %d. %B %Y %I:%M%p")
    # created = datetime.now().strftime("YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ]")
    created = timezone.now()
