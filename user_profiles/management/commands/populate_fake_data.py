# user_profiles/management/commands/populate_fake_data.py
from django.core.management.base import BaseCommand
from faker import Faker
from user_profiles.models import UserProfile
import json
from django.core.files import File
from io import BytesIO
from PIL import Image
from django.contrib.auth.hashers import make_password



fake = Faker()

class Command(BaseCommand):
    help = 'Populate the database with fake user profiles'

    def handle(self, *args, **kwargs):
        for _ in range(25):
            user = UserProfile(
                name=fake.name(),
                designation=fake.job(),
                company=fake.company(),
                about=fake.text(),
                areas_of_interest=json.dumps([]),  # Empty list initially
                display_picture=fake.image_url(),
                password = make_password(fake.password())
            )
            
            user.save()
