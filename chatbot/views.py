from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ChatInputSerializer
from .bot import get_bot_response

class ChatBotView(APIView):
    permission_classes = []

    def post(self, request):
        serializer = ChatInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user_message = serializer.validated_data['message']
        bot_response = get_bot_response(user_message)

        return Response({
            "user_message": user_message,
            "bot_response": bot_response
        })
