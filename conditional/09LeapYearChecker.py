year =int(input("Enter a year: ").strip())

leap=""

if year%100==0 and year%400!=0:
  leap=" not"
elif year%4!=0:
  leap=" not"

print(f"{year} is{leap} a leap year.")