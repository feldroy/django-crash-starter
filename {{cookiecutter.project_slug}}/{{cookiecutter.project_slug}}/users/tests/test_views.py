import pytest
from django.test import RequestFactory
from django.contrib.messages.middleware import MessageMiddleware
from django.contrib.sessions.middleware import SessionMiddleware
from django.urls import reverse

from {{ cookiecutter.project_slug }}.users.models import User
from {{ cookiecutter.project_slug }}.users.views import (
    UserRedirectView,
    UserUpdateView,
)

pytestmark = pytest.mark.django_db


class TestUserUpdateView:
    """
    TODO:
        extracting view initialization code as class-scoped fixture
        would be great if only pytest-django supported non-function-scoped
        fixture db access -- this is a work-in-progress for now:
        https://github.com/pytest-dev/pytest-django/pull/258
    """

    def test_get_success_url(
        self, user: User, request_factory: RequestFactory
    ):
        view = UserUpdateView()
        request = request_factory.get("/fake-url/")
        request.user = user

        view.request = request

        assert view.get_success_url() == f"/users/{user.username}/"

    def test_get_object(
        self, user: User, request_factory: RequestFactory
    ):
        view = UserUpdateView()
        request = request_factory.get("/fake-url/")
        request.user = user

        view.request = request

        assert view.get_object() == user

    def test_form_valid(
        self, user: User, request_factory: RequestFactory
    ):
        form_data = {"name": "John Doe"}
        request = request_factory.post(
            reverse("users:update"), form_data
        )
        request.user = user
        session_middleware = SessionMiddleware()
        session_middleware.process_request(request)
        msg_middleware = MessageMiddleware()
        msg_middleware.process_request(request)

        response = UserUpdateView.as_view()(request)
        user.refresh_from_db()

        assert response.status_code == 302
        assert user.name == form_data["name"]


class TestUserRedirectView:
    def test_get_redirect_url(
        self, user: User, request_factory: RequestFactory
    ):
        view = UserRedirectView()
        request = request_factory.get("/fake-url")
        request.user = user

        view.request = request

        assert (
            view.get_redirect_url() == f"/users/{user.username}/"
        )
