import unittest
# Імпортуйте вашу функцію/клас з файлу src.lab13
from src.lab13 import *


# -- Початок прикладу --
#
# class TestCalculateArea(unittest.TestCase):
#   """
#   Тести для функції calculate_area.
#   """
#   def test_positive_side(self):
#     """
#     Перевірка обчислення площі для додатного значення сторони.
#     """
#     self.assertEqual(calculate_area(5), 25)
#
#   def test_zero_side(self):
#     """
#     Перевірка обчислення площі для нульового значення сторони.
#     """
#     self.assertEqual(calculate_area(0), 0)
#
#   def test_negative_side(self):
#     """
#     Перевірка обробки від'ємного значення сторони.
#     """
#     with self.assertRaises(ValueError):
#       calculate_area(-5)
#
# -- Кінець прикладу --


# Напишіть ваші тести тут
# Створіть клас, що наслідується від unittest.TestCase
# та напишіть в ньому тестові методи
class TestStudentImplementation(unittest.TestCase):
    def test_placeholder(self):
        """
        Цей тест-заглушка перевіряє, що у файлі src/lab13.py є реалізація.
        Замініть його на власні тести.
        """
        # Приклад: перевірка, чи існує певна функція.
        # self.assertTrue(callable(my_function))
        pass


# Цей блок коду дозволяє запускати тести безпосередньо з командного рядка
if __name__ == '__main__':
    unittest.main()