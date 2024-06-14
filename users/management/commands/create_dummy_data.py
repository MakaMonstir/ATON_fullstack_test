from django.core.management.base import BaseCommand
from faker import Faker
from users.models import User, Client

class Command(BaseCommand):
    help = 'Create dummy data for Users and Clients'

    def handle(self, *args, **kwargs):
        faker = Faker()

        # Create dummy users
        for _ in range(10):
            user = User.objects.create_user(
                username=faker.user_name(),
                email=faker.email(),
                password='password',
                full_name=f"{faker.first_name()} {faker.last_name()}"
            )
            self.stdout.write(self.style.SUCCESS(f'Successfully created user {user.username}'))

        # Create dummy clients
        for _ in range(50):
            client = Client.objects.create(
                account_number=faker.bban(),
                last_name=faker.last_name(),
                first_name=faker.first_name(),
                middle_name=faker.first_name(),
                birth_date=faker.date_of_birth(),
                inn=faker.ssn(),
                responsible_person=User.objects.order_by('?').first(),
                status='Не в работе'
            )
            self.stdout.write(self.style.SUCCESS(f'Successfully created client {client.account_number}'))
