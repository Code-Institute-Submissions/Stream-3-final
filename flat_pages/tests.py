from unittest import TestCase
from django.shortcuts import render_to_response

class SimpleTest(TestCase):
    def test_adding_something_simple(self):
        self.assertEqual(1 + 2, 3)

    def test_adding_something_isnt_equal(self):
        self.assertNotEqual(1 + 2, 4)

    def test_flat_page_status_code_is_ok(self):
        flat_page = self.client.get('/pages/about/')
        self.assertEqual(flat_page.status_code, 200)

    #def test_check_content_is_correct(self):
    #    flat_page = self.client.get('/pages/about/')
    #    self.assertTemplateUsed(flat_page, "flatpages.html")
     ##   flat_page_template_output = render_to_response("flatpages.html").content
    #    self.assertEqual(flat_page.content, flat_page_template_output)
