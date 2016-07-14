# **Snippod-Starter-Demo-App-Server**

[![Join the chat at https://gitter.im/shalomeir/snippod-boilerplate](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/shalomeir/snippod-boilerplate?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

## Overview

[**Snippod-Starter-Demo-App-Server**](https://github.com/shalomeir/snippod-starter-demo-app-server) is a **server part** of snippod-starter demo application. A 'snippod-starter-demo-app' is a 'Full Stack Single Page Application' for the starter who want to be a web application developer. 

This repository code is based on [Django](https://www.djangoproject.com/) and [Djnago REST Framework](http://www.django-rest-framework.org/).
You can check out the hosted version [**DEMO**](http://snippod-boilerplate-dev.elasticbeanstalk.com/) at [http://snippod-boilerplate-dev.elasticbeanstalk.com/](http://snippod-boilerplate-dev.elasticbeanstalk.com/).

## Base Repository, Module
  
We made this using these technologies.

* [Django](https://www.djangoproject.com/)
* [Djnago REST Framework](http://www.django-rest-framework.org/)


## Getting Started
Preliminaries :
* Python 3.4
* virtualenv (optional)

You have to git clone this repository.
```
git clone https://github.com/shalomeir/snippod-starter-demo-app-server
```

### Installation for REST API Server

- `virtualenv venv --python=python3.4`
- `source venv/bin/activate`
- `pip install -r requirements.txt`
- `python manage.py makemigrations && python manage.py migrate`
- `python manage.py createsuperuser`


### Usage for REST API Server 

- `python manage.py runserver`


## Description

Django Rest framework provide browserble API. So you can see all get json by browserble API address too.
- account list: ['~/api/v1/accounts/'](http://snippod-boilerplate-dev.elasticbeanstalk.com/api/v1/accounts/)
- post list: ['~/api/v1/posts/'](http://snippod-boilerplate-dev.elasticbeanstalk.com/api/v1/posts/)
- post list sorted by upvote count: ['~/api/v1/posts/?sorting=upvotes'](http://snippod-boilerplate-dev.elasticbeanstalk.com/api/v1/posts/?sorting=upvotes)
- comment list: ['~/api/v1/comments/'](http://snippod-boilerplate-dev.elasticbeanstalk.com/api/v1/comments/)
- single account, post or comment like this ['~/api/v1/posts/:postId/'](http://snippod-boilerplate-dev.elasticbeanstalk.com/api/v1/posts/10/)
- user's posts or comments like this ['~/api/v1/user/:userId/posts/'](http://snippod-boilerplate-dev.elasticbeanstalk.com/api/v1/user/7/posts/)


More information is available at [**this blog post**](http://www.shalomeir.com/2015/05/snippod-boilerplate-1-full-stack-react-flux-django/) written in **Korean**.


## Reference

- [Thinkster.io Django and AngularJS Tutorial](https://thinkster.io/django-angularjs-tutorial/)

## Contributing

Contributions, questions and comments are all welcome and encouraged.

## License
[MIT License](http://opensource.org/licenses/MIT).

Copyright 2016, [Snippod Inc.](http://www.snippod.com/)