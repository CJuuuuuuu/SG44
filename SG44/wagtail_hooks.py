from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

from .models import ConferencePage


class ConferencePageAdmin(ModelAdmin):
    model = ConferencePage
    menu_label = '研討會管理'
    menu_icon = 'doc-full-inverse'
    list_display = ('title', 'conference_date', 'location')
    search_fields = ('title', 'theme_zh', 'theme_en')

# modeladmin_register(ConferencePageAdmin)  # 如果需要在側邊欄顯示
