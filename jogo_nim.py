def menu():
	c = 0
	while c == 0:
		try:
			print("Bem-vindo ao jogo do NIM! Escolha:")
			print(" ")
			print("1 - para jogar uma partida isolada")
			c = int(input("2 - para jogar um campeonato "))
			if c != 1 and c != 2:
				c = 0
		except ValueError:
			c = 0

	if c==1:
		print("\nVoce escolheu uma partida isolada!")
		partida()
	else:
		print("\nVoce escolheu um campeonato!")
		campeonato()

def main():
	menu()

def computador_escolhe_jogada(n,m):
	if n<=m:
		computador_tira=n
	else:
		computador_tira = n%(m+1)

	if computador_tira == 1:
		print("O computador tirou uma peça.")
	else:
		print("O computador tirou",computador_tira,"peças.")

	return computador_tira


def usuario_escolhe_jogada(n,m):
	def msg_error():
		print("\nOops! Jogada inválida! Tente de novo.\n")

	while True:
		try:
			usuario_tira = int(input("Quantas peças você vai tirar? "))
			if usuario_tira < 1 or usuario_tira > n or usuario_tira > m:
				msg_error()
			elif usuario_tira==1:
				print("Você tirou uma peça.")
				break
			else:
				print("Voce tirou",usuario_tira,"peças.")
				break
		except ValueError:
			msg_error()

	return usuario_tira

def partida():
	computador=True
	n = int(input("Quantas peças? "))
	m = int(input("Limite de peças por jogada? "))

	if n%(m+1) > 0:
		print("\nComputador começa!\n")
		computador=True
	else:
		print("\nVoce começa!\n")
		computador=False

	while n>0:
		if computador:
			n=n-computador_escolhe_jogada(n,m)
			if n<=0:
				print("Fim do jogo! O computador ganhou!")
				return 1
			computador=False
		else:
			n=n-usuario_escolhe_jogada(n,m)
			if n<=0:
				print("fim do jogo! O usuário ganhou!")
				return 0
			computador=True

		if n==1:
			print("Agora resta apenas uma peça no tabuleiro.\n")
		else:
			print("Agora resta apenas",n,"peça no tabuleiro.\n")

def campeonato():
	computador=0
	usuario=0
	for x in range(1,4):
		print("\n**** Rodada",x,"****\n")
		win=partida()
		if win==0:
			usuario=usuario+1
		else:
			computador=computador+1
	print("\n**** Final do campeonato! ****\n")
	print("Placar: Você",usuario,"X",computador,"Computador")

main()
