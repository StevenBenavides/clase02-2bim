import csv
from sqlalchemy.orm import sessionmaker
from modelo import engine, Premio, Serie

from config import cadena_base_datos
Session = sessionmaker(bind=engine)
session = Session()

archivo = 'data/premios.csv'

with open(archivo, 'r', encoding='utf-8') as f:
    lector = csv.DictReader(f)
    for fila in lector:
        # Consultamos si el premio ya está en la base de datos
        premio_existente = session.query(Premio).filter_by(nombre_premio=fila['nombre_premio']).first()
    
        if not premio_existente:
            # Buscamos el objeto Serie por su título
            serie_obj = session.query(Serie).filter_by(titulo=fila['serie']).first()
            
            if serie_obj:
                nuevo_premio = Premio(
                    nombre_premio=fila['nombre_premio'],
                    categoria=fila['categoria'],
                    anio=int(fila['anio']),  
                    serie=serie_obj          
                )
                
                session.add(nuevo_premio)
                print("  Premio agregado: %s" % nuevo_premio)
            else:
                print("  Serie no encontrada para el premio: '%s' - Serie: '%s'" % (fila['nombre_premio'], fila['serie']))
        
session.commit()
print("\nDatos de premios ingresados correctamente")
