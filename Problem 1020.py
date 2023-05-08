# problem is Age in Days :
# int type value input
days = int(input())
# decision use days and 365 so 1year
years = int(days/365)
days = days % 365  # stor day
# month = 30day
month = int(days/30)
days = days % 30  # update day
print(years, "ano(s)")
print(month, "mes(es)")
print(days, "dia(s)")
# solve this problem
