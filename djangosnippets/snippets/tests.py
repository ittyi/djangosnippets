from django.contrib.auth import get_user_model
from django.test import TestCase, RequestFactory

from snippets.models import Snippet
from snippets.views import top

UserModel = get_user_model()

# Create your tests here.
class CreateSnippetTest(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create(
            username="test_user",
            email="test@example.com",
            password="secret",
        )
        self.client.force_login(self.user)

    def test_render_creation_form(self):
        response = self.client.get("/snippets/new/")
        self.assertContains(response, "スニペットの登録", status_code=200)

    def test_create_snippet(self):
        data = {'title': 'タイトル', 'code': 'コード', 'description': '解説'}
        self.client.post("/snippets/new/", data)
        snippet = Snippet.objects.get(title='タイトル')
        self.assertEqual('コード', snippet.code)
        self.assertEqual('解説', snippet.description)