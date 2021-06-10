from django.contrib import admin

from manuscripts.models import Manuscript


class ManuscriptAdmin(admin.ModelAdmin):
    model = Manuscript
    list_display = ('id', 'title', 'author', 'category', 'timestamp',
                    'is_deleted')
    list_filter = ('id', 'title', 'author', 'category', 'timestamp',
                   'is_deleted')


admin.site.register(Manuscript, ManuscriptAdmin)
