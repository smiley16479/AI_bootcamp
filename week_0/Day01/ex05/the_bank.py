class Account(object):
	
	ID_COUNT = 1
	
	def __init__(self, name, **kwargs):
		self.id = self.ID_COUNT
		self.name = name
		self.__dict__.update(kwargs)
		# if hasattr(self, 'value'):
		# 	self.value = 0
		Account.ID_COUNT += 1
	
	def transfer(self, amount):
		self.value += amount


# class Bank:
# 	def __init__(obj):
# 		if str(type(obj)) == 
# 	if hasattr(a, 'property'): # check if object passed has certin attribute

class Bank(object):
	"""The bank"""
	def __init__(self):
		self.account = []

	def add(self, account):
		if self.valid_account(account):
			print('compt valide')
			self.account.append(account)
		else:
			print('compt invalide')

	def transfer(self, origin, dest, amount):
		"""
			@origin: int(id) or str(name) of the first account
			@dest:
			int(id) or str(name) of the destination account
			@amount: float(amount) amount to transfer
			@return
			True if success, False if an error occured
		"""
		for i in self.account:
			if i.name == origin or i.id == origin:
				print('compte trouve')
				if i.value >= amount:
					for j in self.account:
						print('compte 2 trouve')
						if j.name == origin or j.id == origin:
							i.value -= amount
							j.value += amount
							return True
		return False

	def rename_attribute(object_, old_attribute_name, new_attribute_name):
	    setattr(object_, new_attribute_name, getattr(object_, old_attribute_name))
	    delattr(object_, old_attribute_name)

	def fix_account(self, account):
		""" fix the corrupted account @account: int(id) or str(name) of the account @return True if success, False if an error occured"""
		

	def valid_account(self, account):
		check = [1,0,0,0,0]
		if isinstance(account, Account):
			if len(account.__dict__) % 2 == 1 :
				for i in account.__dict__.keys():
					if i[0] == 'b':
						check[0] = 0
					elif i.startswith("zip") or i.startswith("addr"):
						check[1] = 1
					elif i == 'name':
						check[2] = 1
					elif i == 'id':
						check[3] = 1
					elif i == 'value':
						check[4] = 1
				for i in check:
					if i == False:
						return False
				return True
		return False

	# Security means checking if the Account is:
	# • the right object
	# • that it is not corrupted
	# • and that it has enough money
	# How do we define if a bank account is corrupted?
	# • It has an even number of attributes.
	# • It has an attribute starting with b.
	# • It has no attribute starting with zip or addr. • It has no attribute name, id and value.
	# Check out the dir function.