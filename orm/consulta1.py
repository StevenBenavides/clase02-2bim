from sqlalchemy.orm import sessionmaker
from modelo import engine, Serie

Session = sessionmaker(bind=engine)
session = Session()

series = session.query(Serie).all()

print("--- Resumen de Series, Actores y Premios ---")
for serie in series:
    promedio_edad = serie.obtener_edad_actores()
    premios_ganados = serie.obtener_premios()
    
    print("\n--------------------------------------------------")
    print(f"Serie: {serie.titulo}")
    print("--------------------------------------------------")    
    print(f"  - Promedio de Edad de Actores: {promedio_edad:.2f} años")
    print(f"  - Premios Ganados: {premios_ganados}")