from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import detail_route
from models import Post, Comment, LikeDislike
from serializers import PostsSerializer, CommentSerializer, FlagSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import APIException, ValidationError

from permissions import IsOwnerOrReadOnly


class PostsViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Post.objects.all()
    serializer_class = PostsSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly, IsAuthenticated,)

    def list(self, request):
        """
        Returns a list of Posts.
        """
        return super(PostsViewSet, self).list(request)

    def create(self, request):
        """
        Creates a new Posts.<br>
        """
        return super(PostsViewSet, self).create(request)

    def destroy(self, request, pk=None):
        """
        Deletes a Posts.
        """
        return super(PostsViewSet, self).destroy(request, pk=pk)

    def retrieve(self, request, pk=None):
        """
        Returns a Posts with id={id}
        """
        return super(PostsViewSet, self).retrieve(request, pk=pk)

    def update(self, request, pk=None, *args, **kwargs):
        """
        Updates an existing Posts.<br>
        """
        # self.object is used by the serializer for validation
        self.object = self.get_object()
        return super(PostsViewSet, self).update(request, pk=pk, *args, **kwargs)

    def partial_update(self, request, pk=None, *args, **kwargs):
        """
        Partially updates an existing Posts.<br>
        """
        # self.object is used by the serializer for validation
        self.object = self.get_object()
        return super(PostsViewSet, self).partial_update(request, pk=pk, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    # @detail_route(methods=['get', 'put'])
    # def vote(self, request, pk=None):
    #     serializer = FlagSerializer(data=request.data)
    #     if serializer.is_valid():
    #         if request.method == 'PUT':
    #             obj= LikeDislike.objects.filter(owner=request.user, voted_post=self.get_object().pk)
    #             if obj.exists():
    #                 if obj.vote == 1:
    #                     pass
    #             else:
    #                 LikeDislike.objects.create(owner=request.user, voted_post=self.get_object().pk, vote=1 if serializer.data['state'] else -1)
    #         obj = LikeDislike.objects.get(voted_post=self.get_object().pk)
    #         return Response({'likes': obj.likes, "dislikes": obj.dislikes, "sum_rating": obj.sum_rating})
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly, IsAuthenticated,)

    def list(self, request):
        """
        Returns a list of Comment.
        """
        return super(CommentViewSet, self).list(request)

    def create(self, request):
        """
        Creates a new Comment.<br>
        """
        return super(CommentViewSet, self).create(request)

    def destroy(self, request, pk=None):
        """
        Deletes a Comment.
        """
        return super(CommentViewSet, self).destroy(request, pk=pk)

    def retrieve(self, request, pk=None):
        """
        Returns a Posts with id={id}
        """
        return super(CommentViewSet, self).retrieve(request, pk=pk)

    def update(self, request, pk=None, *args, **kwargs):
        """
        Updates an existing Comment.<br>
        """
        # self.object is used by the serializer for validation
        self.object = self.get_object()
        return super(CommentViewSet, self).update(request, pk=pk, *args, **kwargs)

    def partial_update(self, request, pk=None, *args, **kwargs):
        """
        Partially updates an existing Comment.<br>
        """
        # self.object is used by the serializer for validation
        self.object = self.get_object()
        return super(CommentViewSet, self).partial_update(request, pk=pk, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
