from .models import Activity, ActivityMaster, ActivityChild
from rest_framework import serializers


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['in_id', 'activity_name', 'user', 'project']


class ActivityMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityMaster
        fields = ['in_id', 'in_activity_id', 'dt_utc_start_time', 'dt_utc_end_time', 'in_mouse_count',
                  'in_keyboard_count', 'in_screenshot_count', 'in_webcam_count']


class ActivityChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityChild
        fields = ['in_id', 'in_session_id', 'dt_utc_start_time', 'dt_utc_end_time', 'in_mouse_count',
                  'in_keyboard_count']
