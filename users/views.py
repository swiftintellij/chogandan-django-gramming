from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.db import IntegrityError
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt


class JsonResponseUtilsMixin(object):
    @staticmethod
    def response(data={}, message="", status=200):
        result = {
            "data": data,
            "message": message,
        }
        return JsonResponse(result)

    @staticmethod
    def failed_response(data={}, message="", status=400):
        result = {
            "data": data,
            "message": message,
        }
        return JsonResponse(result)


class ApiView(JsonResponseUtilsMixin, View):
    pass


@method_decorator(csrf_exempt, name="dispatch")
class UserJoinView(ApiView):

    def post(self, request):
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        email = request.POST.get("email", "")

        if not username:
            return self.failed_response(message="아이디를 입력하세요.")
        if not password:
            return self.failed_response(message="암호를 입력하세요.")
        if not email:
            return self.failed_response(message="이메일을 입력하세요.")

        try:
            validate_email(email)
            user = User.objects.create_user(username=username, password=password, email=email)
        except ValidationError:
            return self.failed_response(message="이메일 형식에 맞지 않습니다.")
        except IntegrityError:
            return self.response(message="회원 가입이 실패했습니다.", status=400)

        return self.response({
                "id": str(user.id),
                "username": user.username,
                "email": user.email,
                "created_at": user.date_joined.strftime("%Y-%m-%d %H:%M:%S"),
            }, message="환영합니다.")


@method_decorator(csrf_exempt, name="dispatch")
class UserLoginView(ApiView):
    def post(self, request):
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        if not username:
            return self.failed_response(message="아이디를 입력하세요")
        if not password:
            return self.failed_response(message="암호를 입력하세요")

        user = authenticate(request, username=username, password=password)
        if user is None:
            return self.failed_response("아이디와 암호가 틀립니다.")

        login(request, user)

        return self.response({
            "username": user.username,
            "email": user.email
        }, message="로그인 성공")


class UserLogoutView(ApiView):
    def get(self, request):
        logout(request)
        return self.response()


