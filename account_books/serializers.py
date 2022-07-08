from rest_framework import serializers
from users.models import User

from account_books.models import AccountBook, AccountCategory


class AcoountCategorySerializer(serializers.ModelSerializer):

    '''카테고리 Serializer

    Writer: 이동연
    Date: 2022-07-05

    카테고리 조회 Serializer 입니다.
    '''

    class Meta:
        model = AccountCategory
        fields = ['id', 'user', 'category_name', 'created_at', 'modified_at']

        ordering = ['category_name']


class AcoountCategoryPostializer(serializers.ModelSerializer):

    '''카테고리 Serializer

    Writer: 이동연
    Date: 2022-07-05

    카테고리 생성 Serializer 입니다.
    '''

    def create(self, validated_data):
        user_id = validated_data.get('user').id
        user = User.objects.get(id=user_id)
        category_name = validated_data.get('category_name')
        return AccountCategory.objects.create(user=user, category_name=category_name)

    class Meta:
        model = AccountCategory
        fields = ['category_name', 'user']


class AcoountCategoryPatchSerializer(serializers.ModelSerializer):

    '''카테고리 Serializer

    Writer: 이동연
    Date: 2022-07-05

    카테고리 수정 Serializer 입니다.
    '''

    def update(self, instance, validated_data):
        instance.category_name = validated_data.get('category_name')
        instance.save()
        return instance

    class Meta:
        model = AccountCategory
        fields = ['category_name']
        ordering = ['category_name']


# 리스트
class AccountBookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountBook
        fields = ['book_name', 'budget', 'delete_flag']


# 생성, 수정
class AccountBookCreatePatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountBook
        fields = ['user', 'book_name', 'budget']
