import csv
from sqlalchemy.orm import sessionmaker
from modelo import engine, Serie, Plataforma, Pais
from config import cadena_base_datos

Session = sessionmaker(bind=engine)
session = Session()

archivo = 'data/series.csv'

with open(archivo, 'r', encoding='utf-8') as f:
        lector = csv.DictReader(f)
        for fila in lector:
            serie = session.query(Serie).filter_by(titulo=fila['titulo']).first()
            
            if not serie:

                # Buscamos la plataforma por nombre
                plataforma = session.query(Plataforma).filter_by(nombre=fila['plataforma']).first()
                
                if plataforma:

                    pais = plataforma.pais 
                    
                    nueva_serie = Serie(
                        titulo=fila['titulo'],
                        genero=fila['genero'],
                        anio_estreno=int(fila['anio_estreno']),
                        temporadas=int(fila['temporadas']),
                        plataforma=plataforma, 
                        pais=pais 
                    )
                    
                    session.add(nueva_serie)
                    print("Serie agregada: %s" % nueva_serie)
                else:
                    print("Plataforma no encontrada para serie: %s" % fila['titulo'])
    
session.commit()
print("Datos de series ingresados correctamente")
