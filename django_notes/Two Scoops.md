#### Ch.1 ####
Black to auto-format code
Flake8 to enforce Pep8 - can install VSCode extension
Can create pre-commit hooks to deny a commit if the code style is violated.
Switch from conda to virtual envs and pyproject.toml for standalone python project repos.
See .vscode file in the first Django project for configuring flake8 and Black.

Relative imports
No import *

ESLint for Javascript

#### Ch.2 ####
Use PostgreSQL when developing.
conda vs pip + virtualenv.

#### Ch.3 ####
Cookiecutter for advanced project templating.
Re-arranging project structure to `configuration_root` and `django_project_root`, but that seems to be a thing for more complex projects.

#### Ch.4 ####
App names = single word
Apps = singular focus, small
Common + uncommon app modules.

#### Ch.5 ####
Changing settings in prod => server restart.
Keep secret keys out of version control (automatic tools can be incorporated in GitHub actions, e.g.: Trufflehog)
No `local_settings.py` 
Multiple settings files: `base, local, staging, test, production` + select it at server runtime OR set `DJANGO_SETTINGS_MODULE` 
If multiple settings files => maybe multiple requirements files.
Unset env vars after you no longer need them.

!! Custom environment variable loading function -> throw custom error.
Packages for this: `django-environ`, `django-configurations`

`django-admin` for multiple setting files?

For services in which environment variables do not work, is it possible to encrypt/decrypt the config files with an environment variable?

### Ch.6 - Models###
Django abstract base class for common fields?
Custom save and delete methods -> won't be called by RunPython.
Always back up data before a migration.
Can take a while if you have a lot of data.

Start with models representing a normalised database (google 1NF -> 4NF ).
If denormalisation is necessary, try caching first.

When to use `null vs blank`:
- text fields: blank = True => stored as empty strings unless null=True and unique=True, then stored as NULL
- images/files: no null, blank ok;
- boolean, numbers, dates, keys, IP, many to many: both ok; if blank=True => also set null=true;

BinaryField - if too large => save to file + FileField

When saving numeric data from Python to Postgres, check that it fits.

Model  `_meta` API.

Model Manager = interface used when interacting with the database (through the ORM) - stored in `objects`?

Rather than having big models, you can do:
- Abstract classes representing behaviors that you can import into your models (e.g: Publishable, Timestampable, etc.)
OR
- Stateless helper functions.


### Ch.7 Queries and the DB layer ###
`get_object_or_404()` = for getting single objects in Views;
`django.core.exceptions.ObjectDoesNotExist` vs `ModelName.DoesNotExist` vs 
`ModelName.MultipleObjectsReturned`

Doing something like `for customer in Customer.objects.iterator()` is bad, as it retrieves objects from the DB one by one and can create race conditions => use query expressions.
Aka example: `Customer.objects.filter(scoops_ordered__gt=F('store_visits'))`

Processing the data in Python is slower than in the DB.

If you need to write SQL, prefer `raw()` over `extra()`. Only do it if the ORM can't handle a query or you can do something more efficient (?). Examples:
- Window functions, advanced joins, unions, groupbys.
- Bulk inserts/updates.
- DB-specific features (e.g: tsvector, tsquery in postgres)

Indexing:
- If it's used frequently (10-25% of all queries).
- Can run tests to determine if indexing leads to an improvement in results.
- `pg_stat_activity` to gauge usage

Default ORM behaviour - autocommit (e.g: after every create/update etc). Can be bad for large sites.
`ATOMIC_REQUESTS` set to true => all requests are wrapped in a transaction. 
`transaction.non_atomic_requests()` = e.g: confirmation email then transaction is rolled back; with this decorator, behavior is back to autocommit inside that function and you can handle error states appropriately;
Ideally, should use transactions for creating, modifying and deleting data.

### Ch.8 - function and class-based Views ###
If you need to tinker a lot with it to make it a class-based View -> consider a function view.
Keep logic out of urls.py. Keep business logic out of Views. Put it into model methods, manager methods and general utility helpers instead.
Use URL namespaces (`tastings:detail`, not `tastings_detail`)

### Ch.9 - FBV Best practices ###
Class-agnostic functionality. E.g: checking a user's permissions.
Can transform them into decorators sometimes.
Impose a hard limit on how many decorators your views can have.
No CBVs guide - a lot of good points: https://spookylukey.github.io/django-views-the-right-way/dependency-injection.html

### Ch.10 - CBV Best practices ###
`django-braces` = more useful mixins;
`ccbv.co.uk` = must read whenever working with CBVs;
Mixin = class that provides functionality to be inherited, but is not meant to be instantiated on its own.
Mixins to the left, base views to the right.

GCBVs = Generic CBV -> complex inheritance chains
When using LoginRequiredMixin -> if dispatch is overridden, call super() immediately.

### Forms
Can use form validation for general incoming data validation. (neat trick!)

### Other tips and tricks
Django admin - move it from the default address, can leave honeypot at /admin
https://djangopackages.org/
User uploaded files - careful and extensive validation.
Vulnerability reporting page
Never display sequential primary keys.
Password hashers?
Log management - https://www.loggly.com/ 








