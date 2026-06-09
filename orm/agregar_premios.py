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
        serie_obj = session.query(Serie).filter_by(titulo=fila['serie']).first()
        
        if serie_obj:
            # verificamos si este premio específico para esta serie ya existe
            premio_existente = session.query(Premio).filter(
                Premio.nombre_premio == fila['nombre_premio'],
                Premio.anio == int(fila['anio']),
                Premio.serie_id == serie_obj.id
            ).first()

            if not premio_existente:
                nuevo_premio = Premio(
                    nombre_premio=fila['nombre_premio'],
                    categoria=fila['categoria'],
                    anio=int(fila['anio']),  
                    serie=serie_obj          
                )
                session.add(nuevo_premio)
                print("  Premio agregado: '%s' a la serie '%s'" % (nuevo_premio, serie_obj.titulo))
            else:
                print("  Premio ya existente para la serie: '%s' - Premio: '%s'" % (serie_obj.titulo, fila['nombre_premio']))
        
session.commit()
print("\nDatos de premios ingresados correctamente")
