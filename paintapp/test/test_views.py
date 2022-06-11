from django.test import TestCase
from django.urls import reverse
from parameterized import parameterized


class TestViewsSequence(TestCase):
    @parameterized.expand([
        ['paint', '/paintapp/', 'paintapp:new_paint', 'paintapp/new_paint.html'],
        ['old', '/paintapp/old/', 'paintapp:old_paint', 'paintapp/old_paint.html'],
        ['info', '/paintapp/info/', 'paintapp:info', 'paintapp/info.html'],
    ])
    def test_sequence(self, name, url_path, reverse_path, template_path):
        def test_view_url_exists_at_desired_location():
            resp = self.client.get(url_path)
            self.assertEqual(resp.status_code, 200)

        def test_view_url_accessible_by_name():
            resp = self.client.get(reverse(reverse_path))
            self.assertEqual(resp.status_code, 200)

        def test_view_uses_correct_template():
            resp = self.client.get(reverse(reverse_path))
            self.assertEqual(resp.status_code, 200)
            self.assertTemplateUsed(resp, template_path)

        test_view_url_exists_at_desired_location()
        test_view_url_accessible_by_name()
        test_view_uses_correct_template()

