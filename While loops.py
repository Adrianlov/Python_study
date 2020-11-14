#i = 1
#while i <= 5:
 #   print('G' *i)
  #  i = i + 1
#print("Done")

numar_secret = 9
ghiceste_numaratoarea = 0
ghiceste_limita = 3
while ghiceste_numaratoarea < ghiceste_limita:
    ghiceste = int(input('Ghiceste: '))
    ghiceste_numaratoarea += 1
    if ghiceste == numar_secret:
        print('Ai castigat')
        break
else:
    print('Ai pierdut')
