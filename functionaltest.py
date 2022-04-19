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
      inpName.send_keys('JP Pogi')
      time.sleep(1)
      
      btnConfirm.click()
      '''
      inputbox.send_keys(Keys.ENTER)
      time.sleep(1)
      table = self.browser.find_element_by_tag_name('tr')
      self.assertTrue(any(row.text == '1: Mickey Mouse'))
      self.fail('Finish the test!')
      '''
      table = self.browser.find_element_by_id('registryTable')
      rows = table.find_elements_by_tag_name('tr')
      self.assertIn('1:JP Pogi',[rows.text for row in rows])
      #self.assertTrue(any(row.text == '1: JP Pogi'),"No table!")
      
   def checking_if_in_table_list(self,row_test):
      table = self.browser.find_element_by_id('registryTable')
      rows = table.find_element_by_tag_name('tr')
      self.assertIn(row_text,[rows.text for row in rows])
      
if __name__=='__main__':
      unittest.main(warnings='ignore')
