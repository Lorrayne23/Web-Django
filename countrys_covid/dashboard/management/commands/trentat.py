import csv

from django.core.management.base import BaseCommand, CommandError
from dashboard.models import Country,Cases # new
from config.settings import ENTRIES_DATAFILE



class Command(BaseCommand):
    help = 'Seed the database with country covid p data'

    def handle(self, *args, **kwargs):
        try:
            
                with open(ENTRIES_DATAFILE)as csv_file:
                    reader = csv.DictReader(csv_file, delimiter=',')
                    csv_data = [line for line in reader]
                    aux =[]
                    aux2 = []

                    for item in csv_data:
                        country = item.get('country')
                        confirmed = int(item.get('confirmed'))
                        deaths = int(item.get('deaths'))
                        recovered = int(item.get('recovered'))
                        obj1 = Country(
                            country_name=country
                        )
                        obj1.save()

                        obj2 = Cases(
                            country=obj1,
                            confirmed=confirmed,
                            deaths=deaths,
                            recovered=recovered,
                        )
                        obj2.save()
                        
                



        except FileNotFoundError:
            raise CommandError(f'File "{ENTRIES_DATAFILE}" does not exist')

        self.stdout.write(self.style.SUCCESS('Successfully seeded database.'))