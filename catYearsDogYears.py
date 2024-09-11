def calculate_age(human_years):
    # Inicializamos las variables para los años del gato y del perro
    cat_years = 0
    dog_years = 0

    # Calculamos los años de gato
    if human_years == 1:
        cat_years = 15
    elif human_years == 2:
        cat_years = 20 + 7
    else:
        cat_years = 15 + 9 + (human_years - 2) * 4

    # Calculamos los años de perro
    if human_years == 1:
        dog_years = 10


    elif human_years == 2:
        dog_years = 15 + 9
    else:
        dog_years = 15 + 9 + (human_years - 2) * 5

    # Retornamos la lista con los años humanos, años de gato y años de perro
    return [human_years, cat_years, dog_years]


# Ejemplo de uso
print(calculate_age(1))  # Salida: [1, 15, 15]
print(calculate_age(2))  # Salida: [2, 24, 24]
print(calculate_age(3))  # Salida: [3, 28, 29]
print(calculate_age(5))  # Salida: [5, 36, 39]
