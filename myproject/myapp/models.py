from django.db import models

# Create your models here.


class BoatingPackage(models.Model):
    slug = models.SlugField(unique=True)
    package_name = models.CharField(max_length=255)
    thumbnail = models.ImageField(upload_to='packages/')
    short_overview = models.CharField(max_length=250)
    places_covering = models.TextField()

    def __str__(self):
        return self.package_name
    
class MainAttraction(models.Model):
    section = models.ForeignKey(BoatingPackage, on_delete=models.CASCADE, related_name='main_attraction')
    main_attraction = models.TextField()

    def __str__(self):
        return self.main_attraction
    
class AttractionBulletPoint(models.Model):
    section = models.ForeignKey(BoatingPackage, on_delete=models.CASCADE, related_name='attraction_bullet_points')
    text = models.CharField(max_length=300)

    def __str__(self):
        return self.text
    
class ItinerarySection(models.Model):
    section = models.ForeignKey(BoatingPackage, on_delete=models.CASCADE, default=1, related_name='itinerary_desc')
    short_description = models.TextField()

    def __str__(self):
        return self.short_description
    
class ItineraryItem(models.Model):
    section = models.ForeignKey(BoatingPackage, on_delete=models.CASCADE, related_name='itinerary_items')
    time = models.CharField(max_length=20)
    plan = models.TextField()

    def __str__(self):
        return f"{self.time} - {self.plan[:30]}..."
    
class FoodStyle(models.Model):
    section = models.ForeignKey(BoatingPackage, on_delete=models.CASCADE, related_name='food_styles')
    food_style = models.CharField(max_length=200)

    def __str__(self):
        return self.food_style
    
class FoodTimings(models.Model):
    section = models.ForeignKey(BoatingPackage, on_delete=models.CASCADE, related_name='foodtiming')
    time = models.CharField(max_length=20)
    food = models.TextField()

    def __str__(self):
        return f"{self.time} - {self.food[:30]}..."
    
class FoodBulletPoint(models.Model):
    section = models.ForeignKey(BoatingPackage, on_delete=models.CASCADE, related_name='food_bullet_points')
    text = models.CharField(max_length=300)

    def __str__(self):
        return self.text
    
class WhenDoesitRun(models.Model):
    section = models.ForeignKey(BoatingPackage, on_delete=models.CASCADE, related_name='run')
    when_does_it_run = models.CharField(max_length=300)

    def __str__(self):
        return self.when_does_it_run
    
class Duration(models.Model):
    section = models.ForeignKey(BoatingPackage, on_delete=models.CASCADE, related_name='durations')
    duration = models.CharField(max_length=300)
    start_time = models.CharField(max_length=300, default='10:00 AM')
    end_time = models.CharField(max_length=300, default='5:00 PM')

    def __str__(self):
        return self.duration
    
class StartAndEndPoints(models.Model):
    section = models.ForeignKey(BoatingPackage, on_delete=models.CASCADE ,related_name='start_end_points')
    starting_point = models.TextField()
    ending_point = models.TextField()

    def __str__(self):
        return self.starting_point
    
    
class Inclusion(models.Model):
    section = models.ForeignKey(BoatingPackage, on_delete=models.CASCADE, related_name='inclusion')
    bullet_points = models.CharField(max_length=300)

    def __str__(self):
        return self.bullet_points
    
class Exclusion(models.Model):
    section = models.ForeignKey(BoatingPackage, on_delete=models.CASCADE, related_name='exclusions')
    bullet_points = models.CharField(max_length=300)

    def __str__(self):
        return self.bullet_points
    
class GoodToKnow(models.Model):
    section = models.ForeignKey(BoatingPackage, on_delete=models.CASCADE, related_name='goodtoknow')
    good_to_know = models.TextField()

    def __str__(self):
        return self.good_to_know