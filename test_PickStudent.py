from PickStudent import PickStudent
from unittest import TestCase
from pprint import pprint
import pdb

class TestPickStudent(TestCase):
	@classmethod
	def setUpClass(self):
		self.ps = PickStudent()
		self.students = self.ps.get_students('./alunos.csv')

	def setUp(self):
		self.ps.reset()

	def test_correct_number_of_students(self):
		self.assertEqual(len(self.students), 23, "Número errado de alunos")

	def test_has_students(self):
		self.assertIn(['1', 'Alice Brenner'], self.students, "Alice tem que estar dentro")
		self.assertIn(['11', 'Luis Fernando'], self.students, "Luis tem que estar dentro")

	def test_doesnt_have_students(self):
		self.assertNotIn(['22', 'Temer'], self.students, "Temer tem que estar fora")
		self.assertNotIn(['23', 'Lula'], self.students, "Lula tem que estar fora")

'''
	def test_picks_one_student(self):
		pick = self.ps.pick_one(self.students)
		self.assertGreater(int(pick[0]), 0, "Número do aluno deve ser maior que 0")
		self.assertGreater(len(pick[1]), 10, "Nome do aluno deve ser mais longo que 10 caracteres")

	def test_picks_two_different_students(self):
		for i in range(int(len(self.students)/2)):
			pick1 = self.ps.pick_one(self.students)
			pick2 = self.ps.pick_one(self.students)

			if pick1 == pick2:
				pdb.set_trace()

			self.assertNotEqual(pick1, pick2, "Duas seleções tem que sempre ser diferentes")

	def test_only_picks_someone_once(self):
		pick1 = self.ps.pick_one(self.students)
		for i in range(len(self.students)-1):
			pick2 = self.ps.pick_one(self.students)
			self.assertNotEqual(pick1, pick2, "Nunca deve selecionar o mesmo aluno mais de uma vez")

	def test_running_out_of_students(self):
		for i in range(len(self.students)):
			pick = self.ps.pick_one(self.students)
		self.assertRaises(IndexError, self.ps.pick_one, self.students)
'''