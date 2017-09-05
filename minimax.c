#include <stdio.h>
#include <math.h>
#define INF 0x3f3f3f3f
#define max(a, b) ((a) > (b) ? (a) : (b))
#define min(a, b) ((a) < (b) ? (a) : (b))

int minimax(int profundidade, int indice, int jogador, int *placar, int h){
	if(profundidade == h) return placar[indice];
	if(jogador == 1){
		return max(minimax(profundidade+1, indice*2, 0, placar, h), 
				   minimax(profundidade+1, indice*2+1, 0, placar, h));
	}
	else {
		return max(minimax(profundidade+1, indice*2, 1, placar, h),
				   minimax(profundidade+1, indice*2+1, 1, placar, h));
	}
}

int main(){
	int placar[] = {3, 5, 2, 9, 12, 5, 23, 23};
	int n = 8, altura = ceil(log(n)/log(2));
	int res = minimax(0,0,1,placar,altura);
	printf("O melhor valor alcancado por A eh %d\n",res);
	return 0;
}