from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time

class PageTest(unittest.TestCase):
   def setUp(self):
      self.browser = webdriver.Firefox()
   #def tearDown(self):
      #self.browser.quit()
      
   def test_enter_and_retrieve(self):
      self.browser.get('http://localhost:8000')
      self.assertIn('Fitness-Talk',self.browser.title)
      headerText = self.browser.find_element_by_tag_name('h1').text
      self.assertIn('Fitness-talk header 1', headerText)
      inpName = self.browser.find_element_by_id('fitness1')
      self.assertEqual(inpName.get_attribute('placeholder'),'Enter your name here.')
      inpName.click()
      inpName.send_keys('Mickey Mouse')
      time.sleep(1)
      '''
      inputbox.send_keys(Keys.ENTER)
      time.sleep(1)
      table = self.browser.find_element_by_tag_name('tr')
      self.assertTrue(any(row.text == '1: Mickey Mouse'))
      self.fail('Finish the test!')
      '''
      
if __name__=='__main__':
      unittest.main(warnings='ignore')
