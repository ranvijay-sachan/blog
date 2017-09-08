from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated

from models import Post, Comment
from serializers import PostsSerializer, CommentSerializer

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
