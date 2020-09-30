import unittest
from city_functions import city_country

class CityTestCase(unittest.TestCase):
    
    def test_city_country(self):
        """Do 'santiago' 'chile' output 'like Santiago, Chile'"""
        formatted_city = city_country('santiago','chile')
        self.assertEqual(formatted_city, 'Santiago, Chile')

    def test_city_country_population(self):
        """Do 'santiago' 'chile' 'population=50000' output 'like Santiago, Chile population=50000'"""
        formatted_city = city_country('santiago', 'chile', '50000')
        self.assertEqual(formatted_city, 'Santiago, Chile -Population 50000')
        

if __name__ == '__main__':
    unittest.main()
