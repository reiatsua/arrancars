from django.db import models


class TeamInfo(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название команды"
    )
    description = models.TextField(
        verbose_name="Описание команды"
    )
    discipline = models.CharField(
        max_length=100,
        verbose_name="Дисциплина"
    )
    goal = models.CharField(
        max_length=200,
        verbose_name="Цель команды"
    )
    logo = models.ImageField(
        upload_to="team/",
        blank=True,
        verbose_name="Логотип команды"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Информация о команде"
        verbose_name_plural = "Информация о команде"


class TeamMember(models.Model):
    nickname = models.CharField("Никнейм", max_length=50)
    role = models.CharField("Роль", max_length=50)
    description = models.TextField("Описание", blank=True)
    photo = models.ImageField(
        "Фото игрока",
        upload_to="players/",
        blank=True
    )

    def __str__(self):
        return self.nickname


class Match(models.Model):
    opponent = models.CharField("Соперник", max_length=100)
    result = models.CharField("Результат", max_length=50)
    date = models.DateField("Дата матча")

    def __str__(self):
        return f"{self.opponent} ({self.result})"