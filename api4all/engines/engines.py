from typing import Optional, List, Dict, Union, Any
import time

from .factory import EngineFactory
from ..base import TextEngine
from ..data.data import dataEngine
from ..utils.models import TextResponse
from ..utils.configs import ModelConfig
from ..logger.base_logger import log_response

# providers dependencies
from groq import Groq
import openai
import replicate
import anthropic
from mistralai.client import MistralClient
import google.generativeai as genai

__all__ = ["GroqEngine", "AnyscaleEngine", "TogetherEngine", "FireworksEngine", "ReplicateEngine", "DeepinfraEngine", "OpenaiEngine", "AnthropicEngine", "MistralEngine", "GoogleEngine"]


#-----------------------------------------GROQ-----------------------------------------#
@EngineFactory.register_engine('groq')
class GroqEngine(TextEngine):
    def __init__(self,
                model: str,
                provider: str = "groq",
                temperature: Optional[float] = ModelConfig.DEFAULT_TEMPERATURE,
                max_tokens: Optional[int] = ModelConfig.DEFAULT_MAX_TOKENS,
                top_p: Optional[float] = ModelConfig.DEFAULT_TOP_P,
                stop: Union[str, List[str], None] = ModelConfig.DEFAULT_STOP,
                messages: Optional[List[Dict[str, str]]] = ModelConfig.MESSAGES_EXAMPLE
                ) -> None:
        super().__init__(model, provider, temperature, max_tokens, top_p, stop, messages)

        self._api_key = self._keys.get_api_keys("GROQ_API_KEY")
        if self._api_key is None:
            self.logger.error(f"API key not found for {self.provider}")
            raise ValueError(f"API key not found for {self.provider}")
        
        # Set up the client
        self._set_up_client()

        self._api_name = dataEngine.getAPIname(self.model, self.provider)


    def _set_up_client(self):
        self.client = Groq(api_key = self._api_key)


    def generate_response(self,
                        **kwargs: Any
                        ) -> Union[str, None]:
        """
        This method is used to generate a response from the AI model.

        """

        start_time = time.time()

        try:
            completion = self.client.chat.completions.create(
                messages=self.messages,
                model=self._api_name,
                temperature=self.temperature,
                max_tokens=self.max_tokens,
                top_p=self.top_p,
                stop=self.stop
            )
        except Exception as e:
            print(f"Error generating response: {e}")
            self.logger.error(f"Error generating response of provider {self.provider}: {e}")
            return None

        actual_time = time.time() - start_time

        content = completion.choices[0].message.content
        input_tokens = completion.usage.prompt_tokens
        output_tokens = completion.usage.completion_tokens
        execution_time = completion.usage.total_time
        cost = dataEngine.calculate_cost(self.provider, self.model, input_tokens, output_tokens)

        response = TextResponse(
            content=content,
            cost=cost,
            execution_time=execution_time,
            actual_time=actual_time,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            provider=self.provider
        )

        log_response(self.logger, "SUCCESS", response)

        return response


#-----------------------------------------Anyscale-----------------------------------------#
@EngineFactory.register_engine('anyscale')
class AnyscaleEngine(TextEngine):
    def __init__(self,
                model: str,
                provider: str = "anyscale",
                temperature: Optional[float] = ModelConfig.DEFAULT_TEMPERATURE,
                max_tokens: Optional[int] = ModelConfig.DEFAULT_MAX_TOKENS,
                top_p: Optional[float] = ModelConfig.DEFAULT_TOP_P,
                stop: Union[str, List[str], None] = ModelConfig.DEFAULT_STOP,
                messages: Optional[List[Dict[str, str]]] = ModelConfig.MESSAGES_EXAMPLE
                ) -> None:
        super().__init__(model, provider, temperature, max_tokens, top_p, stop, messages)

        self._api_key = self._keys.get_api_keys("ANYSCALE_API_KEY")
        if self._api_key is None:
            self.logger.error(f"API key not found for {self.provider}")
            raise ValueError(f"API key not found for {self.provider}")
        
        # Set up the client
        self._set_up_client()

        self._api_name = dataEngine.getAPIname(self.model, self.provider)


    def _set_up_client(self):
        self.client = openai.OpenAI(base_url="https://api.endpoints.anyscale.com/v1",
                                    api_key = self._api_key)


    def generate_response(self,
                        **kwargs: Any
                        ) -> Union[str, None]:
        """
        This method is used to generate a response from the AI model.

        """

        start_time = time.time()

        try:
            completion = self.client.chat.completions.create(
                messages=self.messages,
                model=self._api_name,
                temperature=self.temperature,
                max_tokens=self.max_tokens,
                top_p=self.top_p,
                stop=self.stop
            )
        except Exception as e:
            print(f"Error generating response: {e}")
            self.logger.error(f"Error generating response of provider {self.provider}: {e}")
            return None

        actual_time = time.time() - start_time

        content = completion.choices[0].message.content
        input_tokens = completion.usage.prompt_tokens
        output_tokens = completion.usage.completion_tokens
        execution_time = None
        cost = dataEngine.calculate_cost(self.provider, self.model, input_tokens, output_tokens)

        response = TextResponse(
            content=content,
            cost=cost,
            execution_time=execution_time,
            actual_time=actual_time,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            provider=self.provider
        )

        log_response(self.logger, "SUCCESS", response)

        return response


#-----------------------------------------TOGETHER AI-----------------------------------------#
@EngineFactory.register_engine('together')
class TogetherEngine(TextEngine):
    def __init__(self,
                model: str,
                provider: str = "together",
                temperature: Optional[float] = ModelConfig.DEFAULT_TEMPERATURE,
                max_tokens: Optional[int] = ModelConfig.DEFAULT_MAX_TOKENS,
                top_p: Optional[float] = ModelConfig.DEFAULT_TOP_P,
                stop: Union[str, List[str], None] = ModelConfig.DEFAULT_STOP,
                messages: Optional[List[Dict[str, str]]] = ModelConfig.MESSAGES_EXAMPLE
                ) -> None:
        super().__init__(model, provider, temperature, max_tokens, top_p, stop, messages)

        self._api_key = self._keys.get_api_keys("TOGETHER_API_KEY")
        if self._api_key is None:
            self.logger.error(f"API key not found for {self.provider}")
            raise ValueError(f"API key not found for {self.provider}")
        
        # Set up the client
        self._set_up_client()

        self._api_name = dataEngine.getAPIname(self.model, self.provider)


    def _set_up_client(self):
        self.client = openai.OpenAI(base_url="https://api.together.xyz/v1",
                                    api_key = self._api_key)


    def generate_response(self,
                        **kwargs: Any
                        ) -> Union[str, None]:
        """
        This method is used to generate a response from the AI model.

        """

        start_time = time.time()

        try:
            completion = self.client.chat.completions.create(
                messages=self.messages,
                model=self._api_name,
                temperature=self.temperature,
                max_tokens=self.max_tokens,
                top_p=self.top_p,
                stop=self.stop
            )
        except Exception as e:
            print(f"Error generating response: {e}")
            self.logger.error(f"Error generating response of provider {self.provider}: {e}")
            return None

        actual_time = time.time() - start_time

        content = completion.choices[0].message.content
        input_tokens = completion.usage.prompt_tokens
        output_tokens = completion.usage.completion_tokens
        execution_time = None
        cost = dataEngine.calculate_cost(self.provider, self.model, input_tokens, output_tokens)

        response = TextResponse(
            content=content,
            cost=cost,
            execution_time=execution_time,
            actual_time=actual_time,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            provider=self.provider
        )

        log_response(self.logger, "SUCCESS", response)

        return response


#-----------------------------------------FIREWORKS AI-----------------------------------------#
@EngineFactory.register_engine('fireworks')
class FireworksEngine(TextEngine):
    def __init__(self,
                model: str,
                provider: str = "fireworks",
                temperature: Optional[float] = ModelConfig.DEFAULT_TEMPERATURE,
                max_tokens: Optional[int] = ModelConfig.DEFAULT_MAX_TOKENS,
                top_p: Optional[float] = ModelConfig.DEFAULT_TOP_P,
                stop: Union[str, List[str], None] = ModelConfig.DEFAULT_STOP,
                messages: Optional[List[Dict[str, str]]] = ModelConfig.MESSAGES_EXAMPLE
                ) -> None:
        super().__init__(model, provider, temperature, max_tokens, top_p, stop, messages)

        self._api_key = self._keys.get_api_keys("FIREWORKS_API_KEY")
        if self._api_key is None:
            self.logger.error(f"API key not found for {self.provider}")
            raise ValueError(f"API key not found for {self.provider}")
        
        # Set up the client
        self._set_up_client()

        self._api_name = dataEngine.getAPIname(self.model, self.provider)


    def _set_up_client(self):
        self.client = openai.OpenAI(base_url="https://api.fireworks.ai/inference/v1",
                                    api_key = self._api_key)


    def generate_response(self,
                        **kwargs: Any
                        ) -> Union[str, None]:
        """
        This method is used to generate a response from the AI model.

        """

        start_time = time.time()

        try:
            completion = self.client.chat.completions.create(
                messages=self.messages,
                model=f"accounts/fireworks/models/{self._api_name}",
                temperature=self.temperature,
                max_tokens=self.max_tokens,
                top_p=self.top_p,
                stop=self.stop
            )
        except Exception as e:
            print(f"Error generating response: {e}")
            self.logger.error(f"Error generating response of provider {self.provider}: {e}")
            return None

        actual_time = time.time() - start_time

        content = completion.choices[0].message.content
        input_tokens = completion.usage.prompt_tokens
        output_tokens = completion.usage.completion_tokens
        execution_time = None
        cost = dataEngine.calculate_cost(self.provider, self.model, input_tokens, output_tokens)

        response = TextResponse(
            content=content,
            cost=cost,
            execution_time=execution_time,
            actual_time=actual_time,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            provider=self.provider
        )

        log_response(self.logger, "SUCCESS", response)

        return response


#-----------------------------------------Replicate-----------------------------------------#
@EngineFactory.register_engine('replicate')
class ReplicateEngine(TextEngine):
    def __init__(self,
                model: str,
                provider: str = "replicate",
                temperature: Optional[float] = ModelConfig.DEFAULT_TEMPERATURE,
                max_tokens: Optional[int] = ModelConfig.DEFAULT_MAX_TOKENS,
                top_p: Optional[float] = ModelConfig.DEFAULT_TOP_P,
                stop: Union[str, List[str], None] = ModelConfig.DEFAULT_STOP,
                messages: Optional[List[Dict[str, str]]] = ModelConfig.MESSAGES_EXAMPLE
                ) -> None:
        super().__init__(model, provider, temperature, max_tokens, top_p, stop, messages)

        self._api_key = self._keys.get_api_keys("REPLICATE_API_KEY")
        if self._api_key is None:
            self.logger.error(f"API key not found for {self.provider}")
            raise ValueError(f"API key not found for {self.provider}")
        
        # Set up the client
        self._set_up_client()

        self._api_name = dataEngine.getAPIname(self.model, self.provider)


    def _set_up_client(self):
        self.client = replicate.Client(api_token=self._api_key)

    
    def _construct_replicate_messages(self):
        system_prompt = None
        prompt = ""
        for message in self.messages:
            if message["role"] == "system":
                system_prompt = message["content"]
            else:
                prompt += message["content"] + "\n"

        return system_prompt, prompt


    def generate_response(self,
                        **kwargs: Any
                        ) -> Union[str, None]:
        """
        This method is used to generate a response from the AI model.

        """
        system_prompt, prompt = self._construct_replicate_messages()

        start_time = time.time()

        try:
            completion = self.client.run(
                self._api_name,
                input = {
                    "prompt": prompt,
                    "system_prompt": system_prompt,
                    "temperature": self.temperature,
                    "max_new_tokens": self.max_tokens,
                    "top_p": self.top_p,
                    "stop_sequences": self.stop if self.stop else ""
                }
            )
        except Exception as e:
            print(f"Error generating response: {e}")
            self.logger.error(f"Error generating response of provider {self.provider}: {e}")
            return None

        actual_time = time.time() - start_time
        content = "".join(completion)
        input_tokens = None
        output_tokens = None
        execution_time = None
        cost = None

        response = TextResponse(
            content=content,
            cost=cost,
            execution_time=execution_time,
            actual_time=actual_time,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            provider=self.provider
        )

        log_response(self.logger, "SUCCESS", response)

        return response


#-----------------------------------------Deepinfra-----------------------------------------#
@EngineFactory.register_engine('deepinfra')
class DeepinfraEngine(TextEngine):
    def __init__(self,
                model: str,
                provider: str = "deepinfra",
                temperature: Optional[float] = ModelConfig.DEFAULT_TEMPERATURE,
                max_tokens: Optional[int] = ModelConfig.DEFAULT_MAX_TOKENS,
                top_p: Optional[float] = ModelConfig.DEFAULT_TOP_P,
                stop: Union[str, List[str], None] = ModelConfig.DEFAULT_STOP,
                messages: Optional[List[Dict[str, str]]] = ModelConfig.MESSAGES_EXAMPLE
                ) -> None:
        super().__init__(model, provider, temperature, max_tokens, top_p, stop, messages)

        self._api_key = self._keys.get_api_keys("DEEPINFRA_API_KEY")
        if self._api_key is None:
            self.logger.error(f"API key not found for {self.provider}")
            raise ValueError(f"API key not found for {self.provider}")
        
        # Set up the client
        self._set_up_client()

        self._api_name = dataEngine.getAPIname(self.model, self.provider)


    def _set_up_client(self):
        self.client = openai.OpenAI(base_url="https://api.deepinfra.com/v1/openai",
                                    api_key = self._api_key)


    def generate_response(self,
                        **kwargs: Any
                        ) -> Union[str, None]:
        """
        This method is used to generate a response from the AI model.

        """

        start_time = time.time()

        try:
            completion = self.client.chat.completions.create(
                messages=self.messages,
                model=self._api_name,
                temperature=self.temperature,
                max_tokens=self.max_tokens,
                top_p=self.top_p,
                stop=self.stop
            )
        except Exception as e:
            print(f"Error generating response: {e}")
            self.logger.error(f"Error generating response of provider {self.provider}: {e}")
            return None

        actual_time = time.time() - start_time

        content = completion.choices[0].message.content
        input_tokens = completion.usage.prompt_tokens
        output_tokens = completion.usage.completion_tokens
        execution_time = None
        cost = dataEngine.calculate_cost(self.provider, self.model, input_tokens, output_tokens)

        response = TextResponse(
            content=content,
            cost=cost,
            execution_time=execution_time,
            actual_time=actual_time,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            provider=self.provider
        )

        log_response(self.logger, "SUCCESS", response)

        return response


#-----------------------------------------Lepton-----------------------------------------#
@EngineFactory.register_engine('lepton')
class LeptonEngine(TextEngine):
    def __init__(self,
                model: str,
                provider: str = "lepton",
                temperature: Optional[float] = ModelConfig.DEFAULT_TEMPERATURE,
                max_tokens: Optional[int] = ModelConfig.DEFAULT_MAX_TOKENS,
                top_p: Optional[float] = ModelConfig.DEFAULT_TOP_P,
                stop: Union[str, List[str], None] = ModelConfig.DEFAULT_STOP,
                messages: Optional[List[Dict[str, str]]] = ModelConfig.MESSAGES_EXAMPLE
                ) -> None:
        super().__init__(model, provider, temperature, max_tokens, top_p, stop, messages)

        self._api_key = self._keys.get_api_keys("LEPTON_API_KEY")
        if self._api_key is None:
            self.logger.error(f"API key not found for {self.provider}")
            raise ValueError(f"API key not found for {self.provider}")
        
        self._api_name = dataEngine.getAPIname(self.model, self.provider)

        # Set up the client
        self._set_up_client()


    def _set_up_client(self):
        self.client = openai.OpenAI(base_url=f"https://{self._api_name}.lepton.run/api/v1/",
                                    api_key = self._api_key)


    def generate_response(self,
                        **kwargs: Any
                        ) -> Union[str, None]:
        """
        This method is used to generate a response from the AI model.

        """

        start_time = time.time()

        try:
            completion = self.client.chat.completions.create(
                messages=self.messages,
                model=self._api_name,
                temperature=self.temperature,
                max_tokens=self.max_tokens,
                top_p=self.top_p,
                stop=self.stop
            )
        except Exception as e:
            print(f"Error generating response: {e}")
            self.logger.error(f"Error generating response of provider {self.provider}: {e}")
            return None

        actual_time = time.time() - start_time

        content = completion.choices[0].message.content
        input_tokens = completion.usage.prompt_tokens
        output_tokens = completion.usage.completion_tokens
        execution_time = None
        cost = dataEngine.calculate_cost(self.provider, self.model, input_tokens, output_tokens)

        response = TextResponse(
            content=content,
            cost=cost,
            execution_time=execution_time,
            actual_time=actual_time,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            provider=self.provider
        )

        log_response(self.logger, "SUCCESS", response)

        return response


#-----------------------------------------OpenAI-----------------------------------------#
@EngineFactory.register_engine('openai')
class OpenaiEngine(TextEngine):
    def __init__(self,
                model: str,
                provider: str = "openai",
                temperature: Optional[float] = ModelConfig.DEFAULT_TEMPERATURE,
                max_tokens: Optional[int] = ModelConfig.DEFAULT_MAX_TOKENS,
                top_p: Optional[float] = ModelConfig.DEFAULT_TOP_P,
                stop: Union[str, List[str], None] = ModelConfig.DEFAULT_STOP,
                messages: Optional[List[Dict[str, str]]] = ModelConfig.MESSAGES_EXAMPLE
                ) -> None:
        super().__init__(model, provider, temperature, max_tokens, top_p, stop, messages)

        self._api_key = self._keys.get_api_keys("OPENAI_API_KEY")
        if self._api_key is None:
            self.logger.error(f"API key not found for {self.provider}")
            raise ValueError(f"API key not found for {self.provider}")
        
        # Set up the client
        self._set_up_client()

        self._api_name = dataEngine.getAPIname(self.model, self.provider)


    def _set_up_client(self):
        self.client = openai.OpenAI(api_key = self._api_key)


    def generate_response(self,
                        **kwargs: Any
                        ) -> Union[str, None]:
        """
        This method is used to generate a response from the AI model.

        """

        start_time = time.time()

        try:
            completion = self.client.chat.completions.create(
                messages=self.messages,
                model=self._api_name,
                temperature=self.temperature,
                max_tokens=self.max_tokens,
                top_p=self.top_p,
                stop=self.stop
            )
        except Exception as e:
            print(f"Error generating response: {e}")
            self.logger.error(f"Error generating response of provider {self.provider}: {e}")
            return None

        actual_time = time.time() - start_time

        content = completion.choices[0].message.content
        input_tokens = completion.usage.prompt_tokens
        output_tokens = completion.usage.completion_tokens
        execution_time = None
        cost = dataEngine.calculate_cost(self.provider, self.model, input_tokens, output_tokens)

        response = TextResponse(
            content=content,
            cost=cost,
            execution_time=execution_time,
            actual_time=actual_time,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            provider=self.provider
        )

        log_response(self.logger, "SUCCESS", response)

        return response


#-----------------------------------------Anthropic-----------------------------------------#
@EngineFactory.register_engine('anthropic')
class AnthropicEngine(TextEngine):
    def __init__(self,
                model: str,
                provider: str = "anthropic",
                temperature: Optional[float] = ModelConfig.DEFAULT_TEMPERATURE,
                max_tokens: Optional[int] = ModelConfig.DEFAULT_MAX_TOKENS,
                top_p: Optional[float] = ModelConfig.DEFAULT_TOP_P,
                stop: Union[str, List[str], None] = ModelConfig.DEFAULT_STOP,
                messages: Optional[List[Dict[str, str]]] = ModelConfig.MESSAGES_EXAMPLE
                ) -> None:
        super().__init__(model, provider, temperature, max_tokens, top_p, stop, messages)

        self._api_key = self._keys.get_api_keys("ANTHROPIC_API_KEY")
        if self._api_key is None:
            self.logger.error(f"API key not found for {self.provider}")
            raise ValueError(f"API key not found for {self.provider}")
        
        # Set up the client
        self._set_up_client()

        self._api_name = dataEngine.getAPIname(self.model, self.provider)


    def _set_up_client(self):
        self.client = anthropic.Client(api_key=self._api_key)


    def construct_messages(self):
        system_prompt = None
        new_messages = []
        for message in self.messages:
            if message["role"] == "system":
                system_prompt = message["content"]
            else:
                new_messages.append(message)

        return system_prompt, new_messages

    def generate_response(self,
                        **kwargs: Any
                        ) -> Union[str, None]:
        """
        This method is used to generate a response from the AI model.

        """
        system_prompt, messages = self.construct_messages()

        start_time = time.time()

        try:
            completion = self.client.messages.create(
                system=system_prompt,
                messages=messages,
                model=self._api_name,
                temperature=self.temperature,
                max_tokens=self.max_tokens,
                top_p=self.top_p,
                stop_sequences=self.stop
            )
        except Exception as e:
            print(f"Error generating response: {e}")
            self.logger.error(f"Error generating response of provider {self.provider}: {e}")
            return None

        actual_time = time.time() - start_time

        content = completion.content[0].text
        input_tokens = completion.usage.input_tokens
        output_tokens = completion.usage.output_tokens
        execution_time = None
        cost = dataEngine.calculate_cost(self.provider, self.model, input_tokens, output_tokens)

        response = TextResponse(
            content=content,
            cost=cost,
            execution_time=execution_time,
            actual_time=actual_time,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            provider=self.provider
        )

        log_response(self.logger, "SUCCESS", response)

        return response


#-----------------------------------------Mistral AI-----------------------------------------#
@EngineFactory.register_engine('mistral')
class MistralEngine(TextEngine):
    def __init__(self,
                model: str,
                provider: str = "mistral",
                temperature: Optional[float] = ModelConfig.DEFAULT_TEMPERATURE,
                max_tokens: Optional[int] = ModelConfig.DEFAULT_MAX_TOKENS,
                top_p: Optional[float] = ModelConfig.DEFAULT_TOP_P,
                stop: Union[str, List[str], None] = ModelConfig.DEFAULT_STOP,
                messages: Optional[List[Dict[str, str]]] = ModelConfig.MESSAGES_EXAMPLE
                ) -> None:
        super().__init__(model, provider, temperature, max_tokens, top_p, stop, messages)

        self._api_key = self._keys.get_api_keys("MISTRAL_API_KEY")
        if self._api_key is None:
            self.logger.error(f"API key not found for {self.provider}")
            raise ValueError(f"API key not found for {self.provider}")
        
        # Set up the client
        self._set_up_client()

        self._api_name = dataEngine.getAPIname(self.model, self.provider)


    def _set_up_client(self):
        self.client = MistralClient(api_key=self._api_key)


    def generate_response(self,
                        **kwargs: Any
                        ) -> Union[str, None]:
        """
        This method is used to generate a response from the AI model.

        """
        start_time = time.time()

        try:
            completion = self.client.chat(
                messages=self.messages,
                model=self._api_name,
                temperature=self.temperature,
                max_tokens=self.max_tokens,
                top_p=self.top_p,
            )
        except Exception as e:
            print(f"Error generating response: {e}")
            self.logger.error(f"Error generating response of provider {self.provider}: {e}")
            return None

        actual_time = time.time() - start_time

        content = completion.choices[0].message.content
        input_tokens = completion.usage.prompt_tokens
        output_tokens = completion.usage.completion_tokens
        execution_time = None
        cost = dataEngine.calculate_cost(self.provider, self.model, input_tokens, output_tokens)

        response = TextResponse(
            content=content,
            cost=cost,
            execution_time=execution_time,
            actual_time=actual_time,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            provider=self.provider
        )

        log_response(self.logger, "SUCCESS", response)

        return response


#-----------------------------------------Gooole Gemini AI-----------------------------------------#
@EngineFactory.register_engine('google')
class GoogleEngine(TextEngine):
    def __init__(self,
                model: str,
                provider: str = "google",
                temperature: Optional[float] = ModelConfig.DEFAULT_TEMPERATURE,
                max_tokens: Optional[int] = ModelConfig.DEFAULT_MAX_TOKENS,
                top_p: Optional[float] = ModelConfig.DEFAULT_TOP_P,
                stop: Union[str, List[str], None] = ModelConfig.DEFAULT_STOP,
                messages: Optional[List[Dict[str, str]]] = ModelConfig.MESSAGES_EXAMPLE
                ) -> None:
        super().__init__(model, provider, temperature, max_tokens, top_p, stop, messages)

        self._api_key = self._keys.get_api_keys("GOOGLE_API_KEY")
        if self._api_key is None:
            self.logger.error(f"API key not found for {self.provider}")
            raise ValueError(f"API key not found for {self.provider}")
        
        # Set up the client
        self._set_up_client()

        self._api_name = dataEngine.getAPIname(self.model, self.provider)

        self.generation_config = {
            "temperature": self.temperature,
            "top_p": self.top_p,
            "max_output_tokens": self.max_tokens,
        }

        self.safety_settings = [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_ONLY_HIGH"
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_ONLY_HIGH"
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_ONLY_HIGH"
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_ONLY_HIGH"
        }
        ]


    def _set_up_client(self):
        genai.configure(api_key=self._api_key)


    def construct_prompt_parts(self):
        prompt_parts = []
        for message in self.messages:
            if message["role"] == "system":
                prompt_parts.append(f"{message['content']}")
            elif message["role"] == "user":
                prompt_parts.append(f"Input: {message['content']}")
            else:
                prompt_parts.append(f"Output: {message['content']}")

        return prompt_parts


    def generate_response(self,
                        **kwargs: Any
                        ) -> Union[str, None]:
        """
        This method is used to generate a response from the AI model.

        """
        start_time = time.time()

        model = genai.GenerativeModel(model_name = self._api_name,
                                    generation_config = self.generation_config,
                                    safety_settings = self.safety_settings)
        
        prompt_parts = self.construct_prompt_parts()

        try:
            completion = model.generate_content(prompt_parts)
        except Exception as e:
            print(f"Error generating response: {e}")
            self.logger.error(f"Error generating response of provider {self.provider}: {e}")
            return None

        actual_time = time.time() - start_time

        content = completion.text
        input_tokens = None
        output_tokens = None
        execution_time = None
        cost = 0

        response = TextResponse(
            content=content,
            cost=cost,
            execution_time=execution_time,
            actual_time=actual_time,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            provider=self.provider
        )

        log_response(self.logger, "SUCCESS", response)

        return response

