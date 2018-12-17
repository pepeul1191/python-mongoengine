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

+ http://docs.mongoengine.org/guide/connecting.html#guide-connecting
+ https://stackoverflow.com/questions/29495037/mongoengine-ignore-extra-fields-for-schema-validation
+ http://docs.mongoengine.org/apireference.html
+ https://valarmorghulis.io/tech/201701-mongodb-join-query-with-aggregate/
+ http://api.mongodb.com/python/current/examples/aggregation.html

Thanks/Credits

    Pepe Valdivia: developer Software Web Perú [http://softweb.pe]
