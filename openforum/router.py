from rest_framework import routers
from openforum.viewset import UserViewSet, QuestionViewSet, AnswerViewSet
from openforum.viewset import CommentViewSet, ConfigurationViewSet

# Routers provide an easy way of automatically determining the URL conf.
class router:
    
    def set_router(self):
        
        router = routers.DefaultRouter()
        router.register(r'users', UserViewSet)
        router.register(r'questions', QuestionViewSet)
        router.register(r'answers', AnswerViewSet)
        router.register(r'comments', CommentViewSet)
        router.register(r'configurations', ConfigurationViewSet)
        
        return router