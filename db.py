import shelve


class Account:
	def __init__(self, user, pw):
		self.user = user
		self.pw = pw

	def create(self, name, msg):
		pass


	def login(self):
		s = shelve.open('database.db')
		name = s[self.user]['name']
		msg = s[self.user]['msg']
		s.close()


		print(f'\nName: {name}')
		print(f'Message: {msg}\n')


	def user_check(self):
		s = shelve.open('database.db')
		exist = self.user in s
		s.close()
		if exist:
			return True


	def pw_check(self):
		s = shelve.open('database.db')
		password = s[self.user]['pw']
		s.close()
		if self.pw == password:
			return True
