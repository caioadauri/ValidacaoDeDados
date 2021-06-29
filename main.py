from datetime import datetime, timedelta
from datas_br import DatasBr


cadastro = DatasBr()
print(cadastro.dia_semana())
print(cadastro)

'''
hoje = datetime.today()
hoje_formatada = hoje.strftime("%d/%m/%Y %H:%M")
print(hoje)
print(hoje_formatada)
'''