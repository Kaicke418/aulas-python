# MANIPULAÇÃO DOS EVENTOS
# JOGO LABIRINTO

import pygame

# Inicializa o Pygame
pygame.init()



# COMENTE O CÓDIGO, EXPLIQUE COM SUAS PALAVRAS O QUE ESTA OCORRENDO EM CADA ESTRUTURA DO 
# CÓDIGO IVERIFIQUE, O QUE OCORRE. 
# CONSULTE A BIBLIOTECA -> https://www.pygame.org/docs/



#configuração da tela do jogo

largura, altura = 400, 400

#cria uma tela 400x400
tela = pygame.display.set_mode((largura, altura))
#dá o título da janela do jogo
pygame.display.set_caption("Labirinto")

#define cores para o fundo, para o player e para o labirinto
preto = (0, 0, 0)
branco = (255, 255, 255)
vermelho = (255, 0, 0)

#aqui define o tamanho de cada elemento do labirinto e aonde vai ter chão e paredes 
tamanho_celula = 40
#matriz, definição de chão e parede
labirinto = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 0, 0, 1, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

#faz o player preencher direto o próximo quadrado
x, y = 1 * tamanho_celula, 1 * tamanho_celula
velocidade = 40

#função para mostrar as coisas na tela
def desenhar_labirinto():
    #looping para percorrer a lista labirinto
    for linha in range(len(labirinto)):
        #looping para percorrer as colunas do labirinto
        for coluna in range(len(labirinto[linha])):
            #variavel declarada para uma condição que caso se o numero for igual a 1 vai pintar de preto, caso 0 pintar de branco
            cor = preto if labirinto[linha][coluna] == 1 else branco
            pygame.draw.rect(tela, cor, (coluna * tamanho_celula, linha * tamanho_celula, tamanho_celula, tamanho_celula))

#looping para manter o jogo rodando
executando = True
while executando:
    #script para parar o looping quando o jogador clicar em sair
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False

    #verifica se teclas estão sendo pressionadas
    teclas = pygame.key.get_pressed()
    #condções que verificam se algumas teclas em especificos foram tocadas, e se alguma foi executa uma ação
    if teclas[pygame.K_LEFT]:
        #faz o player se movimentar para esquerda
        novo_x = x - velocidade
        #verifica se o player não está tentando ultrapassar uma parede no eixo x indo para esquerda, e se estiver tentando para o player
        if labirinto[y // tamanho_celula][novo_x // tamanho_celula] == 0:
            x = novo_x
    if teclas[pygame.K_RIGHT]:
        #faz o player se movimentar para direita
        novo_x = x + velocidade
        #verifica se o player não está tentando ultrapassar uma parede no eixo x indo para direita, e se estiver tentando para o player
        if labirinto[y // tamanho_celula][novo_x // tamanho_celula] == 0:
            x = novo_x
    if teclas[pygame.K_UP]:
        #faz o player se movimentar para cima
        novo_y = y - velocidade
        #verifica se o player não está tentando ultrapassar uma parede no eixo y indo para cima, e se estiver tentando para o player
        if labirinto[novo_y // tamanho_celula][x // tamanho_celula] == 0:
            y = novo_y
    if teclas[pygame.K_DOWN]:
        #faz o player se movimentar para baixo
        novo_y = y + velocidade
        #verifica se o player não está tentando ultrapassar uma parede no eixo y indo para baixo, e se estiver tentando para o player
        if labirinto[novo_y // tamanho_celula][x // tamanho_celula] == 0:
            y = novo_y

    #deixa o fundo branco, usando como parâmetro a váriavel declarada antes
    tela.fill(branco)

    #chama a função que mostra as coisas na tela
    desenhar_labirinto()
    #desenha o player
    pygame.draw.rect(tela, vermelho, (x, y, tamanho_celula, tamanho_celula))

    #atualiza um pedaço da tela do monitor
    pygame.display.flip()

    #é um framepoint
    pygame.time.Clock().tick(10)

#fecha o pygame
pygame.quit()
