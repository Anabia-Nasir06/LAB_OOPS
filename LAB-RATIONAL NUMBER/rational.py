class Rational:
    def __init__(self, num, deno):
        if deno == 0:
            raise ValueError("Denominator cannot be zero")
        self.num = num
        self.deno = deno

    @staticmethod
    def GCD(n, d):
        while d != 0:
            n, d = d, n % d
        return n

    @staticmethod
    def LCM(n, d):
        return (n * d) // Rational.GCD(n, d)

    def __add__(self, other):
        new_num = self.num * other.deno + self.deno * other.num
        new_deno = self.deno * other.deno
        gcd = Rational.GCD(new_num, new_deno)
        return Rational(new_num // gcd, new_deno // gcd)

    def __sub__(self, other):
        new_num = self.num * other.deno - self.deno * other.num
        new_deno = self.deno * other.deno
        gcd = Rational.GCD(new_num, new_deno)
        return Rational(new_num // gcd, new_deno // gcd)

    def __str__(self):
        return f"{self.num}/{self.deno}"
