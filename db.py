import shelve


class Account:
	def __init__(self, user, pw):
		self.user = user
		self.pw = pw


	def create(self):
		name = input('Create a name: ')
		msg = input('Create a message: ')

		# write username, pass, name, msg
		s = shelve.open('db/database.db')
		s[self.user] = {'pw': self.pw, 'name': name, 'msg': msg}
		s.close()
		print('Account successfully created')


	def login(self):
		s = shelve.open('db/database.db')
		name = s[self.user]['name']
		msg = s[self.user]['msg']
		s.close()

		print(f'Name: {name}')
		print(f'Message: {msg}')


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


	def delete(self):
		s = shelve.open('db/database.db')
		del s[self.user]
		s.close()
		print('Account successfully deleted')


	def update(self, option):
		s = shelve.open('db/database.db')
		copy = s[self.user]

		if option == 1:
			password = input('New Password: ')
			copy['pw'] = password
			s[self.user] = copy
			print('Password Updated')
		elif option == 2:
			name = input('New Name: ')
			copy['name'] = name
			s[self.user] = copy
			print('Name Updated')
		else:
			msg = input('New Message: ')
			copy['msg'] = msg
			s[self.user] = copy
			print('Message Updated')

		s.close()


	def show(self):
		s = shelve.open('db/database.db')
		for i in s:
			print(f'User: {i}')
		s.close()
