from django.db import models

class Card(models.Model):
    card_image = models.CharField(max_length=8, unique=True, editable=False)

class Present(models.Model):
    voice_giver = models.ForeignKey(
        'user.User',
        on_delete=models.CASCADE,
        related_name='given_presents'  # 역참조 이름 변경
    )
    voice_taker = models.ForeignKey(
        'user.User',
        on_delete=models.CASCADE,
        related_name='taken_presents'  # 역참조 이름 변경
    )
    avatar = models.ForeignKey('voice.Avatar', on_delete=models.CASCADE) #줄 목소리
    card = models.ForeignKey('present.Card', on_delete=models.CASCADE)
    present_message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    