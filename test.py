""" Poking around a little to see how the functions work """

import os
import re
import django
from django.conf import settings
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

# Set up Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wiki.settings")
django.setup()

def main():
    entry = get_entry("CSS")
    print(entry)

def list_entries():
    """
    Returns a list of all names of encyclopedia entries.
    """
    _, filenames = default_storage.listdir("entries")
    return list(sorted(re.sub(r"\.md$", "", filename)
                for filename in filenames if filename.endswith(".md")))

def save_entry(title, content):
    """
    Saves an encyclopedia entry, given its title and Markdown
    content. If an existing entry with the same title already exists,
    it is replaced.
    """
    filename = f"entries/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
    default_storage.save(filename, ContentFile(content))

def get_entry(title):
    """
    Retrieves an encyclopedia entry by its title. If no such
    entry exists, the function returns None.
    """
    try:
        f = default_storage.open(f"entries/{title}.md")
        return f.read().decode("utf-8")
    except FileNotFoundError:
        return None

if __name__ == "__main__":
    main()
