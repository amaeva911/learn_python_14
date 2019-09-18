import ephem

mars = ephem.Mars('1988/12/16') # получение позиции планеты на указанную дату
print(mars) # так выводится объект. Тип и ячейка памяти?

const = ephem.constellation(mars) # в каком созвездии была планета в позиции на дату
print(const)