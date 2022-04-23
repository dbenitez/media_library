import hashlib
from pathlib import Path
import uuid
from django.db import models

class AttachmentType(models.Model):
    name = models.CharField(max_length=16)
    icon = models.FilePathField()


class AttachmentArchitecture(models.Model):
    name = models.CharField(max_length=16)
    icon = models.FilePathField()


# Create your models here.
class Attachment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=128)
    md5sum = models.CharField(max_length=32)
    file = models.FileField()
    type = models.ForeignKey(AttachmentType, on_delete=models.PROTECT)
    architecture = models.ForeignKey(AttachmentArchitecture, on_delete=models.PROTECT)
    size = models.PositiveIntegerField(default=0)
    description = models.TextField(blank=True, null=True)
    tree = models.TextField(default="[]")

    def calc_md5(self):
        md5 = hashlib.md5()
        for chunk in self.file.chunks():
            md5.update(chunk)
        self.md5sum = md5.hexdigest()

    def save(self, *args, **kwargs) -> None:
        if self.file and (self.name is None or len(self.name) == 0):
            file_path = self.file.path()
            self.name = Path(file_path).name

        if not self.pk and self.file:
            self.calc_md5()
            chk = Attachment.objects.filter(
                md5sum=self.md5sum, is_deleted=False).values("pk")
            setattr(self, 'already_exists', False)
            for x in chk:
                self.pk = x["pk"]
                self.refresh_from_db()
                setattr(self, 'already_exists', True)
                return self
        return super().save(*args, **kwargs)