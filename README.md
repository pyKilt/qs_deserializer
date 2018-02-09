
# qs-params

[![PyPI version](https://badge.fury.io/py/qs-params.svg)](https://badge.fury.io/py/qs-params)
[![Build Status](https://travis-ci.org/pyKilt/qs_params.svg?branch=master)](https://travis-ci.org/pyKilt/qs_params)

``` sh
pip install qs-params
```

``` py
from qs import deserialize

print deserialize('nested[value]=foobar&foo=bar&hola=caracola&adios=caracol')

# output: {'hola':'caracola','adios':'caracol','foo':'bar','nested':{'value': 'foobar'}}
```

``` py
from qs import serialize

print serialize({'hola':'caracola','adios':'caracol','foo':'bar','nested':{'value': 'foobar'}})

# output: 'nested[value]=foobar&foo=bar&hola=caracola&adios=caracol'
```
