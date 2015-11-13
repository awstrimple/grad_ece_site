from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
        
    def tearDown(self):
        self.browser.quit()

    def test_homepage_has_links_to_forms(self):

        # Xiao has heard that there is a new ECE website that Amy and Tony
        # really want her to use for filling out forms. So she opens up
        # firefox and checks out the page

        self.browser.get('http://localhost:8000')

        # She notices that the page title and header mention the ECE Graduate Program

        self.assertIn('ECE Graduate Program', self.browser.title)
        self.fail('Finish the test!')

        # Xiao sees that there are several links to various forms. One of them says
        # 'PhD Program of Study Form', another says 'MS Program of Study Form', and
        # another says 'MEng Program of Study Form'

        # She clicks on each of these in turn, and stuff happens. It's very satisfying,
        # so she goes back to studying for 551.

if __name__ == '__main__':
    unittest.main()
