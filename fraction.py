def pgcd(a, b):
    while a % b != 0:
        a, b = b, a % b
    return b


class Fraction:
    """Classe représentant une fraction et opérations sur celle-ci

    Auteur : J.Verkyndt
    Date : Decembre 2023
    Cette classe permet des manipulations de fractions via plusieurs opérations.
    """

    def __init__(self, num, den):
        """Cela construit une fraction basée sur un numérateur et un dénominateur.

                PRE : -le numerateur et le dénominateur doiventt etre des entier
                POST :/
                RAISES : -ZeroDivisionError si dénominateur = 0
        """
        if den == 0:
            raise ZeroDivisionError("Le denominateur ne peut pas être zero.")
        else:
            div = pgcd(num, den)
            self.__num = int(num/div)
            self.__den = int(den/div)
            self.total = self.__num / self.__den
            self.rest = self.__num % self.__den

    @property
    def numerator(self):
        return self.__num

    @property
    def denominator(self):
        return self.__den

    # ------------------ Textual representations ------------------

    @property
    def __str__(self):
        """
                Renvoie une représentation textuelle de la forme réduite de la fraction

                PRE : /
                POST : Renvoie un string de la fraction simplifié

        """
        return str(self.__num) + "/" + str(self.__den)

    def as_mixed_number(self):
        """
                Renvoie une représentation textuelle de la forme réduite de la fraction sous la forme d'un nombre fractionnaire
                Un nombre fractionnaire est la somme d'un entier et d'une fraction propre

                PRE :/
                POST :Retourne un string de la fraction sous la forme d'un nombre entier et d'une fraction (ex: 2 et 1/4)
        """
        if self.total > 1 and self.rest != 0:
            div = pgcd(self.rest, self.__den)
            return str(int(self.__num // self.__den)) + " et " + str(int(self.rest / div)) + "/" + str(int(self.__den / div))
        elif self.rest == 0:
            return str(int(self.__num/self.__den))
        else:
            return str(int(self.__num)) + "/" + str(int(self.__den))

    # ------------------ Operators overloading ------------------

    def __add__(self, other):
        """
                Surcharge de l'opérateur + pour les fractions

                 PRE :-Le terme a aditionner doit etre un objet fraction
                 POST : -Renvoie un objet fraction simplifié de l'addition de ces deux fraction
        """

        num = (self.__num * other.denominator) + (other.numerator * self.__den)
        den = (other.denominator * self.__den)
        div = pgcd(num, den)
        return Fraction(num/div, den/div)

    def __sub__(self, other):
        """
                Surcharge de l'opérateur - pour les fractions

                PRE :-Le terme a soustraire doit etre un objet fraction
                POST : -Renvoie un objet fraction simplifier de la soustraction des deux fractions
        """

        num = (self.__num * other.denominator) - (other.numerator * self.__den)
        den = (other.denominator * self.__den)
        div = pgcd(num, den)
        return Fraction(num/div, den/div)

    def __mul__(self, other):
        """
                Surcharge de l'opérateur * pour les fractions

                PRE :-La fraction utiliser pour la multiplication doit être un objet fraction
                POST : -Renvoie un objet fraction simplifier de la multiplication des deux fractions
        """

        num = (self.__num * other.numerator)
        den = (self.__den * other.denominator)
        div = pgcd(num, den)
        return Fraction(num/div, den/div)

    def __truediv__(self, other):
        """
                Surcharge de l'opérateur / pour les fractions

                PRE : -La fraction utiliser pour la division doit être un objet fraction
                POST : -Renvoie un objet fraction simplifier de la division.
                RAISES : -ZeroDivisionError si le diviseur égale zero.
        """

        num = (self.__num * other.denominator)
        den = (self.__den * other.numerator)
        div = pgcd(num, den)
        return Fraction(num/div, den/div)

    def __pow__(self, other):
        """
                Surcharge de l'opérateur ** pour les fractions
                PRE : -Le terme exposant doit etre un nombre entier.
                POST : -Renvoie un objet fraction simplifier
        """
        numexpo = self.__num ** other
        denexpo = self.__den ** other
        div = pgcd(numexpo, denexpo)
        return Fraction(numexpo/div, denexpo/div)

    def __eq__(self, other):
        """
            Surcharge de l'opérateur == pour les fractions
                PRE : La fraction utiliser pour la l'égalité doit être un objet fraction
                POST : Renvoi 'True' si les deux fractions son égale donc valent la même chose quand elle sont simplifié,
                 sinon renvoi 'False'
        """

        numa = (self.__den * other.numerator)
        numb = (other.denominator * self.__num)
        return numa == numb

    def __float__(self):
        """Renvoie la valeur décimale de la fraction

                PRE : /
                POST :-La valeur de retour est un nombre décimal.
        """
        return self.__num / self.__den

    # ------------------ Properties checking ------------------

    def is_zero(self):
        """
            Vérifier si la valeur d'une fraction est 0

                PRE : /
                POST : Renvoi 'True' si la fraction est égale à zero, sinon renvoi 'False'
        """
        return self.total == 0

    def is_integer(self):
        """
            Vérifier si une fraction est un entier (ex : 8/4, 3, 2/2, ...)

                PRE : /
                POST : Renvoi 'True' si la fraction est un entier, sinon renvoi 'False'
        """
        return self.__num % self.__den == 0

    def is_proper(self):
        """
            Vérifiez si la valeur absolue de la fraction est < 1

                PRE : /
                POST : Renvoi 'True' si la fraction est < 1, sinon renvoi 'False'
        """
        return self.total < 1

    def is_unit(self):
        """
            Vérifier si le numérateur d'une fraction est 1 sous sa forme réduite

                PRE :/
                POST : Renvoi 'True' si le numérateur est 1, sinon renvoi 'False'
        """
        div = pgcd(self.__num, self.__den)
        return self.__num / div == 1

    def is_adjacent_to(self, other):
        """
                Vérifier si deux fractions diffèrent d'une fraction unitaire

                Deux fractions sont adjacentes si la valeur absolue de leur différence est une fraction unitaire

                PRE : La fraction utiliser doit être un objet fraction.
                POST : Renvoi 'True' si les deux fraction diffèrent d'une fraction unitaire, sinon renvoi 'False'
        """

        num = (self.__num * other.denominator) - (other.numerator * self.__den)
        den = (other.denominator * self.__den)
        div = pgcd(num, den)
        return (num / div) == 1 or (num / div) == -1
