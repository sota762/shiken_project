from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator


class ScoreCategory(models.Model):

    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    CATEGORY=(('language','国語'),
              ('math','数学'),
              ('english','英語'),
              ('science','科学'),
              ('history','歴史'))
    
    score=models.IntegerField(
        verbose_name='点数',
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
                ]  
        )
    posted_at=models.DateTimeField(
        verbose_name='登録日時',
        auto_now_add=True
        )
    category=models.CharField(
        verbose_name='カテゴリ',
        max_length=50,
        choices=CATEGORY
        )
    
    def __str__(self):

        return f"{self.user.username} - {self.score}"


    

