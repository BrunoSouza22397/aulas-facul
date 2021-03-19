#recebe valor x e funcao (ex.: x³+2x²+1) e retorna o valor de f(x)
def funcao(x, func):
    x = str(x)
    func = func.replace("x",x)
    result = eval(func)
    return result;

#calcula raiz de função utilizando o método de secante
#recebe x0 e x1 como valores iniciais, TOL como critério de parada, N como número de repetições e a função que será calculada.
def secante(x0, x1, TOL, N, func):
    x2 = x1 - (x1 - x0)*funcao(x1, func)/(funcao(x1, func) - funcao(x0, func))
    i = 1
    
    while ((abs(funcao(x2, func)) > TOL) and (i<= N)):
        x0 = x1
        x1 = x2
        x2 = x1 - (x1 - x0)*funcao(x1, func)/(funcao(x1, func) - funcao(x0, func))
        i = i+1
        
    if (i > N):
        print ('Nao houve convergencia!')
        
    if (abs(funcao(x2, func)) < TOL):
        print(x2)
        
secante(-1.8, -1.2, .1, 20, "x**4-3*x**3+3")
