from django.db import models


class Tenant(models.Model):
    name = models.CharField(max_length=200)


class BaseModel(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Question(BaseModel):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Choice(BaseModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
