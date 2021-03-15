def funcao(x, func):
    func = func.replace("x",x)
    result = eval(func)
    return result;

def secante(x0, x1, TOL, N, func):
    x2 = x1 - (x1 - x0)*funcao(str(x1), func)/(funcao(str(x1), func) - funcao(str(x0), func))
    i = 1
    
    while ((abs(funcao(str(x2), func)) > TOL) and (i<= N)):
        x0 = x1
        x1 = x2
        x2 = x1 - (x1 - x0)*funcao(str(x1), func)/(funcao(str(x1), func) - funcao(str(x0), func))
        i = i+1
        
    if (i > N):
        print ('Nao houve convergencia!')
        
    if (abs(funcao(str(x2), func)) < TOL):
        print(x2)
        
secante(-1.8, -1.2, .1, 20, "x**4-3*x**3+3")
#x**4–3*x**3+3