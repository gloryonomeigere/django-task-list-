from django.test import TestCase
from django.urls import reverse
from .models import Task

# Create your tests here.


class TaskModelTest(TestCase):

    def test_task_creation(self):
        task = Task.objects.create(
            title="Learn DevOps",
            description="Study CI/CD and Jenkins"
        )

        self.assertEqual(task.title, "Learn DevOps")
        self.assertEqual(task.description, "Study CI/CD and Jenkins")
        self.assertFalse(task.completed)

    def test_task_string_representation(self):
        task = Task.objects.create(
            title="Learn Django",
            description="Continue backend development"
        )

        self.assertEqual(str(task), "Learn Django")


class TaskViewTest(TestCase):

    def test_task_list_page_loads(self):
        response = self.client.get(reverse("task_list"))

        self.assertEqual(response.status_code, 200)

    def test_task_creation(self):
        response = self.client.post(
            reverse("task_create"),
            {
                "title": "Test task",
                "description": "Testing task creation"
            }
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.count(), 1)

    def test_task_update(self):
        task = Task.objects.create(
            title="Old title",
            description="Old description"
        )

        response = self.client.post(
            reverse("task_update", args=[task.pk]),
            {
                "title": "Updated title",
                "description": "Updated description"
            }
        )

        self.assertEqual(response.status_code, 302)

        task.refresh_from_db()

        self.assertEqual(task.title, "Updated title")
        self.assertEqual(task.description, "Updated description")
