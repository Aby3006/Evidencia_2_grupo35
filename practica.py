class Persona:
    def __init__(self, apellidos, nombres):
        if not apellidos or not nombres:
            raise ValueError("Los apellidos y nombres no pueden estar vacíos.")
        
        if any(caracter in "0123456789" for caracter in apellidos + nombres):
            raise ValueError("Los apellidos y nombres no pueden contener números.")

        self.apellidos = apellidos
        self.nombres = nombres

    def describir(self):
        return f"Esta es una persona que se apellida {self.apellidos} y se llama {self.nombres}."

class Empleado(Persona): 
    def __init__(self, apellidos, nombres, clave): 
        super().__init__(apellidos, nombres)
        if not isinstance(clave, int) or clave <= 0: 
            raise ValueError("La clave debe ser un número entero positivo.")

        self.clave = clave

    def describir(self):
        return f"Empleado: {self.nombres} {self.apellidos}, Clave: {self.clave}."

class Paciente(Persona):
    def __init__(self, apellidos, nombres, clave, sexo):
        super().__init__(apellidos, nombres)

        if not isinstance(clave, int) or clave <= 0:
            raise ValueError("La clave debe ser un número entero positivo.")

        sexo = str(sexo).lower()

        if sexo not in ["hombre", "mujer"]:
            raise ValueError("El sexo debe ser 'hombre' o 'mujer'.")

        self.clave = clave
        self.sexo = sexo
    
def main():
    while True:
        print("\nRegistro de Persona")
        apellidos = input("Ingrese los apellidos (sin espacios ni números): ")
        nombres = input("Ingrese los nombres (sin espacios ni números): ")
        
        try:
            persona = Persona(apellidos, nombres)
            print(persona.describir())
            break 
        except ValueError as error:
            print("Error:", error) 

    while True:
        print("\nRegistro de Empleado")
        apellidos = input("Ingrese los apellidos del empleado: ")
        nombres = input("Ingrese los nombres del empleado: ")
        
        try:
            clave = int(input("Ingrese la clave del empleado (debe ser un número entero positivo): "))
            empleado = Empleado(apellidos, nombres, clave)
            print(empleado.describir())
            break 
        except (ValueError, TypeError) as error:
            print("Error:", error) 

    while True:
        print("\nRegistro de Paciente")
        apellidos = input("Ingrese los apellidos del paciente: ")
        nombres = input("Ingrese los nombres del paciente: ")
        
        try:
            clave = int(input("Ingrese la clave del paciente (número entero positivo): "))
            sexo = input("Ingrese el sexo del paciente (hombre/mujer): ").strip().lower()

            paciente = Paciente(apellidos, nombres, clave, sexo)
            print(paciente.describir())
            break
        except ValueError as error:
            print("Error:", error)

if __name__ == "__main__":
    main()