# QueryString deserializer

def __setKey (o, keys, value):
    if( len(keys) > 1 ):
        o[keys[0]] = {}
        __setKey(o[keys[0]], keys[1:], value)
    else:
        o[keys[0]] = value

def deserialize(qs):    # write Fibonacci series up to n
    if( not isinstance(qs, str) ):
        raise TypeError('should be a string')

    params = qs.split('&')
    result = {}

    for param in params:
        parts = param.split('=')
        __setKey(result, parts[0].split('.'), parts[1] )

    return result

__all__ = ['deserialize']
