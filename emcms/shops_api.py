from rest_framework import serializers
from . models import Shop,Categories
from rest_framework import viewsets
class CategorySerialiser(serializers.ModelSerializer):
    #shops = serializers.StringRelatedField(many=True)
    class Meta:
        model = Categories
        fields = '__all__'

class ShopSerialiser(serializers.ModelSerializer):
    category = CategorySerialiser(read_only=True)
    class Meta:
        model = Shop
        fields = '__all__'
        #fields = ['pk']

class CategoryWithShopsSerialiser(serializers.ModelSerializer):
    shops = ShopSerialiser(many=True, read_only=True)
    class Meta:
        model = Categories
        fields = '__all__'

