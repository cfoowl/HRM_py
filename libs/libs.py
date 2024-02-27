import ast
import inspect


def compte_multiplications(code_source):
    tree = ast.parse(code_source)
    multiplication_count = sum(isinstance(node, ast.Mult) for node in ast.walk(tree))
    return multiplication_count


def verifie_multiplication(fonction):
    code_source = inspect.getsource(fonction)
    multiplication_count = compte_multiplications(code_source)

    if multiplication_count > 0:
        assert False, "Interdiction d'utiliser la multiplication"


def compte_additions(code_source):
    tree = ast.parse(code_source)
    addition_count = sum(isinstance(node, ast.Add) for node in ast.walk(tree))
    return addition_count


def verifie_additions_limites(fonction, limite):
    code_source = inspect.getsource(fonction)
    additions_count = compte_additions(code_source)

    if additions_count > limite:
        assert (
            False
        ), f"Tu as réussi, malheureusement tu as utilisé {additions_count} additions, au lieu de {limite}"
