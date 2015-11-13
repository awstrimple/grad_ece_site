from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)
        
    def tearDown(self):
        self.browser.quit()

    def test_homepage_has_links_to_forms(self):

        # Xiao has heard that there is a new ECE website that Amy and Tony
        # really want her to use for filling out forms. So she opens up
        # firefox and checks out the page

        self.browser.get('http://localhost:8000')

        # She notices that the page title and header mention
        # the ECE Graduate Program

        self.assertIn('ECE Graduate Program', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('ECE Graduate Program', header_text)

        # Xiao sees that there is a button labeled "MS Program of Study"
        button_text = self.browser.find_element_by_tag_name('button').text
        self.assertEqual(button_text, "MS Program of Study")

        # She clicks on it, and is brought to another page with
        # a form entitled "MS Program of Study", with a place to
        # input her first name
        button = self.browser.find_element_by_tag_name('button')
        button.click()
        self.assertIn('MS POS', self.browser.title)
        ms_pos_form = self.browser.find_element_by_id('ms_pos_form')
        
        inputs = ms_pos_form.find_elements_by_tag_name('input')
        self.assertTrue(
            any(input.get_attribute('name') == 'first_name' for input in inputs)
            )
        
        # so she goes back to studying for 551.
        self.fail("finish writing the FT!!")

if __name__ == '__main__':
    unittest.main()
