# Infinity

## Table of Contents

1. [General Info](#general-info)
2. [Technologies](#technologies)
3. [Installation](#installation)
4. [Collaboration](#collaboration)

---

## General Info

Website created for the "Python" course at Coderhouse.

This site was born with the idea of creating an Ecommerce store for products. Previously, it was initially developed in JavaScript, then React, Node, and now a version with Django.

**Branches:** It has two working branches: `main` (where the final project is hosted) and the `V.01` branch where updates and fixes are worked on.

---

## Technologies

[<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/701px-Python-logo-notext.svg.png" alt="python" width="40" height="40"/>](https://www.python.org/) **3.11.4**

</br>

[<img src="https://static.djangoproject.com/img/logo-django.42234b631760.svg" alt="vite" width="100" height="40"/>](https://www.djangoproject.com/) **4.2.7**

</br>

[<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/sass/sass-original.svg" alt="sass" width="40" height="40"/>](https://sass-lang.com) **V2.19.6**

</br>

---

## Installation

To set up and run the Infinity Shop Django project, follow these steps:

### 1. Clone the Repository

```bash

git clone https://github.com/NicolasCaminos/Infinity-Shop-Django.git

```

### 2. Set Up the Environment

```bash
$ cd Infinity
# Install project dependencies and tools
$ npm run setup
```

### 3. Start the Application

Choose one of the following methods to start the application:

- Method 1: Using npm (for development)

```bash

# Start the application using npm (for development)
$ npm run dev
```

This command uses concurrently to run both the Django server and the frontend development server simultaneously.

- Method 2: Using npm (for development or production)


```bash

# Start the application using npm (for development or production)
$ npm run start
```

This command also uses concurrently to run both the Django server and the frontend development server simultaneously.

- Method 3: Using Python (for development or production)

```bash
# Alternatively, start the application using Python (for development or production)
$ python manage.py runserver
```

## Collaboration

- Nicolás Caminos
