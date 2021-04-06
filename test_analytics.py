#module to manage unit testing of Analytics server logic
import unittest
from analytics import Analytics


class TestAnalytics(unittest.TestCase):
    ''' Test Class to test Class Analytics '''
    test_data = Analytics("2019-08-01")
    test_data.get_analytics()

    # test the customer count for "2019-08-01"
    def testCustomers(self):
        self.assertEqual(TestAnalytics.test_data.output['customers'],9)
    
    # test the total_discount_amount for "2019-08-01"
    def test_total_discount_amount(self):
        self.assertAlmostEqual(TestAnalytics.test_data.output['total_discount_amount'],130429980.24)

    # test the total items sold for "2019-08-01"
    def test_items(self):
        self.assertEqual(TestAnalytics.test_data.output['items'],2895)
    
    # The average order total for "2019-08-01"
    def test_order_total_average(self):
        self.assertAlmostEqual(TestAnalytics.test_data.output['order_total_average'],15895179.73)

    # The average discount rate applied to the items sold for "2019-08-01"
    def test_discount_rate_avg(self):
        self.assertAlmostEqual(TestAnalytics.test_data.output['discount_rate_avg'],0.13)
 
    # The total amount of commissions generated for "2019-08-01"
    def test_commissions_total(self):
        self.assertAlmostEqual(TestAnalytics.test_data.commissions['total'],20833236.94)



 
 
# run the tests

myTest = TestAnalytics()

try:
    myTest.testCustomers()
    print("Test Passed",'myTest.testCustomers()')
except AssertionError as e:
    print('####TEST FAILED#####', 'myTest.testCustomers()', e)

try:
    myTest.test_total_discount_amount()
    print("Test Passed",'myTest.test_total_discount_amount()')
except AssertionError as e:
    print('####TEST FAILED#####', 'myTest.test_total_discount_amount()', e)

try:
    myTest.test_items()
    print("Test Passed",'myTest.test_items()')
except AssertionError as e:
    print('####TEST FAILED#####', 'myTest.test_items()', e)

try:
    myTest.test_order_total_average()
    print("Test Passed",'myTest.test_order_total_average()')
except AssertionError as e:
    print('####TEST FAILED#####', 'myTest.test_order_total_average()', e)

try:
    myTest.test_discount_rate_avg()
    print("Test Passed",'myTest.discount_rate_avg()')
except AssertionError as e:
    print('####TEST FAILED#####', 'myTest.discount_rate_avg()', e)

try:
    myTest.test_commissions_total()
    print("Test Passed",'myTest.test_commissions_total()')
except AssertionError as e:
    print('####TEST FAILED#####', 'myTest.test_commissions_total()', e)

 

