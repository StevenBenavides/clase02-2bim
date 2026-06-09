from sqlalchemy.orm import sessionmaker
from sqlalchemy import func  
from modelo import engine, Serie, Actor

Session = sessionmaker(bind=engine)
session = Session()


print("Consulta: Nombre de la serie y el promedio de la edad de sus actores")
print("="*60)

consulta = session.query(Serie.titulo, func.avg(Actor.edad)).join(Serie.actores).group_by(Serie.titulo).all()

for serie, promedio_edad in consulta:
    print(f"Serie: {serie:<30} | Promedio de Edad de Actores: {promedio_edad:.2f} años")
