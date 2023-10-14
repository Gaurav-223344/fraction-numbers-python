from fraction.data_type import DataType
import math

class Fraction(DataType):
    
    def __init__(self, numerator, denominator, whole_unit=0):
        self.numerator =  numerator
        self.denominator =  denominator
        self.whole_unit =  whole_unit

        self.__validate_all()

    @staticmethod
    def __common_denominator(fraction_1, fraction_2): 
        if (fraction_1.denominator != fraction_2.denominator):
            fraction_1_numerator = fraction_1.numerator * fraction_2.denominator
            fraction_2_numerator =  fraction_2.numerator * fraction_1.denominator
            common_denominator = fraction_1.denominator * fraction_2.denominator

            fraction_1.numerator = fraction_1_numerator
            fraction_2.numerator = fraction_2_numerator
            fraction_1.denominator = common_denominator
            fraction_2.denominator = common_denominator

        print(fraction_1, fraction_2)
        return fraction_1, fraction_2
    
    @staticmethod
    def __validate(value):
        if (str(value).isnumeric()):
            pass
        else:
            raise TypeError("Only integers are allowed ")

    def __validate_all(self):
        self.__validate(self.numerator)
        self.__validate(self.denominator)
        self.__validate(self.whole_unit)


    def __string_representation(self):
        unit = str(self.whole_unit)+" " if self.whole_unit else ""
        return f'{unit}{self.numerator}/{self.denominator}'
    

    def __repr__(self):
        return self.__string_representation()
    
    def __str__(self):
        return self.__string_representation()

    def __eq__(self, other):
        
        frac1, frac2 = self.__common_denominator(self.simplify(), other.simplify())
     
        if (frac1.numerator == frac2.numerator):
            return True
        else:
            return False

    def __ge__(self, other):
        frac1, frac2 = self.__common_denominator(self.simplify(), other.simplify())
     
        if (frac1.numerator >= frac2.numerator):
            return True
        else:
            return False

    def __gt__(self,other):
        frac1, frac2 = self.__common_denominator(self.simplify(), other.simplify())
     
        if (frac1.numerator > frac2.numerator):
            return True
        else:
            return False

    def __le__(self, other):
        frac1, frac2 = self.__common_denominator(self.simplify(), other.simplify())
     
        if (frac1.numerator <= frac2.numerator):
            return True
        else:
            return False

    def __lt__(self, other):
        frac1, frac2 = self.__common_denominator(self.simplify(), other.simplify())
     
        if (frac1.numerator < frac2.numerator):
            return True
        else:
            return False

    def __ne__(self, other=None):
        frac1, frac2 = self.__common_denominator(self.simplify(), other.simplify())
     
        if (frac1.numerator < frac2.numerator):
            return True
        else:
            return False

    def __add__(self):
        pass

    def __sub__(self):
        pass

    def __mult__(self):
        pass

    def __truediv__(self):
        pass


    '''
        improper fraction to mixed number conversion.
        eg ->  1 11/4 to 2 3/4
        
        vise versa

        Conversion to mixed numbers and decimals

        Finding the greatest common factor (GCD) and least common multiple (LCM) of fractions

        Simplifying fractions

        Solving fractional equations
    
    '''

    def simplify(self):
        self.numerator = (self.whole_unit * self.denominator) + self.numerator    
        self.whole_unit = 0

        gcd_value = math.gcd(self.numerator, self.denominator)
        if(gcd_value != 1):
            self.numerator = int(self.numerator / gcd_value)
            self.denominator = int(self.denominator / gcd_value)

        return self

