interfase= [{'interface': 'Ethernet0', 'ip': '1.1.1.1', 'status': 'up'},
        {'interface': 'Ethernet1', 'ip': '2.2.2.2', 'status': 'down'},
        {'interface': 'Serial0', 'ip': '3.3.3.3', 'status': 'up'},
        {'interface': 'Serial1', 'ip': '4.4.4.4', 'status': 'up'}]
print('общее количество интерфейсов: ', len(interfase))
print('название, ip-адрес и статус, соответствующую второму интерфейсу в списке: ', interfase[1])
print('статус последнего интерфейса в списке: ', interfase[-1]['status'])
print('status' in interfase[-1])
print('notes' in interfase[0])
#interfase[0]['notes'] = 'need to reset'
interfase[0].setdefault('notes','need to reset')
print(interfase[0])
interfase.append({'interface':'Ethernet','ip': '3.3.3.3','status':'down'})
print(interfase)
interfase[2]['ip'] ='3.3.3.4'
print(interfase[2]['ip'])
print(interfase[0].pop('notes'))
print(interfase[0])
interfase[3]['status'] = 'down'
print(interfase[3])
del interfase[3]['status']
print(interfase[3])



