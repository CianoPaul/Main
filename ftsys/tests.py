from django.test import TestCase
from ftsys.views import MainPage
from ftsys.models import Item

'''
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.urls import resolve
'''

class HomePageTest(TestCase):
	def test_mainpage_as_seen_client(self):
	   response=self.client.get('/')
	   self.assertTemplateUsed(response,'mainpage.html')
	   
	def test_responding_post_request(self):
	   response = self.client.post('/', data={'fitness1':'NewSurname'})
	   self.assertIn('NewSurname',response.content.decode())
	   self.assertTemplateUsed(response, 'mainpage.html')
	"""
	def test_mainpage_responding_view(self):
	   response=self.client.get('/')
		'''
	   request = HttpRequest()
	   response = MainPage(request)
		'''
	   html = response.content.decode('utf8')
		'''
	   self.assertTrue(html.startswith('<!DOCTYPE html>'))
	   self.assertIn('<title>Tinkle Out Loud</title>',html)
	   self.assertTrue(html.endswith(''))'''
	   stringPage=render_to_string('mainpage.html')
	   self.assertEqual(html,stringPage)
	   self.assertTemplateUsed(response,'mainpage.html')
		"""
class ORMTest(TestCase):
	def test_saving_retrieving_list(self):
	   txtItem1 = Item()
	   txtItem1.text = 'Item one'
	   txtItem1.save()
	   txtItem2 = Item()
	   txtItem2.text = 'Item two'
	   txtItem2.save()
	   savedItems = Item.objects.all()
	   self.assertEqual(savedItems.count(),2)
	   savedItem1 = savedItems[0]
	   savedItem2 = savedItems[1]
	   self.assertEqual(savedItem1.text, 'Item one')
	   self.assertEqual(savedItem2.text, 'Item two')
