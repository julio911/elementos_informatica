#!/bin/bash

function apagar() {
	sudo shutdown -h now
}

function reiniciar() {
	sudo reboot
}

function info() {
	uname -a
}

function kernel() {
	uname
}

function autor() {
	echo "Julio Leiva Vidal, 11/09/1999, estudiante primer año informatica"
}
function salir() {
    echo "adios"
	exit
}
function pr_1(){
    #!/usr/bin/python
    chmod +x Calculadora.py
    python3 ./Calculadora.py
}

echo "Bienvenido a su menu porfavor seleccione su opcion"


while true;
do

    echo "1 apagar"
    echo "2 reiniciar"
    echo "3 info del sistema operativo"
    echo "4 info del kernel"
	echo "5 autor"
	echo "6 ejecutar proyecto_1"
	echo "0 para salir "

	read RESP
	
    if (($RESP == 1)); then
        apagar
    elif (($RESP == 2)) ; then
        reiniciar
    elif (($RESP == 3)); then
        info 
    elif (($RESP == 4)); then
        kernel
    elif (($RESP == 5)); then
        autor
    elif (($RESP == 6)); then
        pr_1
    elif (($RESP == 0 )); then
        salir
	fi
	
done	

