from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select
from django.test import LiveServerTestCase

class PageTest(LiveServerTestCase): 
   def setUp(self):
      self.browser = webdriver.Firefox()
   #def tearDown(self):
      #self.browser.quit()
      
   def test_enter_and_retrieve(self):
      self.browser.get(self.live_server_url)
      self.assertIn('Fitness-Talk',self.browser.title)
      headerText = self.browser.find_element_by_tag_name('h1').text
      self.assertIn('Fitness-talk Registration', headerText)
      inpSurname = self.browser.find_element_by_id('Snameid')
      inpSurname.send_keys('Ciano')
      time.sleep(1)
      
      btnConfirm = self.browser.find_element_by_id('btnConfirm')
      self.assertEqual(inpSurname.get_attribute('placeholder'), 'Enter your Last name here.')
      
      inpFname = self.browser.find_element_by_id('Fnameid')
      inpFname.click()
      inpFname.send_keys('JP')
      
      inpMname = self.browser.find_element_by_id('Mnameid')
      inpMname.click()
      inpMname.send_keys('Monter')
      
      inpAge = self.browser.find_element_by_id('Ageid')
      inpAge.click()
      inpAge.send_keys('21')
      
      inpAddress = self.browser.find_element_by_id('Addressid')
      inpAddress.click()
      inpAddress.send_keys('Blk 9 Lot 9, Chester Place Mansfield st. Dasmarinas City, Cavite')
      
      inpContact = self.browser.find_element_by_id('Contactid')
      inpContact.click()
      inpContact.send_keys('09473230371')
      
      inpSpecify = self.browser.find_element_by_id('Specifyid')
      inpSpecify.click()
      inpSpecify.send_keys('NONE')
      
      inpTotal = self.browser.find_element_by_id('Totalid')
      inpTotal.click()
      inpTotal.send_keys('₱700')
      
      Dropbox1 = self.browser.find_element_by_id('dropdownid')
      Dropbox1 = Select (Dropbox1)
      Dropbox1.select_by_visible_text('NONE')
      
      Dropbox2 = self.browser.find_element_by_id('dropdownid2')
      Dropbox2 = Select (Dropbox2)
      Dropbox2.select_by_visible_text('3 MONTHS')
            
      btnConfirm.click()
      '''
      inputbox.send_keys(Keys.ENTER)
      time.sleep(1)
      table = self.browser.find_element_by_tag_name('tr')
      self.assertTrue(any(row.text == '1: Mickey Mouse'))
      self.fail('Finish the test!')
      '''
      table = self.browser.find_element_by_tag_name('table')
      rows = table.find_elements_by_tag_name('tr')
      self.assertIn('1: Ciano,JP,Monter,21,Blk 9 Lot 9, Chester Place Mansfield st. Dasmarinas City, Cavite,09473230371,NONE,NONE,3 Months,₱700', [row.text for row in rows])
      #self.assertTrue(any(rows.text == '1: JP Pogi'),"No table yet!")

#------2nd Window
   def test_enter_and_retrieve_2(self):
      self.browser.get(self.live_server_url)
      self.assertIn('Fitness-Talk',self.browser.title)
      headerText = self.browser.find_element_by_tag_name('h1').text
      self.assertIn('Fitness-talk Registration', headerText)
      inpSurname = self.browser.find_element_by_id('Snameid')
      inpSurname.send_keys('Ciano')
      time.sleep(1)
      
      btnConfirm = self.browser.find_element_by_id('btnConfirm')
      self.assertEqual(inpSurname.get_attribute('placeholder'), 'Enter your Last name here.')
      
      inpFname = self.browser.find_element_by_id('Fnameid')
      inpFname.click()
      inpFname.send_keys('JP')
      
      inpMname = self.browser.find_element_by_id('Mnameid')
      inpMname.click()
      inpMname.send_keys('Monter')
      
      inpAge = self.browser.find_element_by_id('Ageid')
      inpAge.click()
      inpAge.send_keys('21')
      
      inpAddress = self.browser.find_element_by_id('Addressid')
      inpAddress.click()
      inpAddress.send_keys('Blk 9 Lot 9, Chester Place Mansfield st. Dasmarinas City, Cavite')
      
      inpContact = self.browser.find_element_by_id('Contactid')
      inpContact.click()
      inpContact.send_keys('09473230371')
      
      inpSpecify = self.browser.find_element_by_id('Specifyid')
      inpSpecify.click()
      inpSpecify.send_keys('NONE')
      
      inpTotal = self.browser.find_element_by_id('Totalid')
      inpTotal.click()
      inpTotal.send_keys('₱700')
      
      Dropbox1 = self.browser.find_element_by_id('dropdownid')
      Dropbox1 = Select (Dropbox1)
      Dropbox1.select_by_visible_text('NONE')
      
      Dropbox2 = self.browser.find_element_by_id('dropdownid2')
      Dropbox2 = Select (Dropbox2)
      Dropbox2.select_by_visible_text('3 MONTHS')
            
      btnConfirm.click()

#-----2nd
      self.browser.get(self.live_server_url)
      self.assertIn('Fitness-Talk',self.browser.title)
      headerText = self.browser.find_element_by_tag_name('h1').text
      self.assertIn('Fitness-talk Registration', headerText)
      inpSurname = self.browser.find_element_by_id('Snameid')
      inpSurname.send_keys('Kaedehara')
      time.sleep(1)
      
      btnConfirm = self.browser.find_element_by_id('btnConfirm')
      self.assertEqual(inpSurname.get_attribute('placeholder'), 'Enter your Last name here.')
      
      inpFname = self.browser.find_element_by_id('Fnameid')
      inpFname.click()
      inpFname.send_keys('Kazuha')
      
      inpMname = self.browser.find_element_by_id('Mnameid')
      inpMname.click()
      inpMname.send_keys('Dimatibag')
      
      inpAge = self.browser.find_element_by_id('Ageid')
      inpAge.click()
      inpAge.send_keys('23')
      
      inpAddress = self.browser.find_element_by_id('Addressid')
      inpAddress.click()
      inpAddress.send_keys('Inazuma')
      
      inpContact = self.browser.find_element_by_id('Contactid')
      inpContact.click()
      inpContact.send_keys('09573430372')
      
      inpSpecify = self.browser.find_element_by_id('Specifyid')
      inpSpecify.click()
      inpSpecify.send_keys('NONE')
      
      inpTotal = self.browser.find_element_by_id('Totalid')
      inpTotal.click()
      inpTotal.send_keys('₱1200')
      
      Dropbox1 = self.browser.find_element_by_id('dropdownid')
      Dropbox1 = Select (Dropbox1)
      Dropbox1.select_by_visible_text('NONE')
      
      Dropbox2 = self.browser.find_element_by_id('dropdownid2')
      Dropbox2 = Select (Dropbox2)
      Dropbox2.select_by_visible_text('6 MONTHS')
            
      btnConfirm.click()

      '''
      inputbox.send_keys(Keys.ENTER)
      time.sleep(1)
      table = self.browser.find_element_by_tag_name('tr')
      self.assertTrue(any(row.text == '1: Mickey Mouse'))
      self.fail('Finish the test!')
      '''
      table = self.browser.find_element_by_tag_name('table')
      rows = table.find_elements_by_tag_name('tr')
      self.assertIn('1: Ciano,JP,Monter,21,Blk 9 Lot 9, Chester Place Mansfield st. Dasmarinas City, Cavite,09473230371,NONE,NONE,3 Months,₱700', [row.text for row in rows])
      self.assertIn('2: Kaedehara,Kazuha,Dimatibag,23,Inazuma,09573430372,NONE,NONE,6 Months,₱1200', [row.text for row in rows])
      #self.assertTrue(any(rows.text == '1: JP Pogi'),"No table yet!")

# if __name__=='__main__':
#       unittest.main(warnings='ignore')