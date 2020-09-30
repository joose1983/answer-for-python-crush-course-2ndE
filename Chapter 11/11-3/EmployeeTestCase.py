import unittest
from Employee import Employee

class EmployeeTestCase(unittest.TestCase):

    def setUp(self):
        self.employee1=Employee('jackie','qin',10000)
        self.old_annual_salary=self.employee1.annual_salary
        
    def test_give_default_raise(self):
        self.employee1.give_raise()
        self.assertEqual(self.employee1.annual_salary,self.old_annual_salary+5000)

    def test_give_custom_raise(self):
        self.employee1.give_raise(200)
        self.assertEqual(self.employee1.annual_salary, self.old_annual_salary+200)

if __name__=='__main__':
    unittest.main()
    
    

    
        
