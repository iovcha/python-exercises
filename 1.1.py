#7. Счет за телефон
#conversations = 50
#messages = 50
#cost = 15.00
#additional_minute_costs = 0.25
#additional_message_costs = 0.15
#bills_include = 0.44
#rate = 0.05
conversations = float(input("Kоличество израсходованных за месяц минут разговора : "))
messages = float(input("Kоличество израсходованных за месяц смс-сообщений: "))
if conversations <= 50 and messages > 50:
    cost = 15.00 + ((messages - 50) * 0.15)
elif conversations > 50 and messages <= 50:
    cost = 15.00 + ((conversations - 50) * 0.25)
else:
    cost = 15.00
if conversations > 50 and messages > 50:
    cost1 = (conversations - 50) * 0.25 + (messages - 50) * 0.15
elif (conversations - 50) < 0 and messages > 50:
    cost1 =(messages - 50) * 0.15
elif (messages - 50) < 0 and conversations > 50:
    cost1 = (conversations - 50) * 0.25
else:
    cost1 = 0
if cost1 <= 0:
    print("Дополнительнве минуты  и сообщения не использовались")
    print("Базовуя сумма тарификации = %.2f. " % cost)
    print("налог на поддержку кол-центров 911 в размере $0,44,")
    print("Cуммa отчислений кол-центрам = %.2f." % ((cost + cost1) * 0.05))
    print("Итоговуя сумма к оплате $%.2f." % ((cost + cost1) + (cost + cost1) * 0.05))


else:
    print("Базовуя сумма тарификации = %.2f" % cost)
    print("Сумма за дополнительные минуты и сообщения =  %.2f." % cost1)
    print("налог на поддержку кол-центров 911 в размере $0,44,")
    print("Cуммa отчислений кол-центрам = %.2f." % ((cost + cost1) * 0.05))
    print("Итоговуя сумма к оплате $%.2f." % ((cost + cost1) + (cost + cost1) * 0.05))







