import os
import sys
import django
from django.core.management import call_command

# Adjust the path to your Django project's settings
DJANGO_PROJECT_PATH = "E:\.Code\Python\DjangoWebsite"
sys.path.append(DJANGO_PROJECT_PATH)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')


def load_fixtures():
    django.setup()

    fixtures_folder = os.path.join(DJANGO_PROJECT_PATH, "mainapp", "fixtures")

    if not os.path.exists(fixtures_folder):
        print("Fixtures folder doesn't exist.")
        return

    fixture_files = [f for f in os.listdir(fixtures_folder) if f.endswith(".json")]

    if not fixture_files:
        print("No fixture files found.")
        return

    print(f"Loading {len(fixture_files)} fixture files...")

    for fixture_file in fixture_files:
        fixture_path = os.path.join(fixtures_folder, fixture_file)
        call_command("loaddata", fixture_path)

    print("Fixtures loaded successfully.")


if __name__ == "__main__":
    load_fixtures()
