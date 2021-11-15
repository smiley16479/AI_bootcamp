import csv
#Pas fini les check et les exceptions sont incompletes
class CsvReader(object):

	def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
		if filename == None:
			raise ValueError('filename not provided')
			return None
		self.filename = filename
		self.sep = sep
		self.header = header
		self.skip_top = skip_top
		self.skip_bottom = skip_bottom

	def __enter__(self):
		self.file_obj = open(self.filename, 'r')
		return self

	def __exit__(self, type, value, traceback):
		print("Exception has been handled")
		self.file_obj.close()
		return True

	def getdata(self):
		""" Retrieves the data/records from skip_top to skip bottom.Returns:nested list (list(list, list, ...)) representing the data."""
		print(self.getdata.__name__)
		num_lines = sum(1 for line in self.file_obj) # count file lines
		print("num_lines :", num_lines)
		self.file_obj.seek(0)
		csvreader = csv.reader(self.file_obj, delimiter=self.sep)
		# header = next(csvreader)
		# print("header(getdata) :",header)
		rows = []
		i = 0
		last_column_nb = 0
		try:
			for row in csvreader:
				if i >= self.skip_top and i < (num_lines - self.skip_bottom):
					rows.append(row)
					if last_column_nb != 0:
						print(row)
						for content in row:
							if content == '':
								print("bac")
								raise ValueError('corrupted csv file')
						if last_column_nb != len(row):
							print("bac")
							raise ValueError('corrupted csv file')
						else:
							last_column_nb = len(row)
					else:
						last_column_nb = len(row)
				i += 1
		except ValueError as e:
			print(e)
			quit()
		print("row hors boucle :", row)
		print(rows)

	def getheader(self):
		""" Retrieves the header from csv file.Returns:list: representing the data (when self.header is True).None: (when self.header is False)."""
		if self.header:# and csv.Sniffer().has_header(self.filename.read(1024)):
			self.file_obj.seek(0)
			header = self.file_obj.readline()
			print("header(getheader) :", header)
			return header

# from csvreader import CsvReader 

if __name__ == "__main__":
	with CsvReader('../resources/bad.csv', skip_top=5, skip_bottom=1) as file:
		data = file.getdata()
		header = file.getheader()

# from csvreader import CsvReader

# if __name__ == "__main__":
# 	with CsvReader('../resources/bad.csv') as file:
# 		if file == None:
# 			print("File is corrupted")