from rest_framework import serializers #type:ignore
from applications.ps1.models import IndentFile, File ,StockEntry,StockItem,StockTransfer,IndentItem
from applications.globals.models import ExtraInfo, HoldsDesignation
from applications.filetracking.models import Tracking

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'

# class IndentFileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = IndentFile
#         fields = '__all__'

# arun__________start______
class IndentItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndentItem
        fields = '__all__'

class IndentFileSerializer(serializers.ModelSerializer):
    items = IndentItemSerializer(many=True, read_only=True)  # Nested serializer for related items

    class Meta:
        model = IndentFile
        fields = '__all__'
# arun__________end______

class ExtraInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraInfo
        fields = '__all__'

class HoldsDesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = HoldsDesignation
        fields = '__all__'

class TrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tracking
        fields = '__all__'

class StockEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = StockEntry
        fields = '__all__'

class StockItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockItem
        fields = '__all__'

class StockTransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockTransfer
        fields = '__all__'

