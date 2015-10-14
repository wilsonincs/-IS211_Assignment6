__author__ = 'wilsonincs'

from conversions import convertCelciusToFahrenheit,convertCelciusTokelvin,convertFahrenheitToCelcius,convertKelvinToFahrenheit,kelvinToCelcius, convertFahrenheitToKelvin
import unittest



class CelsiusToKelvin(unittest.TestCase):

    def positiveValue_testing(self):
        self.assertEqual(convertCelciusTokelvin(300.0), 573.15)

    def zeroBasedValue_testing(self):
        self.assertEqual(convertCelciusTokelvin(0.0), 273.15)

    def decimal_value_testing(self):
        self.assertEqual(convertCelciusTokelvin(200.22), 373.37)

    def big_value_testing(self):
        self.assertEqual(convertCelciusTokelvin(937538), 937938.15)

    def negative_value_testing(self):
        self.assertEqual(convertCelciusTokelvin(-200.0), 173.15)


class CelsiusToFahrenhiet(unittest.TestCase):

    def positiveValue_testing(self):
        self.assertEqual(convertCelciusToFahrenheit(300.0), 573.15)

    def zeroBasedValue_testing(self):
        self.assertEqual(convertCelciusToFahrenheit(0.0), 273.15)

    def decimal_value_testing(self):
        self.assertEqual(convertCelciusToFahrenheit(200.22), 373.37)

    def big_value_testing(self):
        self.assertEqual(convertCelciusToFahrenheit(937538), 937938.15)

    def negative_value_testing(self):
        self.assertEqual(convertCelciusToFahrenheit(-200.0), 173.15)


class FahrenheitToCelsius(unittest.TestCase):

    def positiveValue_testing(self):
        self.assertEqual(convertFahrenheitToCelcius(300.0), 573.15)

    def zeroBasedValue_testing(self):
        self.assertEqual(convertFahrenheitToCelcius(0.0), 273.15)

    def decimal_value_testing(self):
        self.assertEqual(convertFahrenheitToCelcius(200.22), 373.37)

    def big_value_testing(self):
        self.assertEqual(convertFahrenheitToCelcius(937538), 937938.15)

    def negative_value_testing(self):
        self.assertEqual(convertFahrenheitToCelcius(-200.0), 173.15)


class FahrenheitToKelvin(unittest.TestCase):

    def positiveValue_testing(self):
        self.assertEqual(convertFahrenheitToKelvin(300.0), 573.15)

    def zeroBasedValue_testing(self):
        self.assertEqual(convertFahrenheitToKelvin(0.0), 273.15)

    def decimal_value_testing(self):
        self.assertEqual(convertFahrenheitToKelvin(200.22), 373.37)

    def big_value_testing(self):
        self.assertEqual(convertFahrenheitToKelvin(937538), 937938.15)

    def negative_value_testing(self):
        self.assertEqual(convertFahrenheitToKelvin(-200.0), 173.15)


class KelvinToCelsius(unittest.TestCase):

    def positiveValue_testing(self):
        self.assertEqual(kelvinToCelcius(300.0), 573.15)

    def zeroBasedValue_testing(self):
        self.assertEqual(kelvinToCelcius(0.0), 273.15)

    def decimal_value_testing(self):
        self.assertEqual(kelvinToCelcius(200.22), 373.37)

    def big_value_testing(self):
        self.assertEqual(kelvinToCelcius(937538), 937938.15)

    def negative_value_testing(self):
        self.assertEqual(kelvinToCelcius(-200.0), 173.15)


class KelvinToFarenheit(unittest.TestCase):

    def positiveValue_testing(self):
        self.assertEqual(convertKelvinToFahrenheit(300.0), 573.15)

    def zeroBasedValue_testing(self):
        self.assertEqual(convertKelvinToFahrenheit(0.0), 273.15)

    def decimal_value_testing(self):
        self.assertEqual(convertKelvinToFahrenheit(200.22), 373.37)

    def big_value_testing(self):
        self.assertEqual(convertKelvinToFahrenheit(937538), 937938.15)

    def negative_value_testing(self):
        self.assertEqual(convertKelvinToFahrenheit(-200.0), 173.15)


if __name__ == "__main__":
    unittest.main()