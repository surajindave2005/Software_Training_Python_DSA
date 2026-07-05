year = int(input())

if (year%400 == 0) or (year%4==0 and year%100 != 0):
    print(f"{year} It's leap year");
else:
    print(f"{year} It's not leap year");
1
