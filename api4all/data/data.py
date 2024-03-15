from typing import Optional, List, Dict, Union, Any
from .constant_data import data


class DataFactory:
    """
    The class is used to store and retrieve data about the AI models.
    """

    def __init__(self, data: dict):
        """
        Initialize the DataFactory with a dictionary of data.
        """
        self.data = data
    
    @property
    def models(self):
        """
        Return a list of all model names in the data.
        """
        return list(self.data.keys())

    @property
    def providers(self):
        """
        Return a set of all provider names in the data.
        """
        providers = set()
        for model in self.data.values():
            for provider in model["provider"].keys():
                providers.add(provider)
        return providers
    
    def isProviderHasModel(self, model: str, provider: str = None):
        """
        Check if a given provider has a given model. If provider is not provided, 
        check if the model exists in the data.
        """
        if not isinstance(model, str) or not model:
            raise ValueError("Model must be a non-empty string. All models are: " + ", ".join(self.models))
        if provider is not None and (not isinstance(provider, str) or not provider):
            raise ValueError("provider must be a non-empty string. All providers are: " + ", ".join(self.providers))

        return provider in self.data[model]["provider"]
    
    def getProvidersForModel(self, model):
        """
        Return a list of all providers for a given model.
        """
        if model not in self.models:
            raise ValueError("Model must be one of the following: " + ", ".join(self.models))
        return list(self.data[model]["provider"].keys())
    
    def getAPIname(self, model, provider):
        """
        Return the API name for a given model and provider.
        """
        return self.data[model]["provider"][provider]["name"]

    def getPrice(self, model, provider):
        """
        Return the price information for a given model and provider.
        """
        if model not in self.models:
            raise ValueError("Model must be one of the following: " + ", ".join(self.models))
        if not self.isProviderHasModel(model, provider):
            raise ValueError(f"{provider} does not support the {model} model. Please select a provider from {self.getProvidersForModel(model)}")
        return self.data[model]["provider"][provider]["price"]
    
    def getContextLength(self, model):
        """
        Return the context length for a given model.
        """
        return self.data[model]["context-length"]
    
    def calculate_cost(self, 
                provider: str, 
                model: str, 
                input_tokens: int,
                output_tokens: int
                ) -> float:
        """
        Calculate the cost of using a given model from a given provider with a given number of input and output tokens.
        """
        input_cost = self.data[model]["provider"][provider]["price"]["input"]
        output_cost = self.data[model]["provider"][provider]["price"]["output"]
        return (input_cost * input_tokens / 1000000) + (output_cost * output_tokens / 1000000)

dataEngine = DataFactory(data)