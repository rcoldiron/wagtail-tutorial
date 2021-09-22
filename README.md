Wagtail Tutorial
================

This tutorial assumes some knowledge of Python, Django, and Git/GitHub (optional). If you have experience with none of these, consider following these tutorials beforehand and coming back to this one once you are ready:

* [The Python Tutorial](https://docs.python.org/3/tutorial/index.html)

* [Python virtual environments](https://docs.python.org/3/tutorial/venv.html)

* [Django Girls Tutorial](https://tutorial.djangogirls.org/en/)

* [Django 3.2 Tutorial](https://docs.djangoproject.com/en/3.2/intro/)

* [Git Handbook](https://guides.github.com/introduction/git-handbook/)


Key Technologies
----------------

These are the key technologies that we are using for this tutorial:

* Python 3.9

* Git and GitHub (if you want to track your code and its versions and/or publish your code)

* Wagtail 2.14 (Django 3.2 is included in the package)

* Visual Studio Code (or your favorite code editor)


Initial Setup
-------------

1. If you want to work with this repo, you can either download the files from GitHub, or fork the repo and clone it to your local machine. Otherwise, make a folder on your local machine to work in and open your command line tool to `cd` into the folder: `cd my-folder`

2. Install Python 3.9 if you do not have it on your computer; however, Wagtail 2.14 is compatible with Python 3.6 and up. Check your Python version with `python --version`.

> NOTE: If it throws an error or doesn't recognize it, you may need to download it. Go to [Python - Downloads](https://www.python.org/downloads/) and follow download instructions for your Operating System.

3. Now create a virtual environment: `python3 -m venv .venv` on Windows 10. The command you have to use may be different, depending on your operating system and version.

4. Activate the virtual environment: `.venv\Scripts\activate.ps1` (on Windows 10). If it worked, you should see the name of the virtual environment in the command line before the file path on the next line, similar to the following: `(.venv) C:Users/YourName/Your/File/Location:`

5. Install Wagtail. This will also install all of its dependencies. I use `pip` to install, but you may use a different Python package manager. This command is for `pip`: `pip install wagtail`

> NOTE: The current version at the time of the creation of this repo is Wagtail 2.14. You can select a version to download, like this `pip install wagtail==2.14`

6. Create the first project: `wagtail start myproject .` where `myproject` is the name of the website or project (this can be whatever you want) and the `.` tells it to create it in your current folder. This command generates the new project files from Wagtail. Please take a moment to look them over.

> NOTE: Docker files are automatically generated with the project. While we will not be using them, we are keeping them in the repo in case you want to look them over and learn more about what they do. Docker can be used for deployment. [READ MORE](https://docs.wagtail.io/en/v2.14/reference/project_template.html#dockerfile)

7. Navigate into the project: `cd myproject` and do the first migration with: `python manage.py migrate`. Next, create a login account for your project with the command `python manage.py createsuperuser` and follow the prompts. Check if it all worked by running `python manage.py runserver` and opening your browser to `http://127.0.0.1:8000/`.

**Before moving onto the code section, get familiar with the CMS interface. Log into your site at `http://127.0.0.1:8000/admin` and read the [Wagtail documentation for Editors](https://docs.wagtail.io/en/stable/editor_manual/index.html)].**


Customizing Your Site - Part I
------------------------------

Let's start by updating the Home Page model, which is found in `home` > `models.py`. The current Home Page model is sub-classed from the Wagtail Page model, but we can add more features and update the template.

1. First, we need to decide what we want to have on our Home Page and import any Wagtail components that we think we need. The current Home Page just has the title and no way to add content.

2. We want to add text to the page. To do this, we need to import **RichTextField**. At the top of the `models.py`, add the following import:

```
from wagtail.core.fields import RichTextField

```

3. Now we will add fields to the model.

```
class HomePage(Page):

    # An introduction to our site
    body = RichTextField(null=True, blank=True)

```

4. Next we need to add content panels to the editor side for the page that will also us to add content. At the top, add the following imports:

```
from wagtail.admin.edit_handlers import FieldPanel

```

5. Then add the content panels to the Home Page model, like this:

```
class HomePage(Page):

    # An introduction to our site
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]

```

6. Now we need to run `python manage.py makemigrations` and `python manage.py migrate` to see it take effect.

7. Run the server and log into the admin. Then go into the HomePage to edit it. You should see your new field!

8. The RichTextField looks like a standard text editor. Write some text, add some photos and links, then republish the page.

> WAIT! None of the content I added shows up on the frontend! Now what?

9. We need to modify the Home Page template to pull in our new field. Templates are found in the app folder under `templates`. Let's look at the `home_page.html` template. It uses the Django templating system and has default content added that we can now delete. Delete `{% comment %}` code, the CSS file link (we will want to replace that), and the line `{% include 'home/welcome_page.html' %}` because we are going to make our own Home Page content.

10. We can add a CSS link specific to this page between these two tags: `{% block extra_css %} {% endblock extra_css %}`; however, the page extends `base.html`, which is actually found in `myproject` > `static` > `css`. The global CSS link should be added to `base.html`. For simplicity, we are just going to pull in the Bootstrap CDN but feel free to make your CSS in the `myproject,css` file. Add it under the `{# Global stylesheets #}` comment tag and save it.

11. Now go back to `home_page.html`. We will put our content within the tags `{% block content %} {% endblock content %}`. Our code will be:

```
{% extends "base.html" %}
{% load static wagtailcore_tags %}

{% block body_class %}template-homepage{% endblock %}

{% block extra_css %}{% endblock extra_css %}

{% block content %}
<div class="container">
    <div class="row">
        <div class="col-12 text-center border-bottom border-success">
            <h1>{{page.title}}</h1>
        </div>
        <div class="col my-4">
            {{page.body|richtext}}
        </div>
    </div>
</div>
{% endblock content %}

```

I've added some basic Bootstrap classes to style the page a little. We need to load `static` to pull in CSS and JS, and we need `wagtailcore_tags` for the special filtering we did for the `body` field. To include fields in your templates, you put them between curly braces and use dot notation: `{{page.body}}`. RichTextFields need a `richtext` filter to display correctly.

12. Save these changes, then `python manage.py runserver` and edit the Home Page with some content to see it in action!

> WHAT OTHER FIELDS CAN YOU ADD TO A PAGE? Well, you can add Django fields like `models.CharField` and Wagtail StreamField Blocks - check out the [StreamField reference](https://docs.wagtail.io/en/stable/reference/streamfield/index.html) to learn more!


Customizing Your Site - Part II
-------------------------------

1. Now let's make our own page model and template!

**I added some new imports at the top, so now my imports look like this:**

```
from wagtail.core.models import Page
from wagtail.core import blocks
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.blocks import ImageChooserBlock

```

2. Then I created my basic Web Page model. I added the template to `home` > `templates` > `home` and specified in my model which template I am going to use. Then I added the content fields that I wanted for my Web Page. This is my code:


```
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

```

3. Go ahead and `makemigrations` and `migrate`.

4. Now in our `web_page.html` template, we can copy some of the code from the Home Page template. We will need to load `wagtailimages_tags` at the top, though, because we have images in this model that are not in the RichTextField.

> NOTE: You can use logic in Wagtail templates the same way you use them in Django templates! Remember that Wagtail uses the same templating system as Django.

5. This is the code for my template (with very basic layout and styling):

```
{% extends "base.html" %}
{% load static wagtailcore_tags wagtailimages_tags %}

{% block body_class %}template-homepage{% endblock %}

{% block extra_css %}{% endblock extra_css %}

{% block content %}
<div class="container-fluid">
    <div class="row">
        {% if page.cover_image %}
        {% image page.cover_image fill-2000x1000 as cover_image %}
        <div class="col-12 py-5 text-white text-center" style="background-image:url({{cover_image.url}});background-repeat:no-repeat;">
            <div class="py-3">
                <h2>{{page.title}}</h2>
                <h3>{{page.subtitle}}</h3>
            </div>
        </div>
        {% endif %}
    </div>
</div>

<div class="container">
    <div class="row my-3">
        {% for block in page.body %}
        <div class="col-12">
            {% include_block block %}
        </div>
        {% endfor %}
    </div>
</div>
{% endblock content %}

```

6. Now `runserver`, create a new Web Page, add some content, and see what it looks like!

You have just created a Wagtail website! CONGRATULATIONS! 🎉🎉🎉

**Wagtail is fun to build and easy to use for editors.**

Next Steps
----------

Add more pages, further customize your templates, and play around with the editor.