from django.db import models

# Create your models here.
MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

class Finch(models.Model):
    scientific_name = models.CharField(max_length=100)
    bird_family = models.CharField(max_length=100)
    food = models.CharField(max_length=100)
    key_information = models.TextField(max_length=250)
    weight = models.IntegerField()
    img = models.TextField(max_length=250)
    
    def __str__(self):
        return self.scientific_name
    
    
class Feeding(models.Model):
    date = models.DateField('feeding date')
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
        default=MEALS[0][0]
    )
    # Cat Foreign Key Below
    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"

    class Meta:
        ordering = ['-date']