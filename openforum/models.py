"""
Django models for openforum
"""

from django.db import models
from bson.json_util import default

# User model define user fields
class User(models.Model):
    def __str__(self):
        return self.user_first_name
    #user_id = models.CharField(max_length=8)
    user_id = models.AutoField(primary_key=True)
    user_first_name = models.CharField('First name', max_length=32)
    user_last_name = models.CharField('Last name', max_length=32)
    user_email_address = models.CharField('Email address', max_length=128)
    user_password = models.CharField('User password', max_length=64)

# Question model define question fields
class Question(models.Model):
    def __str__(self):
        return self.question_summary
    #question_id = models.CharField(max_length=8)
    question_id = models.AutoField(primary_key=True)
    question_author = models.ForeignKey(User, on_delete=models.CASCADE)
    question_summary = models.CharField('Question Summary', max_length=64)
    question_text = models.CharField('Question Text', max_length=200)
    question_date = models.DateTimeField('Date published')
    vote_up_count = models.IntegerField(default=0)
    vote_down_count = models.IntegerField(default=0)
    answer_count = models.IntegerField(default=0)

# Answer model define answer fields
class Answer(models.Model):
    def __str__(self):
        return self.answer_text
    #answer_id = models.CharField(max_length=8)
    answer_id = models.AutoField(primary_key=True)
    question_id_fk = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_author = models.ForeignKey(User, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=200)
    answer_date = models.DateTimeField('Date published')
    vote_up_count = models.IntegerField(default=0)
    vote_down_count = models.IntegerField(default=0)

# Comment model define comment fields
class Comment(models.Model):
    def __str__(self):
        return self.comment_text
    #comment_id = models.CharField(max_length=8)
    comment_id = models.AutoField(primary_key=True)
    question_id_fk = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_id_fk = models.ForeignKey(Answer, on_delete=models.CASCADE)
    comment_author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=200)
    comment_date = models.DateTimeField('Date published')

# Configuration model define configuration fields
class Configuration(models.Model):
    def __str__(self):
        return self.configuration_type
    configuration_type = models.CharField(max_length=8)
    down_vote = models.IntegerField(default=1)
    up_vote = models.IntegerField(default=1)