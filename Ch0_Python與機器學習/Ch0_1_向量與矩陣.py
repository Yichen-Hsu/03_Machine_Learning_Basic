# 向量用串列來實作

a = [1, 2, 3]
b = [4, 5, 6]

def addition_of_vectors(a, b):
    return [a_i+b_i for a_i, b_i in zip(a, b)]

def Vector_dot_product(a, b):
    return sum(a_i*b_i for a_i, b_i in zip(a,b))

print(addition_of_vectors(a, b))
print(Vector_dot_product(a, b))