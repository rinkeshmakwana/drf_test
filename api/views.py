from django.db.models import F
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import ActivityMaster, ActivityChild
from .serializers import ActivityMasterSerializer, ActivityChildSerializer


class ActivityViewSet(ModelViewSet):
    queryset = ActivityMaster.objects.all()
    serializer_class = ActivityMasterSerializer


class MyDailyActivitySyncAPIView(CreateAPIView):
    queryset = ActivityMaster.objects.all()
    serializer_class = ActivityMasterSerializer

    def post(self, request, *args, **kwargs):
        try:
            print(request.data)
            session_id = request.data['in_session_id']
            session_exists = ActivityMaster.objects.filter(in_id=session_id)
            if session_exists:
                session_exists.update(dt_utc_end_time=request.data['dt_utc_end_time'],
                                      in_mouse_count=F('in_mouse_count')+request.data['in_mouse_count'],
                                      in_keyboard_count=F('in_keyboard_count')+request.data['in_keyboard_count'],
                                      in_screenshot_count=F('in_screenshot_count')+request.data['in_screenshot_count'],
                                      in_webcam_count=F('in_webcam_count')+request.data['in_webcam_count'])
                child_data = {
                    "in_session_id": session_exists.get(),
                    "dt_utc_start_time": request.data['dt_utc_start_time'],
                    "dt_utc_end_time": request.data['dt_utc_end_time'],
                    "in_mouse_count": request.data['in_mouse_count'],
                    "in_keyboard_count": request.data['in_keyboard_count']
                }
                serializer = ActivityChildSerializer(data=child_data)
                if serializer.is_valid():
                    serializer.save()
            data = {"MESSAGE": "Synced Successfully"}
            return Response(data)

        except Exception as e:
            data = {"MESSAGE": str(e)}
            return Response(data)
