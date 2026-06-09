import csv
from sqlalchemy.orm import sessionmaker
from modelo import engine, Pais


from config import cadena_base_datos

Session = sessionmaker(bind=engine)
session = Session()

# se carga la información del archivo csv diriguendonos a la carpeta data 
archivos = ['data/paises.csv']

for archivo in archivos:
        
        with open(archivo, 'r', encoding='utf-8-sig') as f:
            lector = csv.DictReader(f)
            for fila in lector:
                # Consultamos si el pais ya esta en la base de datos
                pais = session.query(Pais).filter_by(nombre=fila['nombre']).first()
                
                if not pais:
                    # se crea un objeto de tipo Paises
                    pais = Pais()
                    pais.id = int(fila['id'])
                    pais.nombre = fila['nombre']
                    pais.continente = fila['continente']
                    
                    session.add(pais)
                    print("  Pais agregado: %s" % pais)
    
session.commit()
print("\nDatos de paises ingresados correctamente")

