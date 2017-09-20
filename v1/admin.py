'''
Django admin customisation
'''

from django.contrib import admin
from v1.models import Board, Card, Label, List, User

# class ProductByLanguageAdmin(SortableAdmin):
#   exclude = ['url',
#   ]
#   model = ProductByLanguage
#   list_filter = ('language',)

# class FeatureAdmin(SortableAdmin):

#   exclude = [ 'url',
#   ]
#   list_filter = ('language',)

# class TopFeatureAdmin(SortableAdmin):

#   def has_add_permission(self, request):
#       return False if self.model.objects.count() >= 4 else True
class CardInline(admin.TabularInline):
    model = Card

class ListAdmin(admin.ModelAdmin):
    inlines = [
        CardInline,
    ]

admin.site.register(Board)
admin.site.register(Card)
admin.site.register(Label)
admin.site.register(List, ListAdmin)
admin.site.register(User)
