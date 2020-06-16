from tortoise import fields
from tortoise.models import Model


class qa(Model):
    id = fields.IntField(pk=True)
    question = fields.FloatField(source_field='question') 
    answer = fields.FloatField(source_field='answer')
    created_at = fields.TextField(source_field='created_at')

    class Meta:
        table = "qa"
        table_description = "This table contains question and answer value"

    def __str__(self):
        return "question is square of {} and answer is {}.".format(self.question, self.answer)