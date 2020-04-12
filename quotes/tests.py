from django.test import Client, TestCase 
from django.urls import reverse

from .models import Quote

class QuoteTests(TestCase):

    def setUp(self): self.quote = Quote.objects.create( 
        subject='Harry Potter', 
        author='JK Rowling', 
        quote='Medicine is a science.',
        reference='https://www.google.com/search?q=Medicin+is+a+Science',
        year='1967', 
        )

    def test_quote_listing(self): 
        self.assertEqual(f'{self.quote.subject}', 'Harry Potter') 
        self.assertEqual(f'{self.quote.author}', 'JK Rowling') 
        self.assertEqual(f'{self.quote.quote}', 'Medicine is a science.')
        self.assertEqual(f'{self.quote.reference}', 'https://www.google.com/search?q=Medicin+is+a+Science')
        self.assertEqual(f'{self.quote.year}', '1967')

    def test_quote_list_view(self): 
        response = self.client.get(reverse('quote_list')) 
        self.assertEqual(response.status_code, 200) 
        self.assertContains(response, 'Harry Potter') 
        self.assertTemplateUsed(response, 'quotes/quote_list.html')

    def test_quote_detail_view(self): 
        response = self.client.get(self.quote.get_absolute_url()) 
        no_response = self.client.get('/quotes/12345/') 
        self.assertEqual(response.status_code, 200) 
        self.assertEqual(no_response.status_code, 404) 
        self.assertContains(response, 'JK Rowling') 
        self.assertTemplateUsed(response, 'quotes/quote_detail.html')

