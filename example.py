import logging
from api import BetaFaceAPI

logging.basicConfig(level = logging.INFO)
client = BetaFaceAPI()

client.upload_face('me.jpg', 'avijoy@beta.ro')
matches = client.recognize_faces('randompic.jpg', 'beta.ro')
print(matches)
