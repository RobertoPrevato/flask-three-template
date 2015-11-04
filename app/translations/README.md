## `/app/translations` Translations files

Translations files .po for the application. To compile .po files in .mo files utilized by Babel, one of the possible
ways is to run this command:
```bash
pybabel compile -d app/translations -f
```

Requires Flask-Babel module.

