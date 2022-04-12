# Instalacion del proyecto
- Clonar el repositorio
- Actualiza pip  ```python -m pip install --upgrade pip```
- Crea tu entorno virtual para evitar posible incompatibilidad con otras librerias ``` python -m venv env ```
- Activa el entorno virtual ```cd env/scripts/activate ``` posteriormente regresa a la carpeta raiz del proyecto
- Ejecutar ```pip install -r requeriments.txt ```
- Crea tu base de datos llamada ```fastapi``` en todo casi si la quieres crear con otro nombre o si cuentas con contraseña para el usuario root o otro tipo de usuario puedes cambiarlo en la carpeta config>db.py en la linea 4
- Ejecuta la api con uvicorn app:app e ```ingresar a la ruta /docs```
## Se mostrara lo siguiente: 
![Image text](https://github.com/Esekien/FastApi/blob/main/1.png)
## Problema1
### En este caso ingresamos una lista desordenada la cual para cada numero que ingresemos tendremos que pulsar add integer item, al ejecutarlo nos retornada dos listas una con los pares y otra con los impares
![Image text](https://github.com/Esekien/FastApi/blob/main/2.png)
## Problema2
### En este caso tenemos dos inputs lo cuales ingresamos el numero de fila y el de la columna, si excede a mas de 5 filas o 4 columas retornara invalido, cuando se ocupe una butaca esta se imprimira y mostrara las butacas ocupadas con una x y con 0 las que no
![Image text](https://github.com/Esekien/FastApi/blob/main/3.png)

