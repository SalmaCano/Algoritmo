import math


def adjust_aspect_ratio(x, y):
    # La relación 16:9 significa que X debe ser (16/9) * Y
    new_x = math.ceil((16 / 9) * y)

    # Devolvemos el nuevo ancho (X) y la misma altura (Y)
    return new_x, y


# Ejemplo de uso
original_x = 590
original_y = 280

new_resolution = adjust_aspect_ratio(original_x, original_y)
print(f"La nueva resolución con proporción 16:9 es: {new_resolution[0]} × {new_resolution[1]}")
