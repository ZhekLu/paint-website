from django.test import TestCase
from django.urls import reverse
import json

from paintsite.tasks import comments_notification


class LoginFormTest(TestCase):

    def test_task(self):
        assert comments_notification.run()
        assert comments_notification.run()
        assert comments_notification.run()

    # def test_task_status(self):
    #     response = self.client.post(reverse("run_task"), {"type": 0})
    #     content = json.loads(response.content)
    #     task_id = content["task_id"]
    #     assert response.status_code == 202
    #     assert task_id
    #
    #     response = client.get(reverse("get_status", args=[task_id]))
    #     content = json.loads(response.content)
    #     assert content == {"task_id": task_id, "task_status": "PENDING", "task_result": Нет}
    #     assert response.status_code == 200
    #
    #     while content["task_status"] == "PENDING":
    #         response = client.get(reverse("get_status", args=[task_id]))
    #         content = json.loads(response.content)
    #     assert content == {"task_id": task_id, "task_status": "SUCCESS", "task_result": True}
