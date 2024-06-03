from collections import Counter
import math

def leer_datos(file_path) -> list[int]:
    with open(file_path, 'r') as file:
        data = file.read()
    datos = list(map(int, data.split()))
    return datos

def media_aritmetica(n, sum) -> float:
    return sum / n

def desbideracion_tipica(n, media, sum) -> float:
    return math.sqrt((sum/n) - media*media)

def coeficiente_variacion(media, desbideracion) -> float:
    return desbideracion/media

def main():
    datos = 'archivo.txt'
    datos = leer_datos(datos)

    frecuencias = Counter(datos)

    val_x = sorted(frecuencias.keys())
    val_f = [frecuencias[x] for x in val_x]
    val_fx = [x * f for x, f in zip(val_x, val_f)]
    val_fx2 = [x * x * f for x, f in zip(val_x, val_f)]

    N = sum(val_f)
    sum_fx = sum(val_fx)
    sum_fx2 = sum(val_fx2)

    media = media_aritmetica(N, sum_fx)
    media = round(media, 2)

    desbideracion = desbideracion_tipica(N, media, sum_fx2)
    desbideracion = round(desbideracion, 2)

    coeficiente = coeficiente_variacion(media, desbideracion)
    coeficiente = round(coeficiente, 2) * 100

    print(f"La media aritmetica es {media}")
    print(f"La desbideración típica es {desbideracion}")
    print(f"El coeficiente de variación es del {int(coeficiente)}%")


if __name__ == '__main__':
    main()