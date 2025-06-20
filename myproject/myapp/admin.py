from django.contrib import admin
from .models import ItineraryItem, ItinerarySection, BoatingPackage, AttractionBulletPoint, MainAttraction, FoodStyle, FoodTimings, FoodBulletPoint, WhenDoesitRun, Duration, StartAndEndPoints, Inclusion, Exclusion, GoodToKnow

# Register your models here.



class MainAttractionInline(admin.TabularInline):
    model = MainAttraction
    extra = 1

class AttractionBulletInline(admin.TabularInline):
    model = AttractionBulletPoint
    extra = 1


class ItineraryItemInline(admin.TabularInline):
    model = ItineraryItem
    extra = 1

class ItenerarySectionInline(admin.TabularInline):
    model = ItinerarySection
    extra = 1


class FoodStyleInline(admin.TabularInline):
    model = FoodStyle
    extra = 1

class FoodTimingInline(admin.TabularInline):
    model = FoodTimings
    extra = 1

class FoodBulletInline(admin.TabularInline):
    model = FoodBulletPoint
    extra = 1

class WhenDoesItRunInline(admin.TabularInline):
    model = WhenDoesitRun
    extra = 1

class DurationInline(admin.TabularInline):
    model = Duration
    extra = 1

class StartAndEndingPointsInline(admin.TabularInline):
    model = StartAndEndPoints
    extra = 1

class InclusionInline(admin.TabularInline):
    model = Inclusion
    extra = 1

class ExclusionInline(admin.TabularInline):
    model = Exclusion
    extra = 1

class GoodToKnowInline(admin.TabularInline):
    model = GoodToKnow
    extra = 1

class AttractionAdmin(admin.ModelAdmin):
    inlines = [MainAttractionInline, AttractionBulletInline,  ItenerarySectionInline, ItineraryItemInline, FoodStyleInline, FoodTimingInline, FoodBulletInline, WhenDoesItRunInline, DurationInline, StartAndEndingPointsInline, InclusionInline, ExclusionInline, GoodToKnowInline]

admin.site.register(BoatingPackage, AttractionAdmin)


