from PickStudent import PickStudent
from unittest import TestCase
from pprint import pprint
import filecmp
import pdb
import os

class TestPickStudent(TestCase):
	@classmethod
	def setUpClass(self):
		self.ps = PickStudent()
		studentsCSV = self.ps.get_students('./alunos.csv')
		studentsJSON = self.ps.get_students_json('./alunos.json')
		studentsXSLX = self.ps.get_students_xlsx('./alunos.xlsx')
		studentsDB = self.ps.get_students_sqlite('./dojo2.db')
		self.student_lists = [studentsCSV, studentsJSON, studentsXSLX, studentsDB]

	def setUp(self):
		self.ps.reset()

	def test_correct_number_of_students(self):
		for students in self.student_lists:
			self.ps.reset()
			self.assertEqual(len(students), 20, "Número errado de alunos")

	def test_has_students(self):
		for students in self.student_lists:
			self.ps.reset()
			self.assertIn(['1', 'Alice Brenner'], students, "Alice tem que estar dentro")
			self.assertIn(['21', 'Yang Ricardo'], students, "Yang tem que estar dentro")

	def test_doesnt_have_students(self):
		for students in self.student_lists:
			self.ps.reset()
			self.assertNotIn(['22', 'Temer'], students, "Temer tem que estar fora")
			self.assertNotIn(['23', 'Lula'], students, "Lula tem que estar fora")

	def test_picks_one_student(self):
		for students in self.student_lists:
			self.ps.reset()
			pick = self.ps.pick_one(students)
			self.assertGreater(int(pick[0]), 0, "Número do aluno deve ser maior que 0")
			self.assertGreater(len(pick[1]), 10, "Nome do aluno deve ser mais longo que 10 caracteres")

	def test_picks_two_different_students(self):
		for students in self.student_lists:
			self.ps.reset()
			for i in range(int(len(students)/2)):
				pick1 = self.ps.pick_one(students)
				pick2 = self.ps.pick_one(students)

				if pick1 == pick2:
					pdb.set_trace()

				self.assertNotEqual(pick1, pick2, "Duas seleções tem que sempre ser diferentes")

	def test_only_picks_someone_once(self):
		for students in self.student_lists:
			self.ps.reset()
			pick1 = self.ps.pick_one(students)
			for i in range(len(students)-1):
				pick2 = self.ps.pick_one(students)
				self.assertNotEqual(pick1, pick2, "Nunca deve selecionar o mesmo aluno mais de uma vez")

	def test_running_out_of_students(self):
		for students in self.student_lists:
			self.ps.reset()
			for i in range(len(students)):
				pick = self.ps.pick_one(students)
			self.assertRaises(IndexError, self.ps.pick_one, students)

	def test_saves_log_and_all_differ(self):
		files = []
		index = 0
		for students in self.student_lists:
			self.ps.reset()
			for i in range(len(students)-1):
				pick = self.ps.pick_one(students)
			file = f'./log{index}.csv'
			self.ps.save_picks(file)
			files.append(file)
			size = os.path.getsize(file)
			self.assertGreater(size, 0)
			index += 1

		self.assertFalse(filecmp.cmp(files[0],files[1]))
		self.assertFalse(filecmp.cmp(files[0],files[3]))
		self.assertFalse(filecmp.cmp(files[1],files[2]))
