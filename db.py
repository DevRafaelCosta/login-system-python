import shelve


class Account:
	def __init__(self, user, pw):
		self.user = user.lower()
		self.pw = pw

	def create(self):
		name = input('Create a name: ')
		msg = input('Create a message: ')

		# write username, pass, name, msg
		s = shelve.open('db/database.db')
		s[self.user] = {'pw': self.pw, 'name': name, 'msg': msg}
		s.close()
		print('Account successfully created\n')

	def login(self):
		s = shelve.open('db/database.db')
		name = s[self.user]['name']
		msg = s[self.user]['msg']
		s.close()

		print(f'\nName: {name}')
		print(f'Message: {msg}\n')


	def user_check(self):		
		s = shelve.open('db/database.db')
		exist = self.user in s
		s.close()
		if exist:
			return True


	def pw_check(self):
		s = shelve.open('db/database.db')
		password = s[self.user]['pw']
		s.close()
		if self.pw == password:
			return True
