from typing import NamedTuple, List
from collections import defaultdict
from datetime import datetime, date
import csv
Pelicula = NamedTuple(
    "Pelicula",
    [("fecha_estreno", date), 
    ("titulo", str), 
    ("director", str), 
    ("generos",List[str]),
    ("duracion", int),
    ("presupuesto", int), 
    ("recaudacion", int), 
    ("reparto", List[str])
    ]
)

#Apartado 1
def lee_peliculas(ruta_archivo:str)->List[tuple]:
    with open(ruta_archivo, encoding='utf-8') as f:
        lector=csv.reader(f, delimiter=';')
        next(lector)
        res=[]
        for fecha_estreno, titulo, director, generos, duracion, presupuesto, recaudacion, reparto in lector:
            fecha_estreno=datetime.strptime(fecha_estreno, '%d/%m/%Y').date()
            generos=generos.strip(' ').split(',')
            duracion=int(duracion)
            presupuesto=int(presupuesto)
            recaudacion=int(recaudacion)
            reparto=reparto.strip(' ').split(',')
            tupla=Pelicula(fecha_estreno, titulo, director, generos, duracion, presupuesto, recaudacion, reparto)
            res.append(tupla)
        return res
    
#Apartado 2
def pelicula_mas_ganancias(registro:List[Pelicula], genero:str=None)->tuple:
    dicc=defaultdict()
    for r in registro:
        if genero==None or genero in r.generos:
            dicc[r.titulo]=(r.recaudacion-r.presupuesto)
    lista=dicc.items()
    res=max(lista, key=lambda n:n[1])
    return res

#Apartado 3
def media_presupuesto_por_genero(registro:List[Pelicula])->dict:
    dicc=defaultdict(list)
    for r in registro:
        for g in range(len(r.generos)):
            dicc[r.generos[g].strip(' ')].append(r.presupuesto)
    for k in dicc.keys():
        dicc[k]=(sum(dicc[k])/len(dicc[k]))
    return dicc

#Apartado 4
def peliculas_por_actor(registro:List[Pelicula], año_inicial:int, año_final:int)->dict:
    dicc=defaultdict(int)
    for r in registro:
        if (año_inicial==None or año_inicial<=r.fecha_estreno.year) and (año_final==None or año_final>=r.fecha_estreno.year):
            for a in r.reparto:
                dicc[a.strip(' ')]+=1
    return dicc

#Apartado 5
def actores_mas_frecuentes(registro:List[Pelicula], n:int, año_inicial:int, año_final:int)->list:
    datappa=peliculas_por_actor(registro, año_inicial, año_final)
    lista=[]
    for k in datappa.keys():
        lista.append((k, datappa[k]))
    lista.sort(key=lambda n:n[1], reverse=True)
    res, nada=zip(*lista[:n])
    res=list(res)
    res.sort()
    return res

#Apartado 6
def recaudacion_total_por_año(registro:List[Pelicula], generos:set[str]=None)->dict:
    dicc=defaultdict(int)
    for r in registro:
        if generos==None or set(r.generos)&generos!=set():
            dicc[r.fecha_estreno.year]+=r.recaudacion 
    return dicc

#Apartado 7
def incrementos_recaudacion_por_año(registro:List[Pelicula], generos:set[str]=None)->list[int]:
    datarta=recaudacion_total_por_año(registro, generos)
    listatu=sorted(datarta.items(), key=lambda n:n[0])
    res=[]
    for r in range(len(listatu)):
        if r!=0:
            res.append(listatu[r][1]-listatu[r-1][1])
    return res

