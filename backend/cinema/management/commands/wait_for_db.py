"""
WAIT FOR DB
"""

import time

from psycopg2 import OperationalError as PsycopgError
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand

class Command(BaseCommand):
	""

	def handle(self, *args, **options):
		self.stdout.write("WAITING FOR DB TO BE READY ....")
		db_up = False
		while db_up == False:
			try:
				self.check(databases=['default'])
				db_up = True
			except (PsycopgError, OperationalError):
				self.stdout.write("DB NOT READY YET")
				time.sleep(2.5)
		self.stdout.write("DB READY :]")