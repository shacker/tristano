=====================

INSTALL

pip install -r requirements.txt
pip install psycopg2
cd requirements
bower install
./manage.py syncdb
./manage.py migrate


=====================

STATIC FILE GENERATION

`bower install` installs apps to `static/bower_components`, including foundation and angular

Our own scss and js lives in `static`

In `static/styles/sass/app.scss` we import selective bower-installed foundation components, then override with our own styles and settings, which live in the same dir.

Compass compiles our custom scss from `static/styles/sass` to `static/styles/css`

Thus, generated `styles/css/app.css` includes all of foundations plus our overrides.

To compile, use:
  alias tunes='compass compile --sass-dir tunedex/static/styles/sass --css-dir tunedex/static/styles/css'

In dev mode, we serve directly out of `static`.

In production, `collectstatic` copies all of this plus media included with installed apps over to `static_apps`, which is where everything gets served from.

=====================

