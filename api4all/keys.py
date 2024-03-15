from typing import Optional, List, Dict
from dotenv import find_dotenv, load_dotenv
import os

class Keys:
    """
    
    This class is used to get the available API keys from the environment variables.

    """
    def __init__(self,
                GROQ_API_KEY: Optional[str] = None,
                OPENAI_API_KEY: Optional[str] = None,
                ANYSCALE_API_KEY: Optional[str] = None,
                TOGETHER_API_KEY: Optional[str] = None,
                # Google Cloud Credentials #
                GOOGLE_API_KEY: Optional[str] = None,
                GOOGLE_CLOUD_PROJECT: Optional[str] = None,
                GOOGLE_REGION: Optional[str] = None,
                # ------------------------ #
                MISTRAL_API_KEY: Optional[str] = None,
                ANTHROPIC_API_KEY: Optional[str] = None,
                FIREWORKS_API_KEY: Optional[str] = None,
                REPLICATE_API_KEY: Optional[str] = None,
                DEEPINFRA_API_KEY: Optional[str] = None,

                ) -> None:
        self._find_dotenv()

    def _find_dotenv(self) -> str:
        dotenv_path = find_dotenv()
        if dotenv_path:
            load_dotenv(dotenv_path)
        else:
            print("No .env file found.")
        return dotenv_path
            
    def get_api_keys(self, api_key_name: str) -> str:
        """
        This method is used to get the available API keys from the environment variables.

        """
        api_key = os.getenv(api_key_name)
        if api_key is None:
            print(f"Environment variable {api_key_name} is not set")
            return None
        return api_key