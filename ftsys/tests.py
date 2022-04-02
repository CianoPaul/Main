from django.test import TestCase
from ftsys.views import MainPage
'''
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.urls import resolve
'''

class HomePageTest(TestCase):
	def test_mainpage_as_seen_client(self):
	   response=self.client.get('/')
	   self.assertTemplateUsed(response,'mainpage.html')
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
