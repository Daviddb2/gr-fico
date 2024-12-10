import matplotlib.pyplot

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho']
valores = [105235, 107697, 110256, 109236, 108859, 109986]

matplotlib.pyplot.plot(meses, valores)
matplotlib.pyplot.ylim(100000, 120000)
matplotlib.pyplot.title('Faturamento')
matplotlib.pyplot.xlabel('Meses')
matplotlib.pyplot.show()