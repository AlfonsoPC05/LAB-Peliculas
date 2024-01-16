from peliculas import *

def test_lee_peliculas(ruta_archivo):
    datos=lee_peliculas(ruta_archivo)
    print("Test de lee_peliculas:")
    print(f"Total registros leídos: {len(datos)}")
    print('Mostrando los tres primeros registros:')
    for r in range(3):
        print(f"\t {datos[r]}")

def test_pelicula_mas_ganancias(datos, genero=None):
    print(f"Test de pelicula_mas_ganancias (genero={genero})")
    print(pelicula_mas_ganancias(datos, genero))

def test_media_presupuesto_por_genero(datos):
    print("Test de media_presupuesto_por_genero:")
    print(media_presupuesto_por_genero(datos))

def test_peliculas_por_actor(datos, año_inicial=None, año_final=None):
    pelicpa=peliculas_por_actor(datos, año_inicial, año_final)
    print(f"Test de peliculas_por_actor (año_inicial={año_inicial}, año_final={año_final}):")
    print("(sólo se mostrará el número de películas de tres actores concretos)")
    print(f"Robert Downey Jr.: {pelicpa['Robert Downey Jr.']}")
    print(f"Christian Bale: {pelicpa['Christian Bale']}")
    print(f"Adam Driver: {pelicpa['Adam Driver']}")

def test_actores_mas_frecuentes(datos, n, año_inicial, año_final):
    print(f"Test de actores_mas_frecuentes (n={n}, año_inicial={año_inicial}, año_final={año_final}):")
    print(actores_mas_frecuentes(datos, n, año_inicial, año_final))

def test_recaudacion_total_por_año(datos, generos=None):
    print(f"Test de recaudacion_total_por_año (generos={generos}:")
    print(recaudacion_total_por_año(datos, generos))

def test_incrementos_recaudacion_por_año(datos, generos=None):
    print(f"Test de incrementos_recaudacion_por_año (generos={generos}):")
    print(incrementos_recaudacion_por_año(datos, generos))



if __name__=="__main__":
    datos=lee_peliculas('data/peliculas.csv')
    test_lee_peliculas('data/peliculas.csv')
    test_pelicula_mas_ganancias(datos)
    test_pelicula_mas_ganancias(datos, 'Drama')
    test_media_presupuesto_por_genero(datos)
    test_peliculas_por_actor(datos)
    test_peliculas_por_actor(datos, 2010, 2020)
    test_actores_mas_frecuentes(datos, 3, 2005, 2015)
    test_recaudacion_total_por_año(datos)
    test_recaudacion_total_por_año(datos, {'Drama', 'Acción'})
    test_incrementos_recaudacion_por_año(datos)
    test_incrementos_recaudacion_por_año(datos, {'Drama', 'Acción'})