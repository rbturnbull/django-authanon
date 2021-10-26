# django-authanon

![pipline](https://github.com/rbturnbull/django-authanon/actions/workflows/coverage.yml/badge.svg)
[<img src="https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/rbturnbull/49262550cc8b0fb671d46df58de213d4/raw/coverage-badge.json">](<https://rbturnbull.github.io/django-authanon/coverage/>)
[<img src="https://github.com/rbturnbull/django-authanon/actions/workflows/docs.yml/badge.svg">](<https://rbturnbull.github.io/django-authanon/>)
[<img src="https://img.shields.io/badge/code%20style-black-000000.svg">](<https://github.com/psf/black>)

Allows permissions for an anonymous user and a generic signed-in user to be set as groups.

## Installation 

```
pip install django-authanon
```

Then add to your installed apps:
```
INSTALLED_APPS += [
    "authanon",
]
```

Then add to your installed apps:
```
AUTHENTICATION_BACKENDS += [
    "authanon.backends.AuthanonBackend",
]
```

## Usage



## Configuration