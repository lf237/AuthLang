from django.db import models
from main.models.category_type import CategoryType
from django.template.defaultfilters import slugify


class Category(models.Model):
    # Category "other" object has PK 1 and name "other"
    # Loaded through fixture main/fixture/initinal_data.json
    DEFAULT_PK = 1
    category = models.CharField(max_length = 200, unique = True)
    category_type = models.ForeignKey('CategoryType', default = CategoryType.DEFAULT_PK)
    slug = models.CharField(max_length = 200, blank = True)

    def __unicode__(self):
        return self.category

    def get_unique_slug(self, slug, index):
        # index > 1 means that the slug is not unqiue
        if index > 1:
            # Add index to the end of slug and truncate slug to the proper
            # length of 200
            index_str = str(index)
            new_slug_len = 199 - len(index_str)
            new_slug = slug[:new_slug_len] + "-" + index_str
        else:
            new_slug = slug
        # Check for uniqueness
        if Category.objects.filter(slug=new_slug).first() == None:
            return new_slug[:200]
        else:
            return self.get_unique_slug(slug, index + 1)

    def save(self, *args, **kwargs):
        # Slugify: https://docs.djangoproject.com/en/1.8/ref/templates/builtins/#slugify
        #
        # Slug is auto-generated using the field 'category' if not specified.
        # Slugifies the field 'slug' and trucates it to 200 chars.
        # This is for dynamic urls.
        if len(self.slug) == 0:
            slug = slugify(self.category)[:200]
        else:
            slug = slugify(self.slug)[:200]
        # Make slug is unique.
        #
        # If self.pk is None, this means that the object hasn't been created yet.
        # This implies that it is safe to check for unqiueness.
        if self.pk is None:
            self.slug = self.get_unique_slug(slug, 1)
        # Else this instance has been created already.
        # If slug is the same as what is already stored,
        # then skip checking for uniqueness.
        elif slug == Category.objects.get(pk = self.pk).slug:
            self.slug = slug
        # If the slug is different than what is stored,
        # Check for uniqueness
        else:
            self.slug = self.get_unique_slug(slug, 1)
        super(Category, self).save(*args, **kwargs)