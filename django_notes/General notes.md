- Django "apps" are re-usable submodules/packages.

- Redirecting URL from project to a submodule (include in project's urls.py):
```
urlpatterns = [   
    path("app_name/", include("app_name.urls"))  
]
```
- Mapping route to view: ```
```
from django.urls import path
path(path, view function)
```
- Dynamic segment: `path("<var_name>", views.func, name="path_name")`, with signature `func(request, var_name)`
	Alternatively: `path("<type:var_name>", views.func)`
- HttpResponseRedirect
- There doesn't seem to be a direct equivalent to Spring's DI, which seems a bit inconvenient.
- HTML templates: `django.shortcuts.render(request, path_to_template, **kwargs)` + modify `TEMPLATES[DIRS]` in `settings.py` OR after initialising an app + adding templates for it, add it in `settings.py INSTALLED_APPS` variable. 
- Template filters = for small aesthetic transformations on variables we display.
- Django DTL and tags: url (for redirections, can use the identifiers in urls.py), for, if.

- Loading static files: `{% load static %}` -> `{% static "path_to_css"%}`
- Global css: add `STATICFILES_DIRS` to settings.
- Slugs: `<slug:slug_name>` makes sure that the path-is-in-this-format.
- Reverse to construct app URLs.
- TemplateView, ListView, DetailView, FormView, CreateView

# Data #

Good to think of it as having three types:
- Temporary data: used immediately, don't care about it later, stored in memory; e.g: user input
- Semi-persistent data: stored for a longer time, can be lost and re-created when needed; stored in browser or temp files; e.g: user authentication status;
- Persistent data: stored "forever", must not be lost, stored in a DB; e.g: blog posts, orders, payment methods etc;

SQL vs noSQL - table vs document based;

Setting primary key: `city_id = models.AutoField(primary_key=True)`
Otherwise, it's automatically created and named "id".
After creating or updating a model class, you have to create + run the migrations.

Can create object based on the declared "fields" (init automatically created).
Save it with `object.save()`, retrieve it with `ClassName.objects.all()`, delete it with `object.delete()`, .. `ClassName.objects.create`

Querying data with e.g: `ClassName.objects.get(id=3)` get matches only one value, errors if multiple matches.
`ClassName.objects.filter(filter_stmt)` -> for multiple matches.
Example filter stmt: `rating__lt=3`

More complex queries: 
`from django.db.models import Q
`ClassName.objects.filter(Q(rating__lt=3)|Q(is_bestselling=True))`

"id: may not exist, but "pk" always does.

Cached queries?

Use django.core.validators to .. validate the data.

(blank=True) != (null=True)
If blank = True, must provide a default value for non-string fields. For string fields, blank is naturally an empty string.

`get_absolute_url` override on model object

Primary database + replica database + deploying to cloud and testing

### Serving uploaded files ###
`MEDIA_ROOT = BASE_DIR / "uploads"` setting in settings.py to modify where files are saved
`MEDIA_URL = "/user-media/"` = creating pre-amble for exposing files
Add `+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)` at the end of main project urls file. 
Imports: ```
from django.conf.urls.static import static
from django.conf import settings```
Importing the image: `<img src="{{ post.image.url }}/>"`

`if settings.DEBUG` -> toggle where static files are served from based on the environment type;

**`STATIC_URL`**: URL path used in templates and for linking static files.
**`STATIC_ROOT`**: Directory path where static files are collected when running `collectstatic` (mainly for production).
Same for media.

`uuid.uuid4()` to generate a random file name when uploading (remove the extension before generating and re-add it after).

### Relations ###
ForeignKey is used for one to many relations.
OneToOneField...
ManyToManyModel - creates a mapping table automatically
Other types of relations: circular, self, other apps' models.

`models.ForeignKey(className, on_delete=models.CASCADE|PROTECT|SET_NULL, related_name="books")` 
Related name allows you to e.g: get all the "books belonging to an author".

Chaining filters: `Book.objects.filter(author__last_name__contains="wling")`

Meta class inside a Model class to control how it is displayed?

# Security #
CSRF tokens on POST requests
CSP app against XSS

# Deployment #
Need a WSGI or ASGI server.
`runserver` is for debug purposes only.
Serving static files:
- Can configure Django to serve them (via urls.py) - ok for small sites, slow, not preferred.
- Configure web server to serve static files alongside the Django app - same server and device but separate processes
- Use dedicates service/server for static and uploaded files - more complex initial setup but offers best performance.

STATIC_URL (things written by you) should be kept different from MEDIA_URL (user-uploaded files) - security consideration so files uploaded by you can't be overwritten by malicious users.

`STATIC_ROOT = BASE_DIR / "staticfiles"`
`python manage.py collectstatic`

# Testing #
`SimpleTestCase` - no DB, `TestCase` - with DB
`unittest.mock` - `Mock, MagicMock` = mocking objects
			   - `patch` = mock code
DRF: 
```
from rest_framework.test import APIClient
client = ApiClient()
res = client.get('/greetings/')
```
Then, you can use `res.status_code`, `res.data`, etc...

Use either `tests.py` file or `tests` folder (with `__init__.py` in it), not both. Django looks for modules beginning with `test`.

The test client = dummy web browser = simulate HTTP requests, see redirects + status codes + see that a given request is rendered by a Django template
`from django.test import Client`
Not a replacement for Selenium (tests rendered HTML + JS behaviour) - just checking that the correct templates are being rendered + that it receives correct context data.
`RequestFactory` for testing view functions directly

Each test inside a TestCase subclass is run inside a transaction and then the DB is flushed.

# Docker #
psycopg2 binary on Alpine needs: `postgresql-client, build-base, postgresql-dev, musl-dev` - you seem to need a special build phase for this + Alpine doesn't seem to be recommended if you want to do this in a production environment. Use python slim instead.

`PYTHONUNBUFFERED=1` -> don't buffer stdout and stderr
`PYTHONDONTWRITEBYTECODE=1` -> prevents writing `.pyc` files to disk

`depends_on` = ensures service starts, but doesn't ensure that the application on it is running => race condition possible
DB service starting -> Django service starting; if Django finished initialising before the DB => not good
Solution: make Django wait for db; can do outside Django with a bash script + healthcheck OR inside Django (google wait_for_db.py)

`docker compose down -v` on dev if password doesn't work -> user misconfiguration?

Is running Django in Docker really necessary?

# User Model #
User model manager -> custom logic for creating objects (e.g: hash password)
                  -> creating superUser;
`BaseUserManager` 
`from django.contrib.auth import get_user_model` -> will get default user model for the current app(?)

`AUTH_USER_MODEL = "core.User"` 

Adding a user as a foreign key.
```python
from django.conf import settings

class Article(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
```

# API #

**What to document?**:
- Available endpoints.
- Supported methods.
- Format of payloads (params + JSON format)
- Authentication process
=> generate documentation automatically **drf-spectacular**

`drf_spectacular.views.SpectacularAPIView | SpectacularSwaggerView`

`APIView` = focused around http methods, class method for each of them. Useful for non CRUD APIs - e.g: authentication, running jobs, using external APIs.

`Viewsets` = focused around CRUD, map to Django models, use Routers to generate URLs;

```
router = DefaultRouter()
router.register("recipes", views.RecipeViewSet)
```
Router will create API endpoints depending on what's declared in the view set.
Then, you have to include(router.urls) to urlpatterns.

# DRF #
Public tests = unauthenticated requests (i.e: creating a user)
```
from rest_framework.test import APIClient
from rest_framework import status
```

```
# Allows reverse("user:create")
app_name = "user"
urlpatterns = [path("create/", views.CreateUserView.as_view(), name="create")]
```

Authentication types supported by DRF:
- basic = send username and password with each request -> bad.
- token = use a token in the HTTP header for each request to the API;
- OAuth2 (need 3rd party package)
- session cookies;
JWT does not seem to be natively supported, 3rd party package exists for it too though!
token = database hit per login request, JWT with refresh token can alleviate this

Token authentication: need to create a token serializer, view (`ObtainAuthToken`) then add to urls.

`generics.RetrieveUpdateAPIView` = View for updating an authenticated user; permission_classes, authentication_classes, serializer_class, get_object

Nested serializers are read-only by default.

Serialization: object -> e.g: JSON data
De-serialization: e.g: JSON data -> object

Client sends data to an API endpoint -> Data is de-serialized and available as `validated_data` if de-serialization was successful -> custom create, update methods to actually create or update objects and save them to DB implicitly.

The `"-detail"` part is a convention used by DRF's default router to name the URL pattern for retrieving a single instance of a model. `reverse('appname:model-detail', args=[object_id])` = retrieve the URL corresponding to the model object with id `object-id`.

`model-list` = retrieve all the instances of the model;

Creating a custom ViewSet action (e.g: for uploading an image).

For uploading an image through the API web page:
```python
SPECTACULAR_SETTINGS = {
"COMPONENT_SPLIT_REQUEST": True,
}
```

### REST API course thoughts ###
(Maybe include in repo README after)
- App structure is messy, you can't have a Recipe app with its corresponding model defined in another app. As far as I understood, apps should be package-like, in that you could import them in another application and re-use them?
- The whole concepts of apps in Django is a bit weird. The naming is confusing, it seems to want to reinvent the wheel. Consider having a large app with submodules instead in subsequent projects.
- Code re-usability (DRY). Test files would benefit from a test utilities folder. Instructor does address it though. Test files would also benefit from being able to create dummy model objects in a standardized manner.
- APIs pretty similar to each other, good practice writing the code before watching the video though.

### Deploying a Django App ###
WSGI - runs the Python code
Persistent data (stateless)
Reverse proxy (handles requests from users + serves data more efficiently than a WSGI server)

Nginx - looks much more complex than I expected.

### Mixins ###
To know if two mixins compose as intended, you need to know both their implementations (and potentially tinker with them). 
e.g: 2x`UserPassesTestMixin` would not work together (only 1 of them will actually work, the other silently fails (?)).