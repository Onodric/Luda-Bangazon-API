from .models.product import Product
from .models.order import Order
from .models.order import OrderProduct
from .models.payment_type import PaymentType
from .models.product_type import ProductType
from .models.customer import Customer
from .serializers import *
from django.contrib.auth.models import User
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponse, HttpResponseRedirect, Http404
# from django.views.decorators.csrf import csrf_exempt
import json


def logincustomer_view(request):
    """
    """

    permission_classes = (AllowAny,)

    req_body = json.loads(request.body.decode())
    username = req_body['username']
    password = req_body['password']
    user = authenticate(username=username, password=password)

    success = False
    if user is not None:
        if user.is_active:
            login(request, user)
            data = json.dumps({
                'success': True,
                'username': user.username,
                'email': user.email,
            })
            return HttpResponse(data, content_type='application/json')

        return HttpResponse(self._error_response('disabled'), content_type='application/json')
    return HttpResponse(self._error_response('invalid'), content_type='application/json')


class LoginView(generics.RetrieveAPIView):
    """
    """

    permission_classes = (AllowAny,)

    error_messages = {
        'invalid': "Invalid username or password",
        'disabled': "Sorry, this account is suspended",
    }

    def _error_response(self, message_key):
        data = json.dumps({
            'success': False,
            'message': self.error_messages[message_key],
            'user_id': None,
        })

    def post(self, request):

        return logincustomer_view(request)


class RegisterView(generics.RetrieveAPIView):
    """
    """

    permission_classes = (AllowAny,)

    error_messages = {
        'invalid': "Invalid username or password",
        'disabled': "Sorry, this account is suspended",
    }

    def _error_response(self, message_key):
        data = json.dumps({
            'success': False,
            'message': self.error_messages[message_key],
            'user_id': None,
        })

    @csrf_exempt
    def post(self,request):
        permission_classes = (AllowAny,)

        req_body = json.loads(request.body.decode())
        print(req_body)
        user = User.objects.create_user(
            username = req_body['username'],
            password = req_body['password'],
            email = req_body['email'],
            first_name = req_body['first_name'],
            last_name = req_body['last_name']
            )
        customer = customer_model.Customer.objects.create(
            user = user,
            phone = req_body['phone'],
            shipping_address=req_body['shipping_address']
            )
        return logincustomer_view(request)


class UserViewSet(viewsets.ModelViewSet):
    """
    The User View provides the `list`, `create`, and `retrieve` actions.
    Please click on a specific User's url for the `update` and `destroy` actions.
    If user is not a staff, This will be the UserView
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    """
    The Customer View provides the `list`, `create`, and `retrieve` actions.
    Please click on a specific Customer's url for the `update` and `destroy` actions.
    If user is not a staff, This will be the CustomerView
    """

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class OrderViewSet(viewsets.ModelViewSet):
    """
    The Order View provides the `list`, `create`, and `retrieve` actions.
    Please click on a specific Order's url for the `update` and `destroy` actions.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class PaymentTypeViewSet(viewsets.ModelViewSet):
    """
    The Payment Method View provides the `list`, `create`, and `retrieve` actions.
    Please click on a specific Method's url for the `update` and `destroy` actions.
    """
    queryset = PaymentType.objects.all()
    serializer_class = PaymentTypeSerializer


class ProductTypeViewSet(viewsets.ModelViewSet):
    """
    The Product Category View provides the `list`, `create`, and `retrieve` actions.
    Please click on a specific Category's url for the `update` and `destroy` actions.
    """
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer


class OrderProductViewSet(viewsets.ModelViewSet):
    """
    The Product/Order View provides the `list`, `create`, and `retrieve` actions.
    Please click on a specific item's url for the `update` and `destroy` actions.
    """
    queryset = OrderProduct.objects.all()
    serializer_class = OrderProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    The Product View provides the `list`, `create`, and `retrieve` actions.
    Please click on a specific Product's url for the `update` and `destroy` actions.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
