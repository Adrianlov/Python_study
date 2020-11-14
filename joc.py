comanda = ""
while comanda != "quit":
   comanda = input("> ").lower()
   if comanda == "start":
       print("Masina a pornit")
   elif comanda == "stop":
       print("Masina sa oprit")
   elif comanda == "help":
       print(''' 
       Start - Masina porneste
       Stop - Masina se opreste
       quit - A iesi
       ''')
   else:
       print('Nu intaleg asta')


