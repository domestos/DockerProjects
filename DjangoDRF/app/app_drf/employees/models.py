from django.db import models

# Create your models here.
class Position(models.Model):
    position = models.CharField('Position', max_length=80)

    class Meta:
        ordering = ["position"]

    def __str__(self):
        return self.position


    # CASCADE: когда удаленный объект ссылки удаляется, удалите также и объекты, имеющие ссылки на него (например, при удалении сообщения в блоге, возможно, также захочется удалить комментарии). SQL-эквивалент: CASCADE.
    # PROTECT: Запретить удаление ссылочного объекта. Чтобы удалить его, вам придется удалить все объекты, ссылающиеся на него вручную. SQL-эквивалент: RESTRICT.
    # SET_NULL: Установите ссылку на NULL (требуется, чтобы поле было нулевым). Например, когда вы удаляете пользователя, вы можете оставить комментарии, которые он разместил в сообщениях в блоге, но скажите, что он был опубликован анонимным (или удаленным) пользователем. SQL-эквивалент: SET NULL.
    # SET_DEFAULT: установите значение по умолчанию. SQL-эквивалент: SET DEFAULT.
    # SET(...): задайте заданное значение. Этот не является частью стандарта SQL и полностью обрабатывается Django.
    # DO_NOTHING: Вероятно, очень плохая идея, так как это создаст проблемы целостности в вашей базе данных (ссылаясь на объект, который на самом деле не существует). SQL-эквивалент: NO ACTION.


class Employee(models.Model):
    name = models.CharField('Name', max_length=80, unique=True)
    position_id = models.OneToOneField(Position, default='', blank=True, on_delete=models.SET_DEFAULT, related_name='position_id')
    first_work_day =  models.DateTimeField(blank=False)
    last_work_dat =  models.DateTimeField(blank=True)

    class Meta:
        ordering = ["first_work_day"]
