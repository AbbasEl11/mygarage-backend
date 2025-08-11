# show_urls.py
import os
import django
from django.urls import URLPattern, URLResolver, get_resolver


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

def list_urls(patterns, prefix=''):
    for p in patterns:
        if isinstance(p, URLPattern):
            print(f"{prefix}{p.pattern}  →  {p.callback}")
        elif isinstance(p, URLResolver):
            # dive into include(...)
            list_urls(p.url_patterns, prefix + str(p.pattern))

resolver = get_resolver()
print("=== Alle registrierten URL-Muster ===")
list_urls(resolver.url_patterns)
