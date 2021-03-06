# BOMBERMAN

##### Pre requisitos:
  * python3
  * termcolor

##### Ejecución:

Para ejecutar el programa se debe usar:

    $ python3 bomberman.py

Para ejecutar la cobertura de las pruebas se debe usar:

    $ coverage run test.py

Para visualizar la cobertura de las pruebas se debe usar:

    $ coverage html


### Sobre el juego

##### Controles :

| Acciones  | Tecla |
| ------------- | ------------- |
| Izquierda  | a  |
| Derecha  | d  |
| Arriba  | w  |
| Abajo  | s  |
| Lanzar bomba  | b  |
| Salir  | q  |

##### Equivalencias:

| Símbolos  | Equivalencias |
| ------------- | ------------- |
| '/'  | Ladrillos  |
| 'B'  | Bomberman  |
| 'E'  | Enemigo  |
| 'e'  | Explosión de fuego  |
| 'X'  | Muros  |

##### Funcionalidad:

* El jugador es controlado por el usuario y los enemigos se mueven aleatoriamente en el tablero, pero no pueden atravesar paredes o ladrillos.
* Bomberman puede lanzar una bomba que destruye ladrillos y enemigos a su alrededor después de 3 segundos. Al matar a un enemigo, el usuario obtiene 100 puntos y al romper ladrillos, el usuario obtiene 20 puntos.
* Hay 3 niveles del juego. Al matar a todos los enemigos, el nivel se incrementa aumentando la dificultad del juego.
* El usuario gana el juego al pasar todos los niveles.


#### Desarrollado por: Syed Mohd Ali Rizwi
