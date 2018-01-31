# QueryString deserializer

def deserialize(qs):    # write Fibonacci series up to n
    if( not isinstance(qs, str) ):
        raise TypeError('should be a string')
    params = qs.split('&')
    result = {}

    for param in params:
        print param
        
    return qs.split('&')

__all__ = ['deserialize']
