import csv

with open('Turquia.csv', newline='') as File:
    reader = csv.reader(File, delimiter=';')   # delimitador por defecto => ,
    next(reader)
    total = 0.0
    total_devos = 0.0
    total_pedidos = 0.0
    contador_devos = 0
    contador_pedidos = 0

    for row in reader:
        # Columna 4: total producto
        #print(row[4])
        importe = (float)(row[4].replace('.', '').replace(',', '.'))  # quitamos . de miles y cambiamos , por . en decimales

        if importe < 0.0:
            total_devos += importe
            contador_devos += 1
        else:
            total_pedidos += importe
            contador_pedidos += 1

        total += importe  # para que funcione con cualquier separador

    print('\nEncontrados un total de {0} items que suman: {1}'.format(str(contador_pedidos), str(total_pedidos)))
    print('Encontradas un total de {0} items que suman: {1}\n'.format(str(contador_devos), str(total_devos)))
    print('Total importes pedidos - devos: {0}\n'.format(str(total)))
