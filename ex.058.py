from random import randint
tentativas = 0
print('Sou seu computador...')
print('Acabei de oensar em um número entre 0 e 10')
print('Será que você consegue adivinhar qual foi? ')
palpite = int(input('Qual seu palpite? '))
tentativas += 1
resposta = randint(0, 10)
while palpite != resposta:
      if palpite > resposta:
            palpite = int(input('Menos... Tente mais uma vez: '))
            tentativas += 1
      elif palpite < resposta:
            palpite = int(input('Mais... Tente mais uma vez: '))
            tentativas += 1
      if palpite == resposta:
            print(' ')
            print('Finalmente em! Com {} tentativa(s)'.format(tentativas))
