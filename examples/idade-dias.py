import datetime
import math

qtdDaysBetweenYear = 0
qtdDaysBeforeBorn = 0
qtdDaysAfterPresentYear = 0
qtdDays = 0

print('---Sua idade em dias---')
birthday = input('digite seu aniversário(dd/mm/yyyy): ').split('/')
day, month, year = birthday

currentDate = datetime.date.today()
currentYear = int(currentDate.strftime('%Y'))
currentMonth = int(currentDate.strftime('%m'))
currentDay = int(currentDate.strftime('%d'))

# Qtd days before born
for monthItem in range(1, (int(month))):
    # print(monthItem)
    if(int(year) % 2 != 0):
        if(monthItem % 2 == 0):
            qtdDaysBeforeBorn += 31

        elif(monthItem == 2):
            if((currentYear % 4 == 0) and (currentYear % 100 != 0) and (currentYear % 400 != 0)):
                qtdDaysBeforeBorn += 29
            else:
                qtdDaysBeforeBorn += 28

        else:
            qtdDaysBeforeBorn += 30

    else:

        if(monthItem % 2 == 0):
            qtdDaysBeforeBorn += 30

        elif(monthItem == 2):
            if((currentYear % 4 == 0) and (currentYear % 100 != 0) and (currentYear % 400 != 0)):
                qtdDaysBeforeBorn += 29
            else:
                qtdDaysBeforeBorn += 28

        else:
            qtdDaysBeforeBorn += 31
else:
    qtdDaysBeforeBorn += int(day)

# Qtd days after year init
for monthItem in range(1, currentMonth):
    if(currentYear % 2 != 0):

        if(monthItem % 2 == 0):
            qtdDaysAfterPresentYear += 31

        elif(monthItem == 2):
            if((currentYear % 4 == 0) and (currentYear % 100 != 0) and (currentYear % 400 != 0)):
                qtdDaysAfterPresentYear += 29
            else:
                qtdDaysAfterPresentYear += 28

        else:
            qtdDaysAfterPresentYear += 30

    else:
        if(monthItem % 2 == 0):
            qtdDaysAfterPresentYear += 30

        elif(monthItem == 2):
            if((currentYear % 4 == 0) and (currentYear % 100 != 0) and (currentYear % 400 != 0)):
                qtdDaysAfterPresentYear += 29
            else:
                qtdDaysAfterPresentYear += 28

        else:
            qtdDaysAfterPresentYear += 31
else:
    qtdDaysAfterPresentYear += currentDay

# Counting each year
for yearItem in range(int(year), currentYear):
    if((yearItem % 4 == 0) and (yearItem % 100 != 0) and (yearItem % 400 != 0)):
        qtdDaysBetweenYear += 366
    else:
        qtdDaysBetweenYear += 365

qtdDays = qtdDaysBetweenYear - qtdDaysBeforeBorn + qtdDaysAfterPresentYear

print("Dias entre " + year + " e " + currentYear.__str__() +
      ": " + qtdDaysBetweenYear.__str__())
print("Total de dias antes de você nascer: " + qtdDaysBeforeBorn.__str__())
print("Totais de dias passados neste ano: " + qtdDaysAfterPresentYear.__str__())
print("Total de dias vivo: " + qtdDays.__str__())
