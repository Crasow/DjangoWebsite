import os
import django
from django.core.management import call_command


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

# Initialize Django settings.
django.setup()

# Specify the path to your fixtures folder
fixtures_folder = 'mainapp/fixtures'

# Get a list of all fixture files in the folder
fixture_files = [file for file in os.listdir(fixtures_folder) if file.endswith('.json')]

# Loop through each fixture file and load it into the database
for fixture_file in fixture_files:
    fixture_path = os.path.join(fixtures_folder, fixture_file)
    
    # Load the fixture using the loaddata management command
    call_command('loaddata', fixture_path)

print(f"Loaded {len(fixture_files)} fixtures into the database.")
