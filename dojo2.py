import random

def non_random_choice(list):
	return random.choice(list)

def programar(algo):
	tecnicas = ['algoritmos', 'IA', 'um chatbot', 'um framework', 'alguma tecnologia']
	print(f'* TODO * Resolver {algo} com {non_random_choice(tecnicas)}')

def usar_ferramenta_para_resolver(algo):
	deve_ser_resolvido_com_programacao = str
	if isinstance(algo, deve_ser_resolvido_com_programacao):
		programar(algo)
	else:
		print('Não deve/ pode ser resolvido com programação... mas talvez parte possa ser ajudado?')

def resolver_todos(problemas):
	for problema in problemas:
		usar_ferramenta_para_resolver(problema)

def solucionar(problemas):
	return resolver_todos(problemas)

def aplicacao():
	problemas = input("Quais seus problemas? ").split()
	return solucionar(problemas)

if __name__ == '__main__':
	aplicacao()

'''
- programar -> ferramenta
- solução <- problema
- aplicação <- uso da ferramenta para resolver um problema
'''
