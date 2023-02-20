print('Você acorda em uma casa escura.\n A chuva castiga a velha madeira do casarão e o vidro da janela ao seu lado.')
print('Sua perna dói. Você olha para ela?')
choice = input('[S/N] > ')

if choice in ['S', 's']:
    print('Você olha para sua perna. Na verdade, você olha para sua carne dilacerada. O sangue te faz ter vertigem.')   
elif choice in ['N', 'n']:
    print('Você decide não olhar para sua perna.')
else:
        print('Opção invalida. Escolha entre [S] e [N]')

print('Você não se lembra do que aconteceu.')

