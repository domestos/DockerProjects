from rest_framework import serializers
from .models import Employee , Position
#
# class PositionSerializer(serializers.ModelSerializer):
#      id = serializers.IntegerField(read_only=True)
#
#     class Meta:
#         model = Position
#         fields = (
#             'id', 'position',
#         )

class EmployeeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    #position = PositionSerializer()

    class Meta:
        model = Employee
        fields = ('id', 'name', 'position_id', 'first_work_day', 'last_work_dat',)
