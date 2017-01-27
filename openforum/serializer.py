from rest_framework import serializers
from openforum.models import Question, User, Answer, Comment, Configuration

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('user_id', 'user_first_name', 'user_last_name',
                  'user_email_address', 'user_password')
    
class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ('question_id', 'question_author', 'question_summary', 'question_text',
                  'question_date', 'vote_up_count', 'vote_down_count', 'answer_count')
        
class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Answer
        fields = ('answer_id', 'question_id_fk', 'answer_author', 'answer_text',
                  'answer_date', 'vote_up_count', 'vote_down_count')
        
class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ('comment_id', 'question_id_fk', 'answer_id_fk', 'comment_author',
                  'comment_text', 'comment_date')
        
class ConfigurationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Configuration
        fields = ('configuration_type', 'down_vote', 'up_vote')
    