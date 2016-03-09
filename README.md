<b>Pokemon Catch Rate Calculator - by carchenilla</b>

Pues eso, es una pequeña app en python con GUI para calcular la probabilidad de captura de un Pokemon.

Para su funcionamiento es necesario tener instalado PyQt4, debido a la interfaz gráfica de la aplicación.

Los contenidos del proyecto son: 

- dataDictionary.p 
  <br>Comprimido con pickle contiene todos los datos necesarios de todos los Pokemon, obtenidos haciendo scraping en Bulbpedia. 
  Si se desea, se puede crear de nuevo con el script PokemonDictionary.py 
  
- PokemonDictionary.py
  <br>Modificando el main y ejecutando el script se puede redescargar el fichero desde la web, pero tarda un poquillo. 
  Básicamente va recorriendo una tabla con los ratios de captura de cada pokemon y para cada uno de ellos, accede a su ficha (también en Bulbapedia)
  para extraer el resto de datos necesarios. 

- Pokemon.py
  <br>Se utiliza para encapsular la información de los Pokemon. 

- calculatorGUI.py 
  <br>Contiene la interfaz gráfica de la aplicación. Diseñada con QtDesigner y parseada a un script de Python. 

- RatioCalculator.py
  <br>Script principal. Contiene una clase que extiende a QtDialog que se encarga de lanzar la aplicación y realizar los calculos oportunos
  cuando se pulsa el botón. 

- En la carpeta images se incluyen el icono de la app, el logo, y los sprites de los pokemon, que también se muestran en la interfaz. 

Se puede mejorar y bastante. No hay apenas control de excepciones y la interfaz es bastante sosilla, pero para algo es una versión 1.0.
<br>Cuando tenga un ratejo y si no tengo mucho que hacer lo mismo le dedico un poquillo y sigo con ella.
