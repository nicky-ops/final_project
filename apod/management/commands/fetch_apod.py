'''
Management command to fetch the last 30 days of APOD data
'''
from django.core.management.base import BaseCommand
from apod.views import get_apod_data
from datetime import date, timedelta

class Command(BaseCommand):
    help = 'Fetches the last 30 days of APOD data'
    def handle(self, *args, **options):
        end_date = date.today()
        start_date = end_date - timedelta(days=30)
        current_date = start_date

        while current_date <= end_date:
            apod = get_apod_data(current_date.isoformat())
            if apod:
                self.stdout.write(self.style.SUCCESS(f"Successfully fetched APOD data for {current_date}"))
            else:
                self.stdout.write(self.style.ERROR(f"Failed to fetch APOD data for {current_date}"))

            current_date += timedelta(days=1)