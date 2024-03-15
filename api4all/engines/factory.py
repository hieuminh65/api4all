from ..data.data import dataEngine

class EngineFactory:
    _engines = {}

    @classmethod
    def register_engine(cls, provider):
        def decorator(engine_cls):
            cls._engines[provider] = engine_cls
            return engine_cls
        return decorator

    @classmethod
    def create_engine(cls, provider, **kwargs):
        if (provider is None) or (provider not in dataEngine.providers):
            raise ValueError(f"Please select a provider from {dataEngine.providers}")
        engine_cls = cls._engines.get(provider)
        if engine_cls:
            return engine_cls(**kwargs)
        else:
            raise ValueError(f"No engine registered for provider: {provider}")
