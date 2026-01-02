class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def is_even(num):
        return num % 2 == 0

print(MathUtils.add(10, 20))
print(MathUtils.is_even(6))
