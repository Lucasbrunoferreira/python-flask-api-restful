# Flask API RESTful - Python

## English

This is a simple example, to implements a http web server (API RESTfull) with python (Flask framework).


### Dependencies

| Dependency        | For what?           | Link  |
| ------------- |:-------------:| -----:|
| flask | web framework server    |    http://flask.pocoo.org |
| flask-restful | extension for Flask that adds support for quickly building REST APIs    |    https://flask-restful.readthedocs.io |
| pymongo      | mongo database driver | https://api.mongodb.com/python/current/ |
| marshmallow      | fileds schema validator     |   https://marshmallow.readthedocs.io |
| logzero | create application logs   |    https://logzero.readthedocs.io/en/latest/ |
| unittest | unit tests   |    https://docs.python.org/3/library/unittest.html |



### Routes

* GET - `/api/v1/pets` - Get all pets
* GET - `/api/v1/pets/{pet_id}` - Get only the pet for the id entered in the parameter
* POST - `/api/v1/pets` - Create new pet
* PUT - `/api/v1/pets/{pet_id}` - Edit the pet referring to the id entered in the parameter
* DELETE - `/api/v1/pets/{pet_id}` - Delete the pet referring to the id entered in the parameter

### Architecture

* **Controllers** - It is the layer responsible for manipulating requests and performing business rules.

* **Persistence** - Layer responsible for data manipulation.

    * **Schemas** - Data modeling.
    
    * **Database** - Connection and manipulation with database.
    
* **Tests** - Layer with unit application tests

* **Util** - Gathers higher-use (repetitive) codes in the project.


### Tests
Run all unit application tests
* `cd project-folder`
* `python -m unittest`

### Run
After preparing your environment and your virtualenv, follow the steps:

* `cd project-folder`
* `pip install -r requirements.txt`
*  set the MONGO_URI environment variable (for connection to the database) and the APP_PORT variable (port on which the application will run) on your machine, or manually change the settings.py file.
* `python server.py`

Run application with docker:
* `cd project-folder`
* `docker build -t api-flask-img .`
*  set a MONGODB_URI environment variable no following command and run it.
* `docker run -d -p 8080:8080 --name api-flask -e MONGO_URI="mongodb://user:password@host:port/database" api-flask-img:latest`
* your application is running in 8080 port

##


## Português - Brasil

Este é um exemplo simples, para implementar um servidor web http (API RESTfull) com python (framework Flask).


### Dependências

| Dependência        | Qual o uso?           | Link  |
| ------------- |:-------------:| -----:|
| flask | framework para servidor web   |    http://flask.pocoo.org |
| flask-restful | extensão para adicionar construir REST APIs no Flask com mais praticidade.    |    https://flask-restful.readthedocs.io |
| pymongo      | conexão com o banco de dado NoSQL mongo | https://api.mongodb.com/python/current/ |
| marshmallow      | validação de campos e dados     |   https://marshmallow.readthedocs.io |
| logzero | criação de logs da applicação   |    https://logzero.readthedocs.io/en/latest/ |
| unittest | testes unitários   |    https://docs.python.org/3/library/unittest.html |

### Rotas

* GET - `/api/v1/pets` - Buscar todos os pets cadastrados
* GET - `/api/v1/pets/{pet_id}` - Busque apenas o pet referente ao id informado no paramêtro
* POST - `/api/v1/pets` - Criar um novo pet
* PUT - `/api/v1/pets/{pet_id}` - Editar o pet referente ao id informado no parâmetro
* DELETE - `/api/v1/pets/{pet_id}` - Deletar o pet referente ao id informado no parâmetro

### Arquitetura

* **Controller** - É a camada responsável por manipular as requisições e realizar as regras de negócios.

* **Persistence** - Camada responsável pela manipulação de dados.

    * **Schemas** - Modelagem de dados.
    
    * **Database** - Conexão e manipulação com banco de dados.

* **Tests** - Camada com os testes unitarios da aplicação

* **Util** - Reúne códigos de uso mais alto (repetitivos) no projeto


### Executar os Testes
Para realizar todos os testes do projeto, execute:
* `cd project-folder`
* `python -m unittest`


### Executar a aplicação

Depois de preparar seu ambiente e seu virtualenv, siga os passos:

* `cd project-folder`
* `pip install -r requirements.txt`
*  defina a variavél de ambiente MONGO_URI (para conexão com o  banco) e a variavél APP_PORT (porta na qual a aplicação sera executada) em sua maquina, ou altere manualmente no arquivo settings.py.
* `python main.py`

Se preferir, pode executar a aplicação com o docker:
* `cd project-folder`
* `docker build -t api-flask-img .`
* defina a variavél de ambiente MONGO_URI no comando aseguir e execute-o.
* `docker run -d -p 8080:8080 --name api-flask -e MONGO_URI="mongodb://user:password@host:port/database" api-flask-img:latest`
* sua aplicação esta rodando na porta 8080
