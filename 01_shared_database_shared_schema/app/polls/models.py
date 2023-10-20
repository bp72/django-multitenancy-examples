from django.db import models


class Tenant(models.Model):
    name = models.CharField(max_length=200)
    host = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return str(self.name)


class BaseModel(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Question(BaseModel):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self) -> str:
        return str(self.question_text)


class Choice(BaseModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return str(self.choice_text)
