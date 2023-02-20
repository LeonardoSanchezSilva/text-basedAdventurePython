print('Você acorda em uma casa escura.\n A chuva castiga a velha madeira do casarão e o vidro da janela ao seu lado.')
print('Sua perna dói. Você olha para ela?')

choice = ''
valid_choice = False
while not valid_choice:
    choice = input('[S/N] > ')
    if choice.lower() == 's':
        print('Você olha para sua perna. Na verdade, você olha para sua carne dilacerada. O sangue te faz ter vertigem.')
        valid_choice = True
    elif choice.lower() == 'n':
        print('Você decide não olhar para sua perna.')
        valid_choice = True
    else:
        print('Opção inválida. Escolha entre [S] e [N]')
        valid_choice = False

print('Você não se lembra do que aconteceu.')
print('A sala continua escura, exceto pelos clarões dos trovões. \n Você pode ir para: Leste, Oeste, Norte, Sul')
print('Por onde você segue?')

roomchoice = ''
valid_roomchoice = False
while not valid_roomchoice:
    roomchoice = input(' > ')
    if roomchoice.lower() == 'leste':
        print('Leste.')
        valid_roomchoice = True
    elif roomchoice.lower() == 'oeste':
        print('Oeste.')
        valid_roomchoice = True
    elif roomchoice.lower() == 'norte':
        print('Norte.')
        valid_roomchoice = True
    elif roomchoice.lower() == 'sul':
        print('Sul.')
        valid_roomchoice = True
    else:
        print('Opção inválida. Escolha entre Leste, Oeste, Norte e Sul.')
        valid_roomchoice = False
print('Você se arrasta até o ' + roomchoice)