year=int(input("Enter year:"))
if year % 100 == 0:
    if year % 400 == 0:
        print('yes ,it is a leap year')
    else:
        print('no ,not a leap year')
elif year %4 == 0:
    print('yes ,it is a leap year')
else:
    print('no ,not a leap year')