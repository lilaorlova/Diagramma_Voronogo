"""Даются 2 координаты вершины ребра. Ответ даётся в виде уравнения прямой типа y = kx+b """
def per(x1,y1, x2, y2):
    k = (y1-y2)/(x1-x2)
    b = y2 - k*x2
    b_answer = abs(y2-y1)/2 + y1
    k_answer = -1/k
    return k_answer, b_answer
