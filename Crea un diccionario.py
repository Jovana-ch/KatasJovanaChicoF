# Crea un diccionario llamado planet con los datos propuestos

planet = {
    'name': 'Mars',
    'moons': 2
}
# Muestra el nombre del planeta y el número de lunas que tiene.

print(f'{planet["name"]} has {planet["moons"]} moons')
# Agrega la clave circunferencia con los datos proporcionados previamente

planet['circumference (km)'] = {
    'polar': 6752,
    'equatorial': 6792
}
# Imprime el nombre del planeta con su circunferencia polar.

print(f'{planet["name"]} has a polar circumference of {planet["circumference (km)"]["polar"]}')
