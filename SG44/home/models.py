from django.db import models
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.admin.panels import FieldPanel
from wagtail.admin.panels import FieldPanel as Panel
from wagtail.admin.panels import InlinePanel, MultiFieldPanel
from wagtail.api import APIField
from wagtail.fields import RichTextField
from wagtail.models import Page
from wagtail.snippets.models import register_snippet


class HomePage(Page):
    """研討會首頁"""
    
    # 會議基本資訊
    title_zh = models.CharField("中文標題", max_length=255, default="第44屆測量及空間資訊研討會")
    subtitle_en = models.CharField("英文副標題", max_length=255, default="SG44 Conference on Surveying and Geomatics")
    theme_zh = models.CharField("中文主題", max_length=255, default="智測國土，韌期未來")
    theme_en = models.CharField("英文主題", max_length=255, default="Smart Surveying of National Land, Resilient Future")
    
    conference_date = models.CharField("會議日期", max_length=100, default="2024年 8月 29日 (四) - 30日 (五)")
    location = models.CharField("會議地點", max_length=255, default="國立政治大學 法學院")
    organizer = models.CharField("主辦單位", max_length=255, default="國立政治大學 地政學系")
    co_organizer = models.CharField("承辦單位", max_length=255, default="國立政治大學 地政學系")
    
    # 聯絡資訊
    contact_email = models.EmailField("聯絡信箱", default="sg44@example.com")
    contact_phone = models.CharField("聯絡電話", max_length=50, default="02-29393091")
    
    # Hero 區塊
    hero_description = RichTextField("首頁描述", blank=True)
    
    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('title_zh'),
            FieldPanel('subtitle_en'),
            FieldPanel('theme_zh'),
            FieldPanel('theme_en'),
        ], heading="會議標題"),
        
        MultiFieldPanel([
            FieldPanel('conference_date'),
            FieldPanel('location'),
            FieldPanel('organizer'),
            FieldPanel('co_organizer'),
        ], heading="會議資訊"),
        
        MultiFieldPanel([
            FieldPanel('contact_email'),
            FieldPanel('contact_phone'),
        ], heading="聯絡資訊"),
        
        FieldPanel('hero_description'),
        
        InlinePanel('news_items', label="最新消息"),
        InlinePanel('topics', label="徵稿主題"),
        InlinePanel('timeline_events', label="重要時程"),
    ]
    
    # 限制只能有一個首頁
    max_count = 1
    
    class Meta:
        verbose_name = "研討會首頁"


class NewsItem(ClusterableModel):
    """最新消息"""
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='news_items')
    date = models.DateField("日期")
    category = models.CharField("分類", max_length=50, choices=[
        ('重要公告', '重要公告'),
        ('活動消息', '活動消息'),
        ('系統更新', '系統更新'),
    ])
    title = models.CharField("標題", max_length=255)
    link = models.URLField("連結", blank=True)
    
    panels = [
        FieldPanel('date'),
        FieldPanel('category'),
        FieldPanel('title'),
        FieldPanel('link'),
    ]
    
    class Meta:
        ordering = ['-date']
        verbose_name = "最新消息"
        verbose_name_plural = "最新消息"


class Topic(ClusterableModel):
    """徵稿主題"""
    ICON_CHOICES = [
        ('Map', '地圖'),
        ('Zap', '閃電'),
        ('Shield', '盾牌'),
        ('Globe', '地球'),
        ('Cpu', 'CPU'),
        ('Database', '資料庫'),
    ]
    
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='topics')
    title = models.CharField("主題標題", max_length=100)
    description = models.TextField("主題描述")
    icon_name = models.CharField("圖示", max_length=50, choices=ICON_CHOICES, default='Map')
    order = models.IntegerField("排序", default=0)
    
    panels = [
        FieldPanel('title'),
        FieldPanel('description'),
        FieldPanel('icon_name'),
        FieldPanel('order'),
    ]
    
    class Meta:
        ordering = ['order']
        verbose_name = "徵稿主題"
        verbose_name_plural = "徵稿主題"


class TimelineEvent(ClusterableModel):
    """重要時程"""
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='timeline_events')
    date = models.DateField("日期")
    title = models.CharField("事件標題", max_length=100)
    is_past = models.BooleanField("已過期", default=False)
    order = models.IntegerField("排序", default=0)
    
    panels = [
        FieldPanel('date'),
        FieldPanel('title'),
        FieldPanel('is_past'),
        FieldPanel('order'),
    ]
    
    class Meta:
        ordering = ['order']
        verbose_name = "時程事件"
        verbose_name_plural = "時程事件"
