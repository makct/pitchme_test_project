from django.db import models


class City(models.Model):
    country = models.CharField(max_length=200)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Event(models.Model):
    short_descr = models.CharField(max_length=100, default="Имя ивента")
    full_descr = models.TextField(default="Нужно заполнить описание")
    start_date = models.DateTimeField(verbose_name="Дата начала события", null=True)
    end_date = models.DateTimeField(verbose_name="Дата окончания события", null=True)
    location = models.CharField(max_length=100, default="Узнавайте у огранизатора")
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.city}: {self.short_descr}"


class EventTopic(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.event.short_descr}: {self.topic.name}"


class UserSearchHistory(models.Model):
    username = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    start_interval = models.DateTimeField(null=True)
    end_interval = models.DateTimeField(null=True)
    topic = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.username} - {self.city} - {self.topic} - {self.start_interval} - {self.end_interval}"

    def __repr__(self):
        return f"{self.username} - {self.city} - {self.topic} - {self.start_interval} - {self.end_interval}"