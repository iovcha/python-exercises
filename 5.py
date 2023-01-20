seconds = int(input(''))
days_seconds = 86400
hours_seconds = 3600
minutes_seconds = 60
days = seconds / days_seconds
seconds = seconds % days_seconds
hours = seconds / hours_seconds
seconds = seconds % hours_seconds
minutes = seconds / minutes_seconds
seconds = seconds % minutes_seconds
print('%d : %02d : %02d :%02d' % (days, hours, minutes,  seconds))
