from rest_framework import viewsets
from .models import File, Report, ReportForm
from .serializers import FileSerializer, ReportSerializer, ReportFormSerializer
from rest_framework.response import Response
from rest_framework import status

class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer


class ReportFormViewSet(viewsets.ModelViewSet):
    queryset = ReportForm.objects.all()
    serializer_class = ReportFormSerializer


class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

    def create(self, request, *args, **kwargs):
        form_id = request.data.get('report_form')
        try:
            report_form = ReportForm.objects.get(pk=form_id)
        except ReportForm.DoesNotExist:
            return Response({"error": "Invalid report form ID"}, status=status.HTTP_400_BAD_REQUEST)

        required_file_types = set(report_form.required_file_types)
        uploaded_file_types = {file['file_type'] for file in request.data.get('files', [])}

        if not required_file_types.issubset(uploaded_file_types):
            return Response({"error": "Missing required file types"}, status=status.HTTP_400_BAD_REQUEST)

        return super().create(request, *args, **kwargs)