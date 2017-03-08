from rest_framework import serializers
from .models.product import Product
from .models.order import Order
from .models.order import OrderProduct
from .models.payment_type import PaymentType
from .models.product_type import ProductType
from .models.customer import Customer
from django.contrib.auth.models import User


class ProductTypeSerializer(serializers.HyperlinkedModelSerializer):
    """
    Class for data serialization of a specific Model: ProductCategory
    """

    class Meta:
        model = ProductType
        fields = '__all__'


class OrderProductSerializer(serializers.ModelSerializer):
    """
    Class for data serialization of a specific Model: ProductOrder
    """

    class Meta:
        model = OrderProduct
        fields = '__all__'
        depth = 2


class OrderSerializer(serializers.ModelSerializer):
    """
    Class for data serialization of a specific Model: Order
    Added ProductOorderSerializer to make nested serializers in the
        OrderSerializer
    """
    # product_orders = OrderProductSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = '__all__'
        depth = 1


class UserSerializer(serializers.ModelSerializer):
    """
    Class for data serialization of a specific Model: User
    If user is not staff, This UserSerializer will be picked up on the
        ViewSet
    """

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',)
        extra_kwargs = {'email': {'write_only': True}, 'username': {'write_only': True}}
        depth = 0


class UserStaffSerializer(serializers.ModelSerializer):
    """
    Class for data serialization of a specific Model: User
    If user is_staff, This UserStaffSerializer will be picked up on
        the ViewSet
    Added Orderserializer to make nested serializers in the
        UserStaffSerializer
    """

    class Meta:
        model = User 
        fields = '__all__'
        depth = 0


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    """
    """
    orders = OrderSerializer(many=True, read_only=True)
    user = UserSerializer()

    class Meta:
        model = Customer
        fields = '__all__'
        depth = 1


class ProductSerializer(serializers.ModelSerializer):
    """
    Class for data serialization of a specific Model: Product
    """

    class Meta:
        model = Product
        fields = '__all__'
        depth = 0


class PaymentTypeSerializer(serializers.HyperlinkedModelSerializer):    
    """
    Class for data serialization of a specific Model: Payment Method
    Sets user serializer to only show sensitive imformation to superusers
    """

    class Meta:
        model = PaymentType
        fields = '__all__'
