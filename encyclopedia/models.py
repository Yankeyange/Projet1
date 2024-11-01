from django.db import models

# créons nos modèles ici
# pour chaque language est assigner un choix
class Topic(models.Model):
  name = models.CharField(max_length=200)
  first_name = models.CharField(max_length=200)
  description  = models.TextField()

  def __str_(self):
    return self.name
  
class Entry(models.Model):
  topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
  description = models.TextField()

