#KEGIATAN 1
def add(a, b):
    return a + b

def minus(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    if b != 0:
        return a / b
    else:
        return "Pembagian nol tidak bisa"

def tree(expression_tree):
    if isinstance(expression_tree, tuple):
        left, operation, right = expression_tree
        if operation == '+':
            return add(tree(left), tree(right))
        elif operation == '-':
            return minus(tree(left), tree(right))
        elif operation == '*':
            return mult(tree(left), tree(right))
        elif operation == '/':
            return div(tree(left), tree(right))
    else:
        return expression_tree

expression_tree = ((2, '+', 3), '*', (5, '-', 1))
result = tree(expression_tree)
print("Hasil evaluasi pohon ekspresi:", result)