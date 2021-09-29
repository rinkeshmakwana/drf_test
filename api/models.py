from django.db import models

# Create your models here.

class Activity(models.Model):
    in_id = models.AutoField(auto_created=True, primary_key=True)
    activity_name = models.CharField(max_length=100)
    user = models.CharField(max_length=40)
    project = models.CharField(max_length=50)

    def __str__(self):
        return self.activity_name


class ActivityMaster(models.Model):
    in_id = models.BigIntegerField(primary_key=True)
    in_activity_id = models.ForeignKey(Activity, related_name='activity_master', on_delete=models.CASCADE)
    dt_utc_start_time = models.DateTimeField()
    dt_utc_end_time = models.DateTimeField()
    in_mouse_count = models.IntegerField()
    in_keyboard_count = models.IntegerField()
    is_manual_entry = models.BooleanField(default=False)
    st_manual_entry_reason = models.CharField(max_length=100, blank=True, null=True)
    is_idle_mode = models.BooleanField(default=False)
    in_screenshot_count = models.IntegerField()
    in_webcam_count = models.IntegerField()


class ActivityChild(models.Model):
    in_id = models.AutoField(auto_created=True, primary_key=True)
    in_session_id = models.ForeignKey(ActivityMaster, related_name='activity_child', on_delete=models.CASCADE)
    dt_utc_start_time = models.DateTimeField()
    dt_utc_end_time = models.DateTimeField()
    in_mouse_count = models.IntegerField()
    in_keyboard_count = models.IntegerField()
