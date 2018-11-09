## Boilerplate MongoDB Python

Requisitos de software previamente instalado:

	+ Python 3.5
	+ Python PIP

### Descipción

Instalación de dependencias:

    $ sudo pip install virtualenv
    $ virtualenv -p python3 <<nombre_ambiente>>
    $ source bin/activate
    $ pip install -r requirements.txt

### Logs

```
import logging

logging.basicConfig(filename='example.log',level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
```

### Fuentes

+ https://npyscreen.readthedocs.io/introduction.html
+ https://npyscreen.readthedocs.io/application-structure.html

Thanks/Credits

    Pepe Valdivia: developer Software Web Perú [http://softweb.pe]
