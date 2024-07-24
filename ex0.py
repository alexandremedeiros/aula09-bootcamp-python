from loguru import logger

logger.add("meu_app.log")

def soma(x, y):
    try:
        soma = x + y
        logger.info(f"A soma é {soma}")
        return x + y
    except:
        logger.critical("Algum parâmetro está errado")

print(soma(4, 8))

#logger.warning("blaaaa")