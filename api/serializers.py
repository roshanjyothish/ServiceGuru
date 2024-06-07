from rest_framework import serializers

from api.models import Work,Customer


class WorkSerializer(serializers.ModelSerializer):

    customer=serializers.StringRelatedField(read_only=True)

    class Meta:

        model=Work

        fields="__all__"

        read_only_fields=['id','customer','created_date','update_date','is_active']



class CustomerSerilizer(serializers.ModelSerializer):

    technician=serializers.StringRelatedField(read_only=True)

    work_count=serializers.StringRelatedField(read_only=True)

    work_total=serializers.IntegerField(read_only=True)

    class Meta:

        model=Customer

        fields='__all__'

        read_only_fields=['id','technician','status','created_date','update_date','is_active']