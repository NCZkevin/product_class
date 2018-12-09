from rest_framework import serializers
from .models import Goods, GoodsCategory
from rest_framework.response import Response

# class GoodsClassSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = GoodsClass
#         fields = "__all__"

# class GoodsKeywordSerializer(serializers.ModelSerializer):
#     classes = GoodsClassSerializer()
#     class Meta:
#         model = GoodsKeyword
#         fields = "__all__"
    
#     def create(self, validated_data):
#         classes_data = validated_data.pop('classes')
#         keyword = GoodsKeyword.objects.create(**validated_data)
#         print(classes_data)
#         GoodsClass.objects.create(name=keyword, **class_data)
#         # GoodsClass.objects.create(name=classes_data)
#         # for class_data in classes_data:
#         #     GoodsClass.objects.create(name=keyword, **class_data)
#         return keyword

class CategorySerializer3(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class CategorySerializer2(serializers.ModelSerializer):
    sub_cat = CategorySerializer3(many=True)
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    sub_cat = CategorySerializer2(many=True)
    class Meta:
        model = GoodsCategory
        fields = "__all__"

class GoodsSerializer(serializers.ModelSerializer):
    classes =  CategorySerializer3(many=True, read_only=False, partial=True)

    class Meta:
        model = Goods
        fields = "__all__"

    def update(self, instance, validated_data):
        # import traceback;
        # traceback.print_stack()

        # classes = validated_data.get('classes', instance.classes)
        try:
            classes = validated_data.pop('classes')
        except:
            classes = None
        is_click = validated_data.get('is_click', instance.is_click)
        # ins_cla = instance.classes
        if classes is not None:
            instance = super(GoodsSerializer, self).update(instance, validated_data)
            # for classe in classes:
            cla = GoodsCategory.objects.filter(name__iexact=classes[0]['name'])
            if cla.exists():
                tag = cla.first()
            # print(tag)
            taglist = []
            taglist.append(tag)
            # else:
            #     tag = Tag.objects.create(**tag_data)
            # instance.classes = tag
            # cla1 = GoodsCategory.objects.filter(name__iexact=instance)
            # tag1 = cla1.first()
            # instance.classes.remove(tag1)
            # print(instance)
            instance.classes.set(taglist)
            instance.is_class = 1
            instance.is_click = 1
            instance.save()
            return instance
        else:
            instance.is_click = 1
            instance.save()
            return instance


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = ["company"]