import unittest
from city_functions import city_country

class CityTestCase(unittest.TestCase):
    
    def test_city_country(self):
        """Do 'santiago' 'chile' output 'like Santiagao, Chile'"""
        formatted_city = city_country('santiagao','chile')
        self.assertEqual(formatted_city, 'Santiagao, Chile')

if __name__ == '__main__':
    unittest.main()
