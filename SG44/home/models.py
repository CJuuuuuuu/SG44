from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock


class HomePage(Page):
    """首頁"""
    
    # === 橫幅區 ===
    banner_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="橫幅圖片"
    )
    
    banner_title = models.CharField(
        max_length=255,
        default="SG44 研討會",
        verbose_name="橫幅標題"
    )
    
    banner_subtitle = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="橫幅副標題"
    )
    
    # === 研討會資訊 ===
    conference_date = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="研討會日期"
    )
    
    conference_location = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="研討會地點"
    )
    
    registration_deadline = models.DateField(
        null=True,
        blank=True,
        verbose_name="報名截止日期"
    )
    
    registration_link = models.URLField(
        blank=True,
        verbose_name="報名連結"
    )
    
    # === 主要內容 ===
    intro = RichTextField(
        blank=True,
        verbose_name="簡介"
    )
    
    body = StreamField([
        ('heading', blocks.CharBlock(
            form_classname="title",
            label="標題",
            icon="title"
        )),
        ('paragraph', blocks.RichTextBlock(
            label="段落",
            icon="pilcrow"
        )),
        ('image', ImageChooserBlock(
            label="圖片",
            icon="image"
        )),
        ('quote', blocks.BlockQuoteBlock(
            label="引言",
            icon="openquote"
        )),
        ('embed', blocks.URLBlock(
            label="嵌入連結（YouTube等）",
            icon="media"
        )),
    ], blank=True, use_json_field=True, verbose_name="內容區塊")
    
    # === 特色區塊 ===
    feature_1_icon = models.CharField(
        max_length=50,
        blank=True,
        verbose_name="特色1圖示",
        help_text="例如：📅"
    )
    feature_1_title = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="特色1標題"
    )
    feature_1_text = models.TextField(
        blank=True,
        verbose_name="特色1說明"
    )
    
    feature_2_icon = models.CharField(
        max_length=50,
        blank=True,
        verbose_name="特色2圖示"
    )
    feature_2_title = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="特色2標題"
    )
    feature_2_text = models.TextField(
        blank=True,
        verbose_name="特色2說明"
    )
    
    feature_3_icon = models.CharField(
        max_length=50,
        blank=True,
        verbose_name="特色3圖示"
    )
    feature_3_title = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="特色3標題"
    )
    feature_3_text = models.TextField(
        blank=True,
        verbose_name="特色3說明"
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('banner_image'),  # 改這裡！
            FieldPanel('banner_title'),
            FieldPanel('banner_subtitle'),
        ], heading="橫幅設定"),
        
        MultiFieldPanel([
            FieldPanel('conference_date'),
            FieldPanel('conference_location'),
            FieldPanel('registration_deadline'),
            FieldPanel('registration_link'),
        ], heading="研討會資訊"),
        
        FieldPanel('intro'),
        FieldPanel('body'),
        
        MultiFieldPanel([
            FieldPanel('feature_1_icon'),
            FieldPanel('feature_1_title'),
            FieldPanel('feature_1_text'),
        ], heading="特色1"),
        
        MultiFieldPanel([
            FieldPanel('feature_2_icon'),
            FieldPanel('feature_2_title'),
            FieldPanel('feature_2_text'),
        ], heading="特色2"),
        
        MultiFieldPanel([
            FieldPanel('feature_3_icon'),
            FieldPanel('feature_3_title'),
            FieldPanel('feature_3_text'),
        ], heading="特色3"),
    ]

    class Meta:
        verbose_name = "首頁"
