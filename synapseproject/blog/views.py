from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated

from models import Post
from serializers import PostsSerializer

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

