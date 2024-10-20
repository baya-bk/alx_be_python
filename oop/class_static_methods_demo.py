# class_static_methods_demo.py

class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Returns the sum of two numbers"""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Returns the product of two numbers and prints the class attribute"""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
