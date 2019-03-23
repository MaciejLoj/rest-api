# Basic REST API created using Django Rest Framework
Presents a simple REST API for a web application that solves the problem of preparing and evaluating exam sheets

## Setup
To set up such an app you need to download Docker files and GNU Make.
Just follow below links and download above-mentioned files:

* [docker](https://docs.docker.com/install/)
* [docker-compose](https://docs.docker.com/compose/install/)
* [make](https://www.gnu.org/software/make/)

**Afterwards just clone below repository**:
```
$ git clone https://github.com/MaciejLoj/rest-api
```


## Starting the app

Below commands allow you to start the project locally by building up the container and running the app locally. 

What you have to do is just get to the directory containing docker-compose file and type in below commands.


```
$ make build-dev
$ make dev
