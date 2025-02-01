from typing import List, Optional
from ..base import TTSProvider
import requests
import base64

class KokorosTTS(TTSProvider):
    """Kokoros Text-to-Speech provider."""
    def __init__(self, api_key: Optional[str] = None, model: str = "tts-1-hd"):
        self.model = model

    def generate_audio(self, text: str, voice: str, model: str, voice2: str = None) -> bytes:
        """Generate audio using Kokoros API."""

        # Perform http request to http://localhost:3000/v1/audio/speech with payload:
            # {
            #    "input": text,
            #    "voice": voice,
            #    "model": model,
            #    "return_audio": true
            # }

        resp = requests.post('http://localhost:3030/v1/audio/speech', json={
            "input": text,
            "voice": voice,
            "model": self.model or "k82",
            "return_audio": True
        })

        if resp.status_code != 200:
            raise RuntimeError(f"Failed to generate audio: {resp.text}")

        # Base64 decode the `audio` field from the json response
        decoded = base64.b64decode(resp.json()['audio'])
        return decoded
