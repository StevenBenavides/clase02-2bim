import csv
from sqlalchemy.orm import sessionmaker
from modelo import engine, Plataforma, Pais

# se importa información del archivo configuracion
from config import cadena_base_datos

Session = sessionmaker(bind=engine)
session = Session()

# Archivo CSV único que va a leer para cargar las plataformas
archivo = 'data/plataformas.csv'

with open(archivo, 'r', encoding='utf-8') as f:
    lector = csv.DictReader(f)
    for fila in lector:
        # Consultamos si la plataforma ya esta en la base de datos
        plataforma = session.query(Plataforma).filter_by(nombre=fila['nombre']).first()
        
        if not plataforma:
            # Buscamos el pais por nombre
            pais = session.query(Pais).filter_by(nombre=fila['pais']).first()
            
            if pais:
                # se crea un objeto de tipo Plataformas
                nueva_plataforma = Plataforma()
                nueva_plataforma.id = int(fila['id'])
                nueva_plataforma.nombre = fila['nombre']
                nueva_plataforma.suscriptores_millones = float(fila['suscriptores_millones']) 
                nueva_plataforma.paises_id = pais.id
                
                session.add(nueva_plataforma)
                print("  Plataforma agregada: %s" % nueva_plataforma)
        
session.commit()
print("\nDatos de plataformas ingresados correctamente")
