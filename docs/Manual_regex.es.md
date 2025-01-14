



# Regex
  
Módulo para trabajar con patrones fijos o complejos a través de Regex.  

*Read this in other languages: [English](Manual_regex.md), [Português](Manual_regex.pr.md), [Español](Manual_regex.es.md)*
  
![banner](imgs\Banner_Regex.jpg)

## Como instalar este módulo
  
Para instalar el módulo en Rocketbot Studio, se puede hacer de dos formas:
1. Manual: __Descargar__ el archivo .zip y descomprimirlo en la carpeta modules. El nombre de la carpeta debe ser el mismo al del módulo y dentro debe tener los siguientes archivos y carpetas: \__init__.py, package.json, docs, example y libs. Si tiene abierta la aplicación, refresca el navegador para poder utilizar el nuevo modulo.
2. Automática: Al ingresar a Rocketbot Studio sobre el margen derecho encontrara la sección de **Addons**, seleccionar **Install Mods**, buscar el modulo deseado y presionar install.  


## Descripción de los comandos

### Comienza con
  
Detecta cadenas de texto que comienzan con una letra o un número.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Dato|Dato para buscar palabras que inicien con letra o número.|H|
|Texto|Texto a buscar palabras que inicien en letra o número.|Hola mundo|
|Asignar resultado a variable|Variable que almacena el resultado.|{var}|

### Contiene
  
Busca cadenas de texto que contengan el dato indicado
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Dato|Dato a buscar en el texto|Undo|
|Texto|Texto a buscar las palabras que contienen el dato indicado.|Hola Mundo|
|Asignar resultado a variable|Variable que almacena el resultado.|{var}|

### Obtener fechas
  
Obtiene todas las fechas del texto ingresado
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Texto|Texto donde se obtiene la fecha|Fecha: yyyy/mm/dd - dd/mm/yyyy|
|Asignar resultado a variable|Variable donde se almacena la fecha obtenida|{var}|

### Obtener teléfono
  
Obtiene numeros de teléfonos de un texto
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Texto|Texto donde se obtiene el numero de teléfono|Teléfono: +18005551212|
|Asignar resultado a variable|Variable donde se almacena los numeros de telefonos obtenidos.|{var}|

### Obtener correo
  
Obtiene todos los correos de un texto
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Texto|Texto donde se obtiene el correo electrónico|Correo: usuario@ejemplo.com|
|Asignar resultado a variable|Variable donde se almacena los correos electrónicos obtenidos|{var}|
