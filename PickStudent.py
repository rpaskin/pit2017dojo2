from random import randrange
import csv
from pprint import pprint

class PickStudent:
	already_picked = []

	def reset(self):
		self.already_picked = []

	def get_students(self, file):
		'''
		Veja https://docs.python.org/3/library/csv.html
		'''
		with open(file, newline='') as csvfile:
				return list(csv.reader(csvfile))

	def pick_random(self, list):
		which = randrange(len(list))
		pick = list[which]
		return pick

	def pick_one(self, list):
		# pprint(self.already_picked)
		pick = self.pick_random(list)
		max_tries = len(list)*100	# prevents running forever; unlikely but it could happen since it's random
		while pick in self.already_picked and max_tries > 0:
			# pprint(f"Ops! Already picked {pick}")
			pick = self.pick_random(list)
			max_tries -= 1

		if max_tries > 0:
			# pprint(f"Aha! Picked {pick}")
			self.already_picked.append(pick)
			return pick
		else:
			raise IndexError




if __name__ == '__main__':
	ps = PickStudent()
	alunos = ps.get_students('./alunos.csv')
	user_input = None
	count = 1
	while not user_input and count < len(alunos):
		print(ps.pick_one(alunos)[1])
		count += 1
		user_input = input("Next...")