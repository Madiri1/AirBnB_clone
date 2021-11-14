#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime

# Defines all common attributes/methods for other classes
class BaseModel:
	""" initialise a new BaseModel

	Args:
		*args (any): Unused
		**kwargs (dict): key/value pairs of attributes
	"""

	def __init__(self, *args, **kwargs):
		self.id = str(uuid())
		self.created_at = datetime.today
		self.updated_at = datetime.today

