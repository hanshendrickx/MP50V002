from django.test import SimpleTestCase
from django.urls import reverse, resolve

from .views import HomeStaticpageView, AboutStaticpageView # new


class HomepageTests(SimpleTestCase):

    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'home.html')

    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, 'Homepage')

    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(
            self.response, 'Hi there! I should not be on the page.')

    def test_homepage_url_resolves_homestaticpageview(self): # new
        view = resolve('/')
        self.assertEqual(
            view.func.__name__,
            HomeStaticpageView.as_view().__name__
        )

class AboutStaticpageTests(SimpleTestCase): # new

    def setUp(self): 
        url = reverse('about') 
        self.response = self.client.get(url)

    def test_aboutstaticpage_status_code(self): 
        self.assertEqual(self.response.status_code, 200)

    def test_aboutstaticpage_template(self): 
        self.assertTemplateUsed(self.response, 'about.html')

    def test_aboutstaticpage_contains_correct_html(self): 
        self.assertContains(self.response, 'About Page')

    def test_aboutstaticpage_does_not_contain_incorrect_html(self): 
        self.assertNotContains( self.response, 'Hi there! I should not be on the page.')

    def test_aboutStaticpage_url_resolves_aboutStaticpageview(self): 
        view = resolve('/about/') 
        self.assertEqual( 
            view.func.__name__, 
            AboutStaticpageView.as_view().__name__ )        