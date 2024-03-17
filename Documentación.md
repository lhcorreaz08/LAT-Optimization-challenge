
## Q1 Memory

Estratégia: Delegar el procesamiento de los datos a un microservicio de cloud run de (GCP) asi mismo el almacenamiento del archivo se hace mediante un bucket de GCP. Esto permite enviar unicamente el 
request con los datos del archivo a procesar y el contenedor de lo aloja.

Servicios cloud utilizados (GCP): Cloud Run, Cloud Storage y container registry. 

La lógica del microservicio se encuentra en el directorio ./Cloud Run/Q1_memory_cloud_run con el uso de flask, la implementación algorithm de map-reduce y el archivo dockerfile para la creación de la imagen.

Mejoras:
La implementación se puede hacer con un cluster de dataproc para el procesamiento de los datos, esto permitiría el uso de spark para el procesamiento de los datos y 
el uso de un bucket de GCP para el almacenamiento de los archivos.



## Q2 Memory

Estratégia: Delegar el procesamiento de los datos a un microservicio de cloud run de (GCP) asi mismo el almacenamiento del archivo se hace mediante un bucket de GCP. Esto permite enviar unicamente el
request con los datos del archivo a procesar y el contenedor de lo aloja.

Servicios cloud utilizados (GCP): Cloud Run, Cloud Storage y container registry.

La lógica del microservicio se encuentra en el directorio ./Cloud Run/Q2_memory_cloud_run con el uso de flask, la implementación algorithm de map-reduce y el archivo dockerfile para la creación de la imagen.

Mejoras:
La implementación se puede hacer con un cluster de dataproc para el procesamiento de los datos, esto permitiría el uso de spark para el procesamiento de los datos y
el uso de un bucket de GCP para el almacenamiento de los archivos.



## Q3 Memory

Estratégia: Delegar el procesamiento de los datos a un microservicio de cloud run de (GCP) asi mismo el almacenamiento del archivo se hace mediante un bucket de GCP. Esto permite enviar unicamente el
request con los datos del archivo a procesar y el contenedor de lo aloja.

Servicios cloud utilizados (GCP): Cloud Run, Cloud Storage y container registry.

La lógica del microservicio se encuentra en el directorio ./Cloud Run/Q3_memory_cloud_run con el uso de flask, la implementación algorithm de map-reduce y el archivo dockerfile para la creación de la imagen.

Mejoras:
La implementación se puede hacer con un cluster de dataproc para el procesamiento de los datos, esto permitiría el uso de spark para el procesamiento de los datos y
el uso de un bucket de GCP para el almacenamiento de los archivos.



## Q1 Time

Estratégia: Implementar un algoritmo de map-reduce para el procesamiento de los datos, el cual se encarga de leer el archivo y procesar los datos para obtener el top 10 de usuarios que más tweets han realizado

Servicios cloud utilizados (GCP): Ninguno

Mejoras:
Manejo de librerias como apache spark para el procesamiento de los datos, esto permitiría el uso de spark para el procesamiento de los datos y el uso de un bucket de GCP para el almacenamiento de los archivos.


## Q2 Time

Estratégia: Implementar un algoritmo de map-reduce para el procesamiento de los datos, el cual se encarga de leer el archivo y procesar los datos para obtener el top 10 de emojis más utilizados en los tweets

Servicios cloud utilizados (GCP): Ninguno

Mejoras:
Manejo de librerias como apache spark para el procesamiento de los datos, esto permitiría el uso de spark para el procesamiento de los datos y el uso de un bucket de GCP para el almacenamiento de los archivos.


## Q3 Time

Estratégia: Implementar un algoritmo de map-reduce para el procesamiento de los datos, el cual se encarga de leer el archivo y procesar los datos para obtener el top 10 de usuarios más mencionados en los tweets

Servicios cloud utilizados (GCP): Ninguno

Mejoras:
Manejo de librerias como apache spark para el procesamiento de los datos, esto permitiría el uso de spark para el procesamiento de los datos y el uso de un bucket de GCP para el almacenamiento de los archivos.







