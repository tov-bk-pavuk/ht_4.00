from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


from faker import Faker

# from polls.models import User  # Старый кастомный User bp моделей приложения

fake = Faker()


class Command(BaseCommand):

    def add_arguments(self, parser):

        parser.add_argument('amount', type=int, choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                            help=u'amount - Количество пользователей')

    def handle(self, *args, **options):
        amount = options['amount']
        a = [User(i, username=fake.name(), email=fake.email(),
                  password=fake.password()) for i in range(amount)]
        User.objects.all().delete()  # Команда стирает предыдущие записи для целей тестирования.
        User.objects.bulk_create(a)
