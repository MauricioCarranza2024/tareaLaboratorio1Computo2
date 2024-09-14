*** EXPLICACION DE LOS EJERCICIOS DEL LABORATORIO 1, SEGUNDO COMPUTO, PROGRAMACION III ***

ESTOS EJERCICIOS FUERON DESARROLLADOS POR:

1 - **Mauricio Alfredo Carranza Velasques -SMTR059023**

2 - **Erick Josue Chavez Moraga - SMTR152021**

En este caso dimos solucion a cada ejercio que nos precento y asi mismo pudimos analizar la funcion que dimos a cada uno y daremos un breve comentario a cada ejercio

"""**Ejercicio 1**"""  Este programa crea una ventana gráfica que muestra el nombre completo en este caso de nosotros dos ("Mauricio Carranza y Erick Chavez") y la edad suponiendo que es nuestra edad (18 y 19 años) centrados en la pantalla. La ventana tiene un diseño sencillo con etiquetas que presentan esta información de forma clara y bien alineada. Es útil para interfaces en las que se requiere mostrar información básica del usuario.

Problema que resuelve el ejercicio 1:
Sirve como una interfaz simple para mostrar información personal en aplicaciones que requieran la verificación de identidad o presentación de datos básicos.

"""**Ejercicio 2**"""  Este programa muestra una ventana en la que el usuario puede ingresar una clave secreta. Para mantener la privacidad, los caracteres que el usuario escribe no son visibles, ya que el campo de texto está configurado en modo "contraseña". Una vez que la clave es ingresada, el programa puede procesarla en este caso, hicimos que solo la guardara.

Problema que resuelve el ejercicio 2:
Es útil para situaciones donde se necesita proteger la entrada de información confidencial, como en formularios de inicio de sesión o autenticación.

"""**Ejercicio 3**"""  Este programa permite al usuario ingresar su número de cédula y nombre completo en dos campos de texto separados. Luego, esta información puede ser procesada o almacenada. La interfaz es simple y funcional, ya que es diseñada para recopilar datos personales esenciales.

Problema que resuelve el ejercicio 3:
El programa es ideal para formularios de registro o sistemas de entrada de datos, donde se requiere la identificación de los usuarios mediante su cédula y nombre completo. Esto es común en aplicaciones de verificación o registro.

"""**Ejercicio 4**""" Este programa crea una ventana donde el usuario puede ingresar tres datos básicos de tres mascotas: su nombre, especie, y edad. El campo de edad está validado para aceptar solo números, lo que garantiza la correcta entrada de datos. Se utiliza una interfaz gráfica simple y directa para facilitar la captura de la información.

Problemática que resuelve:

Este programa permite registrar de forma sencilla y correcta los datos básicos de las mascotas, especialmente asegurándose de que la edad sea un valor numérico. Esto evita que los usuarios ingresen texto no válido y ayuda a organizar correctamente la información.

"""**Ejercicio 5**""" El programa muestra una ventana que permite al usuario ingresar 10 datos característicos de una persona, como su nombre, edad, género, nacionalidad, entre otros. El campo de edad está validado para aceptar solo números, evitando errores en la entrada. Esta interfaz es sencilla y muestra los campos en un diseño vertical.

Problemática que resuelve:

El programa resuelve el problema de recolectar varios datos de una persona de manera eficiente y organizada. Asegura que los datos ingresados en el campo de edad sean válidos, evitando errores típicos en el formato de entrada. Además, permite almacenar y visualizar datos importantes de manera estructurada.

"""**Ejercicio usando PyQt mediante una problematica**""" Este programa permite que el usuario ingrese mediante el teclado su nombre, género, país y edad en el cual estuvimos utilizando los widgets QRadioButton, QComboBox, y QSpinBox. Al presionar el botón "Enviar", los datos ingresados se muestran en una ventana emergente (QMessageBox).

Los Widgets utilizados:

QRadioButton: Se utiliza para seleccionar el género entre opciones binarias (masculino o femenino).

QComboBox: Permite seleccionar un país de una lista predefinida.

QSpinBox: Se utiliza para seleccionar la edad, restringiendo el valor a un rango de 0 a 100 años.

Problema que resuelve este ejercicio: desde nuestro punto de vista, este programa es útil en escenarios donde se necesita recolectar datos personales básicos de manera rápida y sencilla, puede ser parte de una interfaz para el registro de usuarios o para formularios en kioscos de autoservicio, donde se requieren datos como género, país y edad, asi facilita la entrada de información y reduce errores mediante el uso de opciones predefinidas y controladas.
