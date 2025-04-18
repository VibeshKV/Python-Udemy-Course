cardno = input('Enter card number')
lastDigits = cardno[15::]
four= '*' * 4 + ''
dispno = four * 3 + lastDigits
print(dispno) 
