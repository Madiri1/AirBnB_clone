#!/usr/bin/python3

import uuid

# Defines all common attributes/methods for other classes
class BaseModel:
	def __init__(self, id):
		self.id = str(uuid.uuid4())


