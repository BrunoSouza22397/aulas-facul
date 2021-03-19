#recebe valor x e funcao (ex.: x³+2x²+1) e retorna o valor de f(x)
def funcao(x, func):
    func = func.replace("x",x)
    result = eval(func)
    return result;
