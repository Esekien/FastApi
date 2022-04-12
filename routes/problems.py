from fastapi import APIRouter, Query
from typing import List

problems = APIRouter()
lista = [['0','0','0','0'],
        ['0','0','0','0'],
        ['0','0','0','0'],
        ['0','0','0','0'],
        ['0','0','0','0']]



@problems.get('/par-impar',response_model=List[int], tags=['problems'])
def get_list(lista: List[int] = Query(None)):
    lista.sort()
    pares = []
    impares = []
    for i in lista:
        if(i%2==0):
            pares.append(i)
        else:
            impares.append(i)
    return {'pares':pares , 'impares':impares}

@problems.post('/problema2', tags=['problems'])
def post_butaca(fila:int, colum:int):
    if fila > 4 or colum > 3:
        return 'fila o columna invalida(s)'
    if lista[fila][colum] == 'x':
        return 'butaca ocupada intente de nuevo'
    lista[fila][colum] = 'x'
    return {'ok':'butaca agregada',
            'butacas':lista}