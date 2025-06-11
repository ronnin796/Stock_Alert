from django.core.management.base import BaseCommand
from inventory.utils.alert import check_and_alert

class Command(BaseCommand):
    help = 'Check stock and send alerts'

    def handle(self, *args, **kwargs):
        alerts = check_and_alert()
        self.stdout.write(self.style.SUCCESS(f'Sent {len(alerts)} alerts.'))
