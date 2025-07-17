from django.contrib import admin

#Yaptığımız article sınıfının importu
from .models import Article, Comment

# Register your models here.
admin.site.register(Comment)
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    #Article kısmında hangi özelliklerin gösterilmesi
    list_display = ["title", "author", "created_date"]
    
    #Link verme 
    list_display_links = ["title", "created_date"]
    
    #Arama kısmı verme
    search_fields = ["title"]
    
    #Oluşturulma tarihine göre filreleme
    list_filter = ["created_date"]

    #Djangonun kendisinin oluşturmamızı istediği meta class'ı
    class Meta:
        model = Article

