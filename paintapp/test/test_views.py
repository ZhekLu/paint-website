from django.test import TestCase
from django.urls import reverse


class NewPaintViewTest(TestCase):
    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/paintapp/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('paintapp:new_paint'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('paintapp:new_paint'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'paintapp/new_paint.html')


class OldPaintViewTest(TestCase):
    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/paintapp/old/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('paintapp:old_paint'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('paintapp:old_paint'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'paintapp/old_paint.html')


class InfoViewTest(TestCase):
    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/paintapp/info/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('paintapp:info'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('paintapp:info'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'paintapp/info.html')
