from rest_framework import serializers
from friendship.models import Friend, Block, Follow, FriendshipRequest


class FriendshipRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendshipRequest
        fields = ('id','from_user', 'to_user', 'message', 'created', 'rejected', 'viewed')


class CreateFriendshipRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendshipRequest
        fields = ('to_user', 'message')


class UpdateFriendshipRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendshipRequest
        fields = ('rejected',)


class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = ('id', 'to_user', 'from_user', 'created')



