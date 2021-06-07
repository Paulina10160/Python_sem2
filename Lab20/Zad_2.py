import unittest


class TestPPM(unittest.TestCase):
    def setUp(self) -> None:
        self.w1 = BMR(60, 170, 20)
        self.m1 = BMR(80, 185, 23)

    def test_for_men(self):
        # True
        m1_check = self.m1.Men_ppm()
        self.assertTrue(m1_check > 0)

    def test_for_women(self):
        # False
        w1_check = self.w1.Women_ppm()
        self.assertTrue(w1_check < 0)


class BMR:
    def __init__(self, mass, heigh, age):
        self.mass = mass
        self.heigh = heigh
        self.age = age

    def Men_ppm(self):
        return 66 + (13.7 * self.mass) + (5 * self.heigh) + (6.76 * self.age)

    def Women_ppm(self):
        return 655 + (9.6 * self.mass) + (1.8 * self.heigh) + (4.7 * self.age)


if __name__ == "__main__":
    unittest.main()