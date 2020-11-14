#'''if aplicant has high income AND good credit
#       Eligible foar loan'''

has_high_income = False
has_good_credit = False
has_criminal_record = False

if has_high_income and not has_criminal_record:
    print("Eligible for loan")
elif has_criminal_record and not has_good_credit:
    print("Imi pare rau")
else:
    print("Ce cauti aici bai? ")

#AND: Amandoua trebuie sa fie adevarate
#OR: Una trebuie sa fie adevarata
#NOT: O elimina