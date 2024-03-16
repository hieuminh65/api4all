data = {
    "openai/gpt-3.5-turbo-0125": {
        "provider": {
            "openai": {
                "name": "gpt-3.5-turbo-0125",
                "price": {
                    "input": 0.5,
                    "output": 1.5
                }
            }
        },
        "context-length": 16385
    },
    "openai/gpt-3.5-turbo": {
        "provider": {
            "openai": {
                "name": "gpt-3.5-turbo",
                "price": {
                    "input": 0.5,
                    "output": 1.5
                }
            }
        },
        "context-length": 16385
    },
    "openai/gpt-4": {
        "provider": {
            "openai": {
                "name": "gpt-4",
                "price": {
                    "input": 30,
                    "output": 60
                }
            }
        },
        "context-length": 8192
    },
    "openai/gpt-4-32k": {
        "provider": {
            "openai": {
                "name": "gpt-4-32k",
                "price": {
                    "input": 60,
                    "output": 120
                }
            }
        },
        "context-length": 32768
    },
    "mistralai/Mixtral-8x7B-Instruct-v0.1": {
        "provider": {
            "groq": {
                "name": "mixtral-8x7b-32768",
                "price": {
                    "input": 0,
                    "output": 0
                }
            },
            "anyscale": {
                "name": "mistralai/Mixtral-8x7B-Instruct-v0.1",
                "price": {
                    "input": 0.5,
                    "output": 0.5
                }
            },
            "fireworks": {
                "name": "mixtral-8x7b-instruct",
                "price": {
                    "input": 0.5,
                    "output": 0.5
                }
            },
            "replicate": {
                "name": "mistralai/mixtral-8x7b-instruct-v0.1",
                "price": {
                    "input": 0.3,
                    "output": 1
                }
            },
            "together": {
                "name": "mistralai/Mixtral-8x7b-Instruct-v0.1",
                "price": {
                    "input": 0.6,
                    "output": 0.6
                }
            },
            "deepinfra": {
                "name": "mistralai/Mixtral-8x7B-Instruct-v0.1",
                "price": {
                    "input": 0.27,
                    "output": 0.27
                }
            },
            "mistral": {
                "name": "open-mistral-7b",
                "price": {
                    "input": 0.7,
                    "output": 0.7
                }
            }
        },
        "context-length": 32768
    },
    "google/gemma-7b-it": {
        "provider": {
            "groq": {
                "name": "gemma-7b-it",
                "price": {
                    "input": 0,
                    "output": 0
                }
            },
            "anyscale": {
                "name": "google/gemma-7b-it",
                "price": {
                    "input": 0.15,
                    "output": 0.15
                }
            },
            "together": {
                "name": "google/gemma-7b-it",
                "price": {
                    "input": 0.2,
                    "output": 0.2
                }
            },
            "replicate": {
                "name": "google-deepmind/gemma-7b-it:2790a695e5dcae15506138cc4718d1106d0d475e6dca4b1d43f42414647993d5",
                "price": {
                    "input": 0.05,
                    "output": 0.25
                }
            },
            "fireworks": {
                "name": "gemma-7b-it",
                "price": {
                    "input": 0.2,
                    "output": 0.2
                }
            },
            "deepinfra": {
                "name": "google/gemma-7b-it",
                "price": {
                    "input": 0.13,
                    "output": 0.13
                }
            }
        },
        "context-length": 8192
    },
    "mistral/open-mistral-7b": {
        "provider": {
            "mistral": {
                "name": "open-mistral-7b",
                "price": {
                    "input": 0.25,
                    "output": 0.25
                }
            }
        },
        "context-length": 8192
    },
    "mistral/open-mixtral-8x7b": {
        "provider": {
            "mistral": {
                "name": "open-mixtral-8x7b",
                "price": {
                    "input": 0.7,
                    "output": 0.7
                }
            }
        },
        "context-length": 32768
    },
    "mistral/mistral-small-latest": {
        "provider": {
            "mistral": {
                "name": "mistral-small-latest",
                "price": {
                    "input": 2,
                    "output": 6
                }
            }
        },
        "context-length": 32768
    },
    "mistral/mistral-medium-latest": {
        "provider": {
            "mistral": {
                "name": "mistral-medium-latest",
                "price": {
                    "input": 2.7,
                    "output": 8.1
                }
            }
        },
        "context-length": 32768
    },
    "mistral/mistral-large-latest": {
        "provider": {
            "mistral": {
                "name": "mistral-large-latest",
                "price": {
                    "input": 8,
                    "output": 24
                }
            }
        },
        "context-length": 32768
    },
    "anthropic/claude-3-opus": {
        "provider": {
            "anthropic": {
                "name": "claude-3-opus-20240229",
                "price": {
                    "input": 15,
                    "output": 75
                }
            }
        },
        "context-length": 200000
    },
    "anthropic/claude-3-sonnet": {
        "provider": {
            "anthropic": {
                "name": "claude-3-sonnet-20240229",
                "price": {
                    "input": 3,
                    "output": 15
                }
            }
        },
        "context-length": 200000
    },
    "anthropic/claude-3-haiku": {
        "provider": {
            "anthropic": {
                "name": "claude-3-haiku-20240307",
                "price": {
                    "input": 0.25,
                    "output": 1.25
                }
            }
        },
        "context-length": 200000
    },
    "anthropic/claude-2.1": {
        "provider": {
            "anthropic": {
                "name": "claude-2.1",
                "price": {
                    "input": 8,
                    "output": 24
                }
            }
        },
        "context-length": 200000
    },
    "anthropic/claude-2.0": {
        "provider": {
            "anthropic": {
                "name": "claude-2.0",
                "price": {
                    "input": 8,
                    "output": 24
                }
            }
        },
        "context-length": 100000
    },
    "anthropic/claude-instant-1.2": {
        "provider": {
            "anthropic": {
                "name": "claude-instant-1.2",
                "price": {
                    "input": 0.8,
                    "output": 2.4
                }
            }
        },
        "context-length": 100000
    },
    "meta/Llama-2-70b-chat-hf": {
        "provider": {
            "anyscale": {
                "name": "meta-llama/Llama-2-70b-chat-hf",
                "price": {
                    "input": 1,
                    "output": 1
                }
            },
            "groq": {
                "name": "llama2-70b-4096",
                "price": {
                    "input": 0,
                    "output": 0
                }
            },
            "together": {
                "name": "meta-llama/Llama-2-70b-chat-hf",
                "price": {
                    "input": 0.9,
                    "output": 0.9
                }
            },
            "replicate": {
                "name": "meta/llama-2-70b-chat",
                "price": {
                    "input": 0.65,
                    "output": 2.75
                }
            },
            "fireworks": {
                "name": "llama-v2-70b-chat",
                "price": {
                    "input": 0.9,
                    "output": 0.9
                }
            },
            "deepinfra": {
                "name": "meta-llama/Llama-2-70b-chat-hf",
                "price": {
                    "input": 0.7,
                    "output": 0.9
                }
            }
        },
        "context-length": 4096
    },
    "google/gemini-1.0-pro": {
        "provider": {
            "google": {
                "name": "gemini-1.0-pro",
                "price": {
                    "input": 0,
                    "output": 0
                }
            }
        },
        "context-length": 32768
    },
}