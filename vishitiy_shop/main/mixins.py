import random # Импортируем модуль random для генерации случайных чисел

from pytils.translit import slugify # Импортируем функцию slugify для преобразования текста в slug


class SaveSlugMixin:
    # Миксин для автоматического сохранения slug при сохранении объекта модели.
    def save(self, slug_field="slug", slugify_value=None, *args, **kwargs):
        # Переопределенный метод save для сохранения объекта модели с генерацией и сохранением уникального slug.
        if slug_field and slugify_value:
            slug = getattr(self, slug_field)
            if not slug:
                new_slug = slugify(slugify_value)
                setattr(self, slug_field, new_slug)
                while self.__class__.objects.filter(
                    **{slug_field + "__iexact": new_slug}
                ).exists():
                    new_slug += str(
                        random.randint(0, (self.__class__.objects.count() + 1) * 100)
                    )
                    setattr(self, slug_field, new_slug)
        return super().save(*args, **kwargs)
