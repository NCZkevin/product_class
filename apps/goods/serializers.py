from rest_framework import serializers
from .models import Goods, GoodsClass, GoodsKeyword

class GoodsClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsClass
        fields = "__all__"

class GoodsKeywordSerializer(serializers.ModelSerializer):
    classes = GoodsClassSerializer()
    class Meta:
        model = GoodsKeyword
        fields = "__all__"
    
    def create(self, validated_data):
        classes_data = validated_data.pop('classes')
        keyword = GoodsKeyword.objects.create(**validated_data)
        print(classes_data)
        GoodsClass.objects.create(name=keyword, **class_data)
        # GoodsClass.objects.create(name=classes_data)
        # for class_data in classes_data:
        #     GoodsClass.objects.create(name=keyword, **class_data)
        return keyword

class GoodsSerializer(serializers.ModelSerializer):
    classes = GoodsClassSerializer(many=True)
    class Meta:
        model = Goods
        fields = "__all__"