import csv
from sqlalchemy.orm import sessionmaker
from modelo import engine, Actor, Pais, Serie
from config import cadena_base_datos

Session = sessionmaker(bind=engine)
session = Session()

archivos = ['data/actores.csv']
for archivo in archivos:
        print("\nProcesando archivo: %s" % archivo)
        
        with open(archivo, 'r', encoding='utf-8-sig') as f:
            lector = csv.DictReader(f)
            for fila in lector:
                actor_existente = session.query(Actor).filter_by(nombre=fila['nombre']).first()
                
                if not actor_existente:
                    pais = session.query(Pais).filter_by(nombre=fila['pais']).first()
                    # Buscamos el objeto Serie por su título
                    serie = session.query(Serie).filter_by(titulo=fila['serie']).first()
                    
                    if pais and serie:
                        # Creamos el actor y asignamos los OBJETOS a las relaciones
                        actor = Actor(
                            nombre=fila['nombre'],
                            edad=int(fila['edad']),
                            pais=pais,    
                            serie=serie   
                        )
                        
                        session.add(actor)
                        print("  Actor agregado: %s" % actor)
                    else:
                        if not pais:
                            print("  País no encontrado para actor: '%s' - País: '%s'" % (fila['nombre'], fila['pais']))
                        if not serie:
                            print("  Serie no encontrada para actor: '%s' - Serie: '%s'" % (fila['nombre'], fila['serie']))
                else:
                    print("  Actor ya existe: %s" % actor_existente.nombre)
    
session.commit()
print("\nDatos de actores ingresados correctamente")
