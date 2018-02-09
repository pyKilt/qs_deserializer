# QueryString deserializer

import re

def setKey (o, keys, value):
    if( len(keys) > 1 ):
        o[keys[0]] = {}
        setKey(o[keys[0]], keys[1:], value)
    else:
        o[keys[0]] = value

def bracketsToDots (text):
    return re.sub(r"\]\[|\[|\]", ".", re.sub(r"\]$", "", re.sub(r"^\[", "", text)) )

def deserialize(qs):
    if( not isinstance(qs, str) ):
        raise TypeError('should be a string')

    params = qs.split('&')
    result = {}

    for param in params:
        parts = param.split('=')
        setKey(result, bracketsToDots(parts[0]).split('.'), parts[1] )

    return result

__all__ = ['deserialize', 'setKey', 'bracketsToDots']
