from django.db import models
from django.db import models


class File(models.Model):
    FILE_TYPES = [
        ('image', 'Image'),
        ('audio', 'Audio'),
        ('text', 'Text'),
    ]

    file_id = models.AutoField(primary_key=True)
    file_type = models.CharField(max_length=10, choices=FILE_TYPES)
    file_path = models.FileField(upload_to='uploads/')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.file_type} - {self.file_path.name}'

class ReportForm(models.Model):
    form_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    required_file_types = models.JSONField()

    def __str__(self):
        return self.name

class Report(models.Model):
    report_id = models.AutoField(primary_key=True)
    report_form = models.ForeignKey(ReportForm, on_delete=models.CASCADE)
    text_content = models.TextField()
    files = models.ManyToManyField(File, related_name='reports')

    def __str__(self):
        return f'Report {self.report_id} for {self.report_form.name}'
