def logger(f):
    def inspect(*args, **kwargs):
        res = f(*args, **kwargs)
        print(f"Args: {args}\nKwargs: {kwargs}\nRetvalue: {res}")
        return res
    return inspect

@logger  
def concat(*args, reversed = False):
    if reversed:
        return print(*args[::-1])
    return print(*args)

#concat = logger(concat)

l = concat("hello", " ", "world", "asd", reversed = True)