# rest-api
Django REST API

# Basic REST API created using Django Rest Framework
> It's a project entirely developed by myself. It presents a simple REST API for a web application that solves the problem of preparing and evaluating exam sheets

## Setup

Parts of the app are run in docker containers. On your local machine you need to download below files:

* [docker](https://docs.docker.com/install/)
* [docker-compose](https://docs.docker.com/compose/install/)
* [make](https://www.gnu.org/software/make/)

Clone or download repository:
```
$ git clone https://github.com/MaciejLoj/rest-api
```
**Running locally**

The following commands, respectively: build all the services and run the containers.

What you need to do to run the app is just open your terminal, then open cloned repository and go to Makefile directory.
Afterwards type in below commands and enjoy the app.
```
$ make build-dev
$ make dev
