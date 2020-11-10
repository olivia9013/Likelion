from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    #author = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    #user = models.ForeignKey(User에서 User는 import 해야하고, 모델이름임)

    #위에서 user 이라고 적더라도, post.user로 됨
    #author이라고 하면 post.author
    body = models.TextField()
    created_at = models.DateTimeField()
    #Cascade 폭포, 최상위클래스가 지워지면 관련된것도 모두 지우겠다는 의미
    #on_delete=models.CASCADE UER가 지워졌을때 관련있는 post class도 다 지워버린다?
# Create your models here.
    liked_users = models.ManyToManyField(User, related_name='liked_posts')
    #좌측 변수는 실제 코딩할때 쓰고 DB에서는 무관...^^,,

    def __str__(self):
        if self.user: 
            return f'{self.user.get_username()}: {self.body}'
            #요 위에서 return을 하면 아래의 return은 실행하지 않는다.
            #그래서 else 필요 없이 하단에 그냥 바로 return 씀.
        return f'{self.body}'


    