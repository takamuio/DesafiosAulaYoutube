celcius = float(input('Digite graus celcius: '))
fahr = (celcius * 9/5) + 32
print('{:.2f} °C é equivalente a {:.2f} °F'.format(celcius, fahr))

fahrenheit = float(input('Digite graus Fahrenheit: '))
celc = (fahrenheit - 32) * 5/9
print('{:.2f} °F é equivalente a {:.2f} °C'.format(fahrenheit, celc))
