from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('data published')
    body = models.TextField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    # null=True writer가 비어있어도 괜찮다 - 원래 writer라는 항목이 없는데 새로 추가를 하는 상황을 보자,
    # 비어있어도 괜찮아야지 아무런 문제가 없이 writer라는 항목이 생성된다 / False면 migrate 자체가 안됨

    def __str__(self):
        return self.title

class Comment(models.Model):
    body = models.TextField(max_length = 500)
    pub_date = models.DateTimeField('data published')
    
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    # null=True 필요없다 어짜피 처음 추가하는 거니까
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)
    # 어느 포스트에 해당하는지 - 포스트 정보도 받아와야한다
