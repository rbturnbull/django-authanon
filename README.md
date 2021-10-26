# django-authanon

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