from django.db import models

from wagtail.core.models import Page
from wagtail.core import blocks
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.blocks import ImageChooserBlock


class HomePage(Page):

    # An introduction to our site
    body = RichTextField(blank=True)


    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]


class WebPage(Page):

    cover_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    subtitle = models.CharField(
        max_length = 255,
        null = True,
        blank = True,
    )
    body = StreamField([
        ('text', blocks.RichTextBlock(null=True, blank=True)),
        ('image', ImageChooserBlock(null=True, blank=True)),
        ],
        blank=True,
    )

    template="home/web_page.html"

    content_panels = Page.content_panels + [
        ImageChooserPanel('cover_image'),
        FieldPanel('subtitle'),
        StreamFieldPanel('body'),
    ]