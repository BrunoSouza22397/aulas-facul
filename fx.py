﻿def funcao(x, func):
    func = func.replace("x",x)
    result = eval(func)
    return result;