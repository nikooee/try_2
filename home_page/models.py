from django.db import models


# Create your models here.
class Artist(models.Model):
    f_name = models.CharField(max_length=20, null=True)
    l_name = models.CharField(max_length=20, null=True, blank=True)
    nick_name = models.CharField(max_length=20, null=True, blank=True)
    avatar = models.ImageField(null=True, blank=False, upload_to='albums/%Y-%m-%d/')

    def save(self,*args, **kwargs):
        if self.f_name or self.l_name or self.nick_name:
            super(self).save(*args, **kwargs)


    def __str__(self):
        if self.f_name and self.l_name:
            return self.f_name + '' + self.l_name
        elif self.f_name:
            return self.f_name
        elif self.l_name:
            return self.l_name
        elif self.nick_name:
            return self.nick_name
        else:
            return ''


class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True)  # any album has an artist which should relate to the Artist model
    title = models.CharField(max_length=20, null=True)
    description = models.CharField(max_length=20, null=True)
    summary = models.TextField(null=True)
    rate = models.FloatField(null=True, default=0)
    like = models.PositiveIntegerField(null=True, default=0)
    release_date = models.DateField(null=True)
    cover = models.ImageField(null=True, blank=False, upload_to='albums/%Y-%m-%d/')

    def __str__(self):
        return self.title


class Image(models.Model):
#    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=20, null=True)
    Image = models.FileField(null=True, blank=False, upload_to='albums/%Y-%m-%d/')

    def __str__(self):
        return self.title


class Tag(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=20, null=True)

