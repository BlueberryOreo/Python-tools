# util
# 获取两个数的最大公因数
def max_common_factor(a, b):
    m = 0
    for i in range(1, min(abs(a), abs(b)) + 1):
        if a % i == 0 and b % i == 0:
            m = i

    return m


# 将一个有限小数转换成分数
def change_to_fraction(numerator: float):
    denominator = 1
    while numerator != int(numerator):
        denominator *= 10
        numerator *= 10
    f = Fraction(numerator=int(numerator), denominator=denominator)
    f.reduction()
    return f


# 判断一个分数是否为无限循环小数
def is_infinity(f):
    f.reduction()
    denominator = f.denominator
    while denominator % 5 == 0:
        denominator /= 5

    while denominator % 2 == 0:
        denominator /= 2

    if denominator == 1:
        return False
    else:
        return True


class DivideByZeroError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


# 分数类
class Fraction:
    numerator = None  # 分子
    denominator = None  # 分母

    # 创建一个分数，可以用字符串（a/b）表示，也可以利用关键参数直接输入分子与分母
    def __init__(self, fraction="", numerator=None, denominator=None):
        if fraction != "":
            if "/" in fraction:
                nums = list(map(int, fraction.split("/")))
                if nums[1] == 0:
                    raise DivideByZeroError("The denominator can not be 0")
                self.numerator = nums[0]
                self.denominator = nums[1]
            else:
                self.numerator = int(fraction)
                self.denominator = 1
        elif numerator is not None and denominator is not None:
            if denominator == 0:
                raise DivideByZeroError("The denominator can not be 0")
            self.numerator = numerator
            self.denominator = denominator

    # 分数的加法
    def add(self, f2):
        new_numerator = self.numerator * f2.denominator + f2.numerator * self.denominator
        new_denominator = self.denominator * f2.denominator
        common_factor = max_common_factor(new_numerator, new_denominator)
        new_numerator //= common_factor
        new_denominator //= common_factor
        return Fraction(numerator=new_numerator, denominator=new_denominator)

    # 分数的减法
    def minus(self, f2):
        new_numerator = self.numerator * f2.denominator - f2.numerator * self.denominator
        new_denominator = self.denominator * f2.denominator
        common_factor = max_common_factor(new_numerator, new_denominator)
        new_numerator //= common_factor
        new_denominator //= common_factor
        return Fraction(numerator=new_numerator, denominator=new_denominator)

    # 分数的乘法
    def multiple(self, f2):
        new_numerator = self.numerator * f2.numerator
        new_denominator = self.denominator * f2.denominator
        common_factor = max_common_factor(new_numerator, new_denominator)
        new_numerator //= common_factor
        new_denominator //= common_factor
        return Fraction(numerator=new_numerator, denominator=new_denominator)

    # 分数的除法
    def divide(self, f2):
        new_numerator = self.numerator * f2.denominator
        new_denominator = self.denominator * f2.numerator
        common_factor = max_common_factor(new_numerator, new_denominator)
        new_numerator //= common_factor
        new_denominator //= common_factor
        return Fraction(numerator=new_numerator, denominator=new_denominator)

    # 分数的乘方，返回一个浮点数
    def pos(self, exp):
        return self.numerator ** exp / self.denominator ** exp

    # 分数的约分
    def reduction(self):
        common_factor = max_common_factor(self.numerator, self.denominator)
        self.numerator //= common_factor
        self.denominator //= common_factor

    # 获取分数（字符串形式）
    def get_fraction_str(self):
        return str(self.numerator) + "/" + str(self.denominator) if self.denominator != 1 else str(self.numerator)

    # 获取分数（整型元组形式）
    def get_fraction(self):
        return self.numerator, self.denominator

    # 获得分数的值
    def get_value(self):
        return self.numerator / self.denominator

    # 获得分数的符号
    def get_sign(self):
        if self.numerator * self.denominator > 0:
            sign = "+"
        elif self.numerator * self.denominator < 0:
            sign = "-"
        else:
            sign = "0"
        return sign


if __name__ == "__main__":
    # test
    print(max_common_factor(10, 20))
    f = change_to_fraction(2.57)
    print(f.get_fraction_str())

    f1 = Fraction("-2/3")
    f2 = Fraction(numerator=6, denominator=3)
    print(f1)

    print(f1.get_fraction_str())
    print(f2.get_fraction_str())

    print(f1.get_fraction())
    print(f2.get_fraction())
    f1.reduction()
    f2.reduction()
    print(f1.get_fraction_str())
    print(f2.get_fraction_str())
    print(f2.get_fraction())

    print(f1.get_value())
    print(f2.get_value())

    print(f1.get_sign())
    print(f2.get_sign())

    f3 = f1.add(f2)
    print(f3.get_fraction_str())

    f4 = f1.minus(f2)
    print(f4.get_fraction_str())

    f5 = f1.multiple(f2)
    print(f5.get_fraction_str())

    f6 = f1.divide(f2)
    print(f6.get_fraction_str())