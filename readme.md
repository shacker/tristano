# About

Tristano is a generic, ready-to-extend, responsive Django + Angular site based on:

- Zurb Foundation (CSS grid and UI widgets)
- AngularJS
- Django REST Framework (API generation)
- Django-AllAuth (for social network logins)
- Django Extensions
- Editable public profiles (via Markdown)
- Asset pipeline (compression and minification) via django-compressor
- Class-based generic views

Tristano is not intended to be installed as a reusable Django app. Instead, start a new project with it,
rename, remove the git history, add it to a new repo, and start tweaking.

postgres and a clean virtualenv are assumed, but season to taste.

# Installing

```
[create blank database `tristano` or other]
pip install -r requirements.txt
pip install psycopg2
cd requirements
bower install
mv local_settings.sample.py local_settings.py and tweak as needed
./manage.py migrate
```

Because apps are kept in the `apps` directory rather than in the project root, you'll need to add its path to your virtualenv:

```
cd apps
pwd [copy path to clipboard]
add2virtualenv [paste]
```

Rename the `project` directory to match the name of your current project and fix references to it in settings.

Via `/admin`, add a Site record for localhost.

Add at least one social network via Social Apps.


# Static File Management

`bower install` installs apps to `static/bower_components`, including foundation and angular

Our own scss and js lives in `static`

In `static/styles/sass/app.scss` we import selective bower-installed foundation components, then override with our own styles and settings, which live in the same dir.

Compass compiles our custom scss from `static/styles/sass` to `static/styles/css`

Thus, generated `styles/css/app.css` includes all of foundations plus our overrides.

To compile, use:
`cd tristano; compass compile`

Compass will use the input and output settings listed in `config.rb`.

Or, take advantage of the included config.rb by opening a 2nd terminal and running (from the main directory):
`compass watch`

In dev mode, we serve directly out of `static`.

In production, `collectstatic` copies all of this plus media included with installed apps over to `static_apps`, which is where everything gets served from.

Test django-compressor's minification by setting

`COMPRESS_ENABLED = True`

in `local_settings.py` and then viewing source.

# API

A simple books API (meant to be changed to whatever app/model you're building) is demonstrated via `django-rest-framework` with the `sampledata` app. Enter a few books, then access `/api/books` for the demo. Append `?format=json` to any REST URL for raw data.

# Versions

v 1.0: Initial release
