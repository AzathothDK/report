from rest_framework import serializers
from .models import File, Report, ReportForm

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'


class ReportFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportForm
        fields = '__all__'


class ReportSerializer(serializers.ModelSerializer):
    files = FileSerializer(many=True, read_only=True)

    class Meta:
        model = Report
        fields = '__all__'
