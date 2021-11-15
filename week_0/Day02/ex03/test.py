

class File(object):
	def __init__(self, file_name, method):
		self.file_obj = open(file_name, method)
	def __enter__(self):
		return self
	def __exit__(self, type, value, traceback):
		print("Exception has been handled")
		self.file_obj.close()
		# return True

	def print_str(self):
		print("hello")

with File('demo.txt', 'w') as opened_file:
	# opened_file.undefined_function()
	opened_file.print_str()
	# pass

# Output: Exception has been handled