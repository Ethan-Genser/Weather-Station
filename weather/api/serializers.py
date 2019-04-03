from rest_framework import serializers
from . import models

class TemperatureSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'celcius', 'change', 'time_stamp')
        model = models.Temperature
        
        # cd ~/weather/weather
        # sudo apt install nginx
        # y
        # cd /etc/nginx/sites-enabled
        # 