from classroom.asignatura import Asignatura
from classroom.grupo import Grupo

if __name__ == "__main__":
    
    asignatura1 = Asignatura("Vision por Computador")
    asignatura2 = Asignatura("POO", "Salon 503B")

    grupo1 = Grupo()
    grupo2 = Grupo("Grupo 32")
    grupo3 = Grupo("Grupo 23", [asignatura1])
    grupo4 = Grupo("Grupo 12", [asignatura1, asignatura2], ["Jaime", "David", "Oswaldo"])

    grupo1.agregarAlumno("Alumno10")
    grupo2.agregarAlumno("Alumno20")
    grupo3.agregarAlumno("Alumno30")
    grupo4.agregarAlumno("Alumno40")

    grupo1.agregarAlumno("Alumno11")
    grupo2.agregarAlumno("Alumno21")
    grupo3.agregarAlumno("Alumno31")
    grupo4.agregarAlumno("Alumno41")

    grupo1.agregarAlumno("Alumno14", ["Alumno12", "Alumno13"])
    grupo2.agregarAlumno("Alumno24", ["Alumno22", "Alumno23"])
    grupo3.agregarAlumno("Alumno34", ["Alumno32", "Alumno33"])
    grupo4.agregarAlumno("Alumno44", ["Alumno42", "Alumno43"])
    
    
    print(grupo1)
    print(grupo2)
    print(grupo3)
    print(grupo4)
    print(grupo1.listadoAlumnos)
    print(grupo2.listadoAlumnos)
    print(grupo3.listadoAlumnos)
    print(grupo4.listadoAlumnos)