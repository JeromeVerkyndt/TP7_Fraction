import fraction


def test_fraction(num, den):
    try:
        fract = fraction.Fraction(num, den)
        print(fract.__str__)
    except AttributeError as e:
        print(e)
    except ZeroDivisionError as e:
        print(e)
    except ValueError as e:
        print(e)


test_fraction(1, -2)
test_fraction(3, 0)
test_fraction(3, -5)
test_fraction(-7, 4)
test_fraction(-45, -234)

print("---------------------------")
test_deux = fraction.Fraction(7, 5)
fract_bis = fraction.Fraction(3, 4)
print(test_deux.as_mixed_number())
print(test_deux.__str__)
print(test_deux.__sub__(fract_bis).__str__)
print(test_deux.__mul__(fract_bis).__str__)
print(test_deux.__truediv__(fract_bis).__str__)
print(test_deux.__pow__(3).__str__)
print(test_deux.__eq__(fract_bis))
print(test_deux.__float__())
print(test_deux.is_zero())
print(test_deux.is_integer())
print(test_deux.is_proper())
print(test_deux.is_unit())
print(test_deux.is_adjacent_to(fract_bis))
