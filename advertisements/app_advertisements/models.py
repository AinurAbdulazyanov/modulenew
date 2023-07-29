from django.db import models


class Advertisement(models.Model):
    # название товара
    # CharField - короткое текстовое поле
    # 'заголовок' - verbose_name - человекочитаемое название
    title = models.CharField('заголовок', max_length=128)
    # Описание товара
    # Длинное текстовое поле 
    description = models.TextField('описание')
    # Цена
    # Числовое поле с фиксированной точкой
    price = models.DecimalField('цена', max_digits=10, decimal_places=2)
    # Уместен ли торг?
    # Булевое поле (логическое)
    auction = models.BooleanField('Торг', help_text='Отметьте, если хотите торговаться')
    # Дата публикации
    created_at = models.DateTimeField(auto_now_add=True)
    # Дата изменения/обновления + что изменилось
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Advertisement(id={self.id}, title={self.title}, price={self.price})"



    class Meta:
        db_table = 'advertisements'

    # Продавец(имя, контакты для связи, отзывы)
    # Фото объявление
    # Рейтинг
    # В продаже/не в продаже - актуальность

    


