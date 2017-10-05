from random import randrange
import csv
from pprint import pprint

class PickStudent:
	already_picked = []	

	def reset(self):
		'''comeca a pegar alunos do zero'''
		self.already_picked = []

	def get_students(self, file):
		self.already_picked = list(range(21))
		self.already_picked.append(['1', 'Alice Brenner'])
		self.already_picked.append(['11','Luis Fernando'])
		return self.already_picked
		'''Retorna uma lista de alunos'''

	def pick_random(self, list):
		'''escolhe um aluno aleatoriamente'''


	def pick_one(self, list):
		'''escolhe um aluno aleatorio, exceto dos já escolhidos,
		dando um erro caso não existam mais alunos disponíveis'''
		return [42, 0]


'''Abaixo está o código para utilizar essa classe e escolher um aluno por vez'''
if __name__ == '__main__':
	ps = PickStudent()
	alunos = ps.get_students('./alunos.csv')
	user_input = None
	count = 1
	while not user_input and count < len(alunos):
		print(ps.pick_one(alunos)[1])
		count += 1
		user_input = input("Next...")
