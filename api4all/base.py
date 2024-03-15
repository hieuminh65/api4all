"""
The TextEngine provides quick start code for state-of-the-art providers and their AI models.
"""

from typing import Optional, List, Dict, Union, Any
from abc import ABC, abstractmethod
from api4all.logger.base_logger import setup_logger
from .keys import Keys
from .data.data import dataEngine
from .utils.models import TextResponse
from .utils.configs import ModelConfig


class TextEngine(ABC):
    def __init__(self,
                model: str,
                provider: str,
                temperature: Optional[float] = ModelConfig.DEFAULT_TEMPERATURE,
                max_tokens: Optional[int] = ModelConfig.DEFAULT_MAX_TOKENS,
                top_p: Optional[float] = ModelConfig.DEFAULT_TOP_P,
                stop: Union[str, List[str], None] = ModelConfig.DEFAULT_STOP,
                messages: Optional[List[Dict[str, str]]] = ModelConfig.MESSAGES_EXAMPLE
                ) -> None:
        
        """
        Initialize the TextEngine with the following parameters:
        - model: the API string name of the model to use. Available models are listed in the README.
        - temperature: the sampling temperature to use. A float between 0.0 and 2.0.
        - max_tokens: the maximum number of tokens to generate. An integer between 1 and the context length of the model.
        - top_p: the nucleus sampling probability to use. A float between 0.0 and 1.0.
        - stop: the stop sequence to use. A string or a list of strings.
        - provider: the provider to use. Available providers are listed in the README.
        - messages: the messages to use. A list of dictionaries with a 'role' and 'content' key.
        """

        self.logger = setup_logger()

        self.model = model
        if (model is None) or (model not in dataEngine.models):
            self.logger.error(f"Invalid model")
            raise ValueError(f"Please select a model from {dataEngine.models}")

        self.provider = provider
        if (provider is None) or (provider not in dataEngine.getProvidersForModel(model)):
            self.logger.error(f"Invalid provider")
            raise ValueError(f"This model is not supported or non-existed. Please select a provider from {dataEngine.getProvidersForModel(model)} that supports the {model} model")
        

        self.temperature = temperature
        if (temperature is None) or (temperature < 0.0) or (temperature > 2.0):
            self.logger.error(f"Invalid temperature")
            raise ValueError(f"Please select a temperature between 0.0 and 2.0")
        

        self.max_tokens = max_tokens
        if (max_tokens < 1) or (max_tokens > dataEngine.getContextLength(model)):
            self.logger.error(f"Invalid max tokens")
            raise ValueError(f"The context length of this model is {dataEngine.getContextLength(model)}")
        

        self.top_p = top_p
        if (top_p < 0) or (top_p > 1):
            self.logger.error(f"Invalid top p")
            raise ValueError(f"Please select a top p between 0.0 and 1.0")
        

        self.stop = stop
        if (stop is not None) and (not isinstance(stop, (str, list))):
            self.logger.error(f"Invalid stop sequence")
            raise ValueError(f"Stop should be a string or a list of strings")

        
        self.messages = messages
        if not all(isinstance(message, dict) and 'role' in message and 'content' in message for message in messages):
            self.logger.error(f"Invalid messages format")
            raise ValueError("Each message should be a dictionary with a 'role' and 'content' key")
        
        self._keys = Keys()


    @abstractmethod
    def generate_response(self,
                        messages: Optional[List[Dict[str, str]]] = None,
                        model: Optional[str] = None,
                        temperature: Optional[float] = None,
                        max_tokens: Optional[int] = None,
                        top_p: Optional[float] = None,
                        **kwargs: Any
                        ) -> Union[TextResponse, None]:
        """
        This method is used to generate a response from the AI model.

        """
        ...