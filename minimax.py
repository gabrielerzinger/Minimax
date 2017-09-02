import math

def minimax(profundidade, indice, jogador, placar, h):
#Função minimax para o jogo Maximizer x Minimizer que define a pontuação maxima que
#o Maximizer pode obter começando se ambos jogarem de forma ótima.
	if (profundidade == h): # Se a profundidade chegou ao fim
		return placar[indice] # Retorna o placar deste indice

	if(jogador == 1): #Se é o jogador A ( maximizer )
		return max(minimax(profundidade+1, indice*2, 0, placar, h),  #Maximo entre ir pra Dir/Esq
					minimax(profundidade+1, indice*2 + 1, 0, placar, h))

	else: #Se é o jogador B ( minimizer )
		return min(minimax(profundidade+1, indice*2, 1, placar, h), #Mininmo entre ir pra Dir/Esq
					minimax(profundidade+1, indice*2 + 1, 1, placar, h))


placar = [3, 5, 2, 9, 12, 5, 23, 23] # Arvore
n = 8 # Numero de elementos
altura = (math.log(n)/math.log(2))
res = minimax(0,0,1,placar, altura)
s = 'O melhor valor alcancado por A eh ' + str(res)
print(s)
