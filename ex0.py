from utils_log import log_decorator

@log_decorator
def soma(x, y):
    return x + y

print(soma(4, 8))

#logger.warning("blaaaa")