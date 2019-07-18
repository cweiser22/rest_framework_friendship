from rest_framework import views, mixins, generics
from friendship.models import Friend, FriendshipRequest
from . import serializers

# Create your views here.
class FriendsListView(generics.ListAPIView):
    serializer_class = serializers.FriendSerializer
    
    def get_queryset(self):
        user = self.request.user
        return Friend.objects.friends(user)


#handles actions on all friend requests
class FriendRequestListView(generics.ListCreateAPIView):

    #might just use one serializer to make this simpler
    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.FriendshipRequestSerializer
        else:
            return serializers.CreateFriendshipRequestSerializer


#handles actions on single friend requests
class FriendRequestDetailView(generics.RetrieveUpdateAPIView):

    

    #might just use one serializer to make this simpler
    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.UpdateFriendshipRequestSerializer
        else:
            return serializers.FriendshipRequestSerializer


