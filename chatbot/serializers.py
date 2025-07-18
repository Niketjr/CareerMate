from rest_framework import serializers

class ChatInputSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=1000)
