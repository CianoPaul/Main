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
	   response = self.client.post('/', data={'Sname':'Ciano',
	   	'Fname':'JP',
	   	'Mname':'Monter',
	   	'Age':'21',
	   	'Address':'Chester Place',
	   	'Contact':'09473230371',
	   	'Dropdown':'None',
	   	'Specify':'None',
	   	'Dropdown2':'3 Months',
	   	'Total':'700'})
	   
	   self.assertEqual(Item.objects.count(), 1)
	   newItem = Item.objects.first()
	   self.assertEqual(newItem.sname, 'Ciano')
	   self.assertEqual(newItem.fname, 'JP')
	   self.assertEqual(newItem.mname, 'Monter')
	   self.assertEqual(newItem.age, '21')
	   self.assertEqual(newItem.add, 'Chester Place')
	   self.assertEqual(newItem.contact, '09473230371')
	   self.assertEqual(newItem.disease, 'None')
	   self.assertEqual(newItem.specifydisease, 'None')
	   self.assertEqual(newItem.plan, '3 Months')
	   self.assertEqual(newItem.total, '700')
	   
#----------------

	def test_POST_redirect(self):
	   response = self.client.post('/', data={'Sname':'Ciano',
	   	'Fname':'JP',
	   	'Mname':'Monter',
	   	'Age':'21',
	   	'Address':'Chester Place',
	   	'Contact':'09473230371',
	   	'Dropdown':'None',
	   	'Specify':'None',
	   	'Dropdown2':'3 Months',
	   	'Total':'700'})
	   self.assertEqual(response.status_code, 302)
	   self.assertEqual(response['location'], '/')
	
	def test_only_saves_items_if_necessary(self):
		self.client.get('/')
		self.assertEqual(Item.objects.count(), 0)


	# def test_mainpage_responding_view(self):
	#    response=self.client.get('/')
		
	#    request = HttpRequest()
	#    response = MainPage(request)
		
	#    html = response.content.decode('utf8')
		
	#    self.assertTrue(html.startswith('<!DOCTYPE html>'))
	#    self.assertIn('<title>Tinkle Out Loud</title>',html)
	#    self.assertTrue(html.endswith(''))'''
	#    stringPage=render_to_string('mainpage.html')
	#    self.assertEqual(html,stringPage)
	#    self.assertTemplateUsed(response,'mainpage.html')
		

#------------------

class ORMTest(TestCase):
	def test_saving_retrieving_list(self):
	   txtItem1 = Item()
	   txtItem1.sname = 'Rodrigo'
	   txtItem1.fname = 'Roque'
	   txtItem1.mname = 'Bibi'
	   txtItem1.age = '32'
	   txtItem1.add = 'Davao'
	   txtItem1.contact = '012345678910'
	   txtItem1.disease = 'AIDS'
	   txtItem1.specifydisease = 'None'
	   txtItem1.plan = '3 Months'
	   txtItem1.total = '700'
	   txtItem1.save()
	   txtItem2 = Item()
	   txtItem2.sname = 'Naxos'
	   txtItem2.fname = 'Bong'
	   txtItem2.mname = 'Bing'
	   txtItem2.age = '37'
	   txtItem2.add = 'Makati'
	   txtItem2.contact = '012745288914'
	   txtItem2.disease = 'AIDS'
	   txtItem2.specifydisease = 'None'
	   txtItem2.plan = '6 Months'
	   txtItem2.total = '1500'
	   txtItem2.save()
	   savedItems = Item.objects.all()
	   self.assertEqual(savedItems.count(),2)
	   savedItem1 = savedItems[0]
	   savedItem2 = savedItems[1]
	   self.assertEqual(savedItem1.sname, 'Rodrigo')
	   self.assertEqual(savedItem1.fname, 'Roque')
	   self.assertEqual(savedItem1.mname, 'Bibi')
	   self.assertEqual(savedItem1.age, '32')
	   self.assertEqual(savedItem1.add, 'Davao')
	   self.assertEqual(savedItem1.contact, '012345678910')
	   self.assertEqual(savedItem1.disease, 'AIDS')
	   self.assertEqual(savedItem1.specifydisease, 'None')
	   self.assertEqual(savedItem1.plan, '3 Months')
	   self.assertEqual(savedItem1.total, '700')

	   self.assertEqual(savedItem2.sname, 'Naxos')
	   self.assertEqual(savedItem2.fname, 'Bong')
	   self.assertEqual(savedItem2.mname, 'Bing')
	   self.assertEqual(savedItem2.age, '37')
	   self.assertEqual(savedItem2.add, 'Makati')
	   self.assertEqual(savedItem2.contact, '012745288914')
	   self.assertEqual(savedItem2.disease, 'AIDS')
	   self.assertEqual(savedItem2.specifydisease, 'None')
	   self.assertEqual(savedItem2.plan, '6 Months')
	   self.assertEqual(savedItem2.total, '1500')

	def test_template_display_list(self):
		Item.objects.create(sname='Ciano',
	        fname='JP',
	        mname='Monter',
	        age='21',
	        add='Chester Place Dasmarinas City',
	        contact='09473230371',
	        disease='None',
	        specifydisease='None',
	        plan='3 Months',
	        total='700')

		Item.objects.create(sname='Kamisato',
	        fname='Ayato',
	        mname='De Guzman',
	        age='25',
	        add='Inazuma',
	        contact='094564563453',
	        disease='None',
	        specifydisease='None',
	        plan='3 Months',
	        total='700')

		response=self.client.get('/')
		self.assertIn('1: Ciano,JP,Monter,21,Chester Place Dasmarinas City,09473230371,None,None,3 Months,700',response.content.decode())
		self.assertIn('2: Kamisato,Ayato,De Guzman,25,Inazuma,094564563453,None,None,3 Months,700', response.content.decode())