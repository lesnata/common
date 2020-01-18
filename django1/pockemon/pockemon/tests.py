from http import HTTPStatus

from django.http import request
from django.test import TestCase
from django.test import Client

from django.urls import reverse
from .views import good_reads


class StatusViewtests(TestCase):
    client = Client()

    def test_health_check_view(self):
        response = self.client.get(reverse("health_check"))
        assert response.status_code == HTTPStatus.OK

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        assert response.status_code == HTTPStatus.OK

    def test_good_reads_view(self):
        response = self.client.get(reverse("good_reads"))
        assert response.status_code == HTTPStatus.OK

