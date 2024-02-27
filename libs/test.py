from libs.libs import verifie_multiplication, verifie_additions_limites


def test_1(function):
    assert (
        function(3) == 3
    ), f"Mauvaise réponse ! La réponse attendue était 3 ! Mais tu m'as retourné {function(3)}"

    assert (
        function(4) == 4
    ), f"Mauvaise réponse ! La réponse attendue était 4 ! Mais tu m'as retourné {function(4)}"

    assert (
        function(8) == 8
    ), f"Mauvaise réponse ! La réponse attendue était 8 ! Mais tu m'as retourné {function(8)}"

    print("Bravo tu as réussi !!")


def test_6(function):
    assert (
        function(5, 4) == 9
    ), f"Mauvaise réponse ! La réponse attendue était 9 ! Mais tu m'as retourné {function(5, 4)}"
    assert (
        function(1, 6) == 7
    ), f"Mauvaise réponse ! La réponse attendue était 7 ! Mais tu m'as retourné {function(1, 6)}"
    assert (
        function(-7, 6) == -1
    ), f"Mauvaise réponse ! La réponse attendue était -1 ! Mais tu m'as retourné {function(-7, 6)}"
    assert (
        function(8, -8) == 0
    ), f"Mauvaise réponse ! La réponse attendue était 0 ! Mais tu m'as retourné {function(8, -8)}"
    print("Bravo tu as réussi !!")


def test_7(function):
    assert (
        function(1) == 1
    ), f"Mauvaise réponse ! La réponse attendue était 1 ! Mais tu m'as retourné {function(1)}"
    assert (
        function(0) is None
    ), f"Mauvaise réponse ! La réponse attendue était None ! Mais tu m'as retourné {function(0)}"
    assert (
        function(9) == 9
    ), f"Mauvaise réponse ! La réponse attendue était 9 ! Mais tu m'as retourné {function(9)}"
    assert (
        function("B") == "B"
    ), f"Mauvaise réponse ! La réponse attendue était 'B' ! Mais tu m'as retourné {function('B')}"
    assert (
        function(-3) == -3
    ), f"Mauvaise réponse ! La réponse attendue était -3 ! Mais tu m'as retourné {function(-3)}"
    print("Bravo tu as réussi !!")


def test_8(function):
    verifie_multiplication(function)
    assert (
        function(4) == 12
    ), f"Mauvaise réponse ! La réponse attendue était 12 ! Mais tu m'as retourné {function(4)}"
    assert (
        function(-1) == -3
    ), f"Mauvaise réponse ! La réponse attendue était -3 ! Mais tu m'as retourné {function(-1)}"
    assert (
        function(0) == 0
    ), f"Mauvaise réponse ! La réponse attendue était 0 ! Mais tu m'as retourné {function(0)}"
    print("Bravo tu as réussi !!")


def test_9(function):
    assert (
        function(4) is None
    ), f"Mauvaise réponse ! La réponse attendue était None ! Mais tu m'as retourné {function(4)}"
    assert (
        function(0) == 0
    ), f"Mauvaise réponse ! La réponse attendue était 0 ! Mais tu m'as retourné {function(0)}"
    assert (
        function(-4) is None
    ), f"Mauvaise réponse ! La réponse attendue était None ! Mais tu m'as retourné {function(4)}"
    assert (
        function("F") is None
    ), f"Mauvaise réponse ! La réponse attendue était None ! Mais tu m'as retourné {function('F')}"
    print("Bravo tu as réussi !!")


def test_10(function):
    verifie_multiplication(function)
    assert (
        function(5) == 40
    ), f"Mauvaise réponse ! La réponse attendue était 40 ! Mais tu m'as retourné {function(5)}"
    assert (
        function(-1) == -8
    ), f"Mauvaise réponse ! La réponse attendue était -8 ! Mais tu m'as retourné {function(-1)}"
    assert (
        function(4) == 32
    ), f"Mauvaise réponse ! La réponse attendue était 32 ! Mais tu m'as retourné {function(4)}"
    assert (
        function(0) == 0
    ), f"Mauvaise réponse ! La réponse attendue était 0 ! Mais tu m'as retourné {function(0)}"
    verifie_additions_limites(function, 3)
    print("Bravo tu as réussi !!")


def test_11(function):
    assert function(2, 7) == (
        5,
        -5,
    ), f"Mauvaise réponse ! La réponse attendue était (-5, 5) ! Mais tu m'as retourné {function(-5,5)}"
    assert function(9, 4) == (
        -5,
        5,
    ), f"Mauvaise réponse ! La réponse attendue était (-5, 5) ! Mais tu m'as retourné {function(9,4)}"
    assert function(-5, -5) == (
        0,
        0,
    ), f"Mauvaise réponse ! La réponse attendue était (0, 0) ! Mais tu m'as retourné {function(-5,-5)}"
    assert function(9, -4) == (
        -13,
        13,
    ), f"Mauvaise réponse ! La réponse attendue était (-13, 13) ! Mais tu m'as retourné {function(9,-4)}"
    print("Bravo tu as réussi !!")


def test_12(function):
    verifie_multiplication(function)
    assert (
        function(2) == 80
    ), f"Mauvaise réponse ! La réponse attendue était 80 ! Mais tu m'as retourné {function(2)}"
    assert (
        function(-3) == -120
    ), f"Mauvaise réponse ! La réponse attendue était -120 ! Mais tu m'as retourné {function(-3)}"
    assert (
        function(7) == 280
    ), f"Mauvaise réponse ! La réponse attendue était 280 ! Mais tu m'as retourné {function(7)}"
    assert (
        function(0) == 0
    ), f"Mauvaise réponse ! La réponse attendue était 0 ! Mais tu m'as retourné {function(0)}"
    verifie_additions_limites(function, 6)
    print("Bravo tu as réussi !!")


def test_13(function):
    assert (
        function(1, 8) is None
    ), f"Mauvaise réponse ! La réponse attendue était None ! Mais tu m'as retourné {function(1,8)}"
    assert (
        function(3, 3) == 3
    ), f"Mauvaise réponse ! La réponse attendue était 3 ! Mais tu m'as retourné {function(3,3)}"
    assert (
        function(5, 5) == 5
    ), f"Mauvaise réponse ! La réponse attendue était 5 ! Mais tu m'as retourné {function(5,5)}"
    assert (
        function(6, 6) == 6
    ), f"Mauvaise réponse ! La réponse attendue était 6 ! Mais tu m'as retourné {function(6,6)}"
    print("Bravo tu as réussi !!")


def test_14(function):
    assert (
        function(4, 6) == 6
    ), f"Mauvaise réponse ! La réponse attendue était 6 ! Mais tu m'as retourné {function(4,6)}"
    assert (
        function(-3, -1) == -1
    ), f"Mauvaise réponse ! La réponse attendue était -1 ! Mais tu m'as retourné {function(-3,-1)}"
    assert (
        function(2, 2) == 2
    ), f"Mauvaise réponse ! La réponse attendue était 2 ! Mais tu m'as retourné {function(2,2)}"
    assert (
        function(4, -9) == 4
    ), f"Mauvaise réponse ! La réponse attendue était 4 ! Mais tu m'as retourné {function(4,-9)}"
    print("Bravo tu as réussi !!")


def test_16(function):
    assert (
        function(3) == 3
    ), f"Mauvaise réponse ! La réponse attendue était 3 ! Mais tu m'as retourné {function(3)}"
    assert (
        function(-9) == 9
    ), f"Mauvaise réponse ! La réponse attendue était 9 ! Mais tu m'as retourné {function(-9)}"
    assert (
        function(8) == 8
    ), f"Mauvaise réponse ! La réponse attendue était 8 ! Mais tu m'as retourné {function(8)}"
    assert (
        function(0) == 0
    ), f"Mauvaise réponse ! La réponse attendue était 0 ! Mais tu m'as retourné {function(0)}"
    assert (
        function(-6) == 6
    ), f"Mauvaise réponse ! La réponse attendue était 6 ! Mais tu m'as retourné {function(-6)}"
    print("Bravo tu as réussi !!")


def test_17(function):
    assert (
        function(8, -2) == 1
    ), f"Mauvaise réponse ! La réponse attendue était 1 ! Mais tu m'as retourné {function(8,-2)}"
    assert (
        function(4, 5) == 0
    ), f"Mauvaise réponse ! La réponse attendue était 0 ! Mais tu m'as retourné {function(4,5)}"
    assert (
        function(-9, -1) == 0
    ), f"Mauvaise réponse ! La réponse attendue était 0 ! Mais tu m'as retourné {function(-9,-1)}"
    assert (
        function(4, -2) == 1
    ), f"Mauvaise réponse ! La réponse attendue était 1 ! Mais tu m'as retourné {function(4,-2)}"
    print("Bravo tu as réussi !!")


def test_20(function):
    verifie_multiplication(function)
    assert (
        function(5, 5) == 25
    ), f"Mauvaise réponse ! La réponse attendue était 25 ! Mais tu m'as retourné {function(5,5)}"
    assert (
        function(0, 9) == 0
    ), f"Mauvaise réponse ! La réponse attendue était 0 ! Mais tu m'as retourné {function(0,9)}"
    assert (
        function(8, 0) == 0
    ), f"Mauvaise réponse ! La réponse attendue était 0 ! Mais tu m'as retourné {function(8,0)}"
    assert (
        function(9, 3) == 27
    ), f"Mauvaise réponse ! La réponse attendue était 27 ! Mais tu m'as retourné {function(9,3)}"
    print("Bravo tu as réussi !!")
