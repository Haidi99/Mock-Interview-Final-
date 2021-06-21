from rest_framework.decorators import api_view
from twilio.twiml.voice_response import Gather, VoiceResponse


@api_view(
    ["GET"],
)
def getting_audio_from_user(request):
    if request.method == "GET":
        response = VoiceResponse()
        response.gather()

        return response()
