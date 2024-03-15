# api4all
Easy-to-use LLM API from a state-of-the-art provider and comparison.

## Installation
1. Install the package
```bash
pip3 install api4all
```

2. Create and activate a virtual environment (optional but recommended)
- Unix / macOS
```bash
python3 -m venv venv
source venv/bin/activate
```
- Windows
```bash
python3 -m venv venv
.\venv\Scripts\activate
```

## Quick Start
1. Wrap the API key in a `.env` file of the provider you want to test.
```bash
TOGETHER_API_KEY=xxx
OPENAI_API_KEY=xxx
MISTRAL_API_KEY=xxx
ANTHROPIC_API_KEY=xxx
```

2. Run the code
```python
from api4all import EngineFactory

messages = [
    {"role": "system",
    "content": "You are a helpful assistent for the my Calculus class."},
    {"role": "user",
    "content": "What is the current status of the economy?"}
]


engine = EngineFactory.create_engine(provider="together", 
                                    model="google/gemma-7b-it", 
                                    messages=messages, 
                                    temperature=0.5, 
                                    max_tokens=256, 
                                    )

response = engine.generate_response()

print(response)
```

3. Check the [log file](logfile.log) for the response and the cost of the request.
```bash
Request ID - fa8cebd0-265a-44b2-95d7-6ff1588d2c87
	create at: 2024-03-15 16:38:18,129
	INFO - SUCCESS
	
    Response:
		I am not able to provide information about the current status of the economy, as I do not have access to real-time information. Therefore, I recommend checking a reliable source for the latest economic news and data.
	
    Cost: $0.0000154    # Cost of this provider for this request
	Provider: together  # Provider used for this request
	Execution-time: Execution time not provided by the provider
	Actual-time: 0.9448428153991699 # Actual time taken by the request
	Input-token: 33     # Number of tokens used for the input
	Output-token: 44    # Number of tokens used for the output
```

## Providers and Pricing

### Providers

Provider | Free Credit | Rate Limit | API Key name | Provider string name |
|:------:|:------:|:------:|:------:|:------:|
|  [Groq](https://wow.groq.com)          |     Unlimited | 30 Requests / Minute  | GROQ_API_KEY | "groq"  |
|  [Anyscale](https://www.anyscale.com)  |     $10      | 30 Requests / Second  |  ANYSCALE_API_KEY | "anyscale"  |
|  [Together AI](https://www.together.ai)|     $25      | 1 Requests / Second  | TOGETHER_API_KEY | "together"  | 
|  [Replicate](https://replicate.com)    |     Free to try  | 50 Requests / Second    | REPLICATE_API_KEY | "replicate"  |
|  [Fireworks](https://fireworks.ai)     |     $1      | 600 Requests / Minute  |  FIREWORKS_API_KEY | "fireworks"  |  
|  [Deepinfra](https://deepinfra.com)    |     Free to try     | 200 Concurrent request |  DEEPINFRA_API_KEY | "deepinfra"  |
|  [Google AI (Vertex AI)](https://ai.google.dev)    |     Unlimited     | 60 Requests / Minute | GOOGLE_API_KEY | "google"  |
|  [OpenAI](http://openai.com)    |     &#x2715;     | 60 Requests / Minute | OPENAI_API_KEY | "openai"  |
|  [Mistral AI](https://mistral.ai)    |     Free to try     | 5 Requests / Second | MISTRAL_API_KEY | "mistral"  |
|  [Anthropic](https://www.anthropic.com)    |     Free to try     | 5 Requests / Minute | ANTHROPIC_API_KEY | "anthropic"  |


- **Free to try**: Free to try, no credit card required but limited to a certain number of tokens.

### Open-source models
<details>
<summary><b>1. Mixtral-8x7b-Instruct-v0.1</b></summary>

Mixtral 8x7B is a high-performing sparse mixture of experts model (SMoE) with open weights, licensed under Apache 2.0. It surpasses Llama 2 70B in most benchmarks, offering 6x faster inference. It's the best open-weight model considering cost/performance trade-offs, matching or exceeding GPT3.5 on most standard benchmarks.
<br>
- Developer: Mistral AI
- Context Length: 32,768

Provider | Input Pricing ($/1M Tokens) | Output Pricing ($/1M Tokens) |
|:------:|:------:|:------:|
|  [Groq](https://wow.groq.com)          |     $0        | $0    | 
|  [Anyscale](https://www.anyscale.com)  |     $0.5      | $0.5  | 
|  [Together AI](https://www.together.ai)|     $0.6      | $0.6  | 
|  [Replicate](https://replicate.com)    |     $0.3      | $1    |  
|  [Fireworks](https://fireworks.ai)     |     $0.5      | $0.5  |  
|  [Deepinfra](https://deepinfra.com)    |     $0.27     | $0.27 |   

</details>

<details>
<summary><b>2. Gemma 7B it</b></summary>

- Developer: Google AI
- Context Length: 8,192


Provider | Input Pricing ($/1M Tokens) | Output Pricing ($/1M Tokens) |
|:------:|:------:|:------:|
|  [Groq](https://wow.groq.com)          |     $0        | $0    | 
|  [Anyscale](https://www.anyscale.com)  |     $0.15      | $0.15  | 
|  [Together AI](https://www.together.ai)|     $0.2      | $0.2  | 
|  [Replicate](https://replicate.com)    |     &#x2715;      | &#x2715;    |  
|  [Fireworks](https://fireworks.ai)     |     $0.2      | $0.2  |  
|  [Deepinfra](https://deepinfra.com)    |     &#x2715;     | &#x2715; |   

</details>


<details>
<summary><b>3. LLaMA2-70b</b></summary>

- Developer: Meta AI
- Context Length: 4,096


Provider | Input Pricing ($/1M Tokens) | Output Pricing ($/1M Tokens) |
|:------:|:------:|:------:|
|  [Groq](https://wow.groq.com)          |     $0        | $0         | 
|  [Anyscale](https://www.anyscale.com)  |     $1.0      | $1.0       | 
|  [Together AI](https://www.together.ai)|     $0.9      | $0.9       | 
|  [Replicate](https://replicate.com)    |     $0.65     | $2.75      |  
|  [Fireworks](https://fireworks.ai)     |     $0.9      | $0.9       |  
|  [Deepinfra](https://deepinfra.com)    |     $0.7      | $0.9       |   

</details>


<details>
<summary><b>4. Mistral-7B-Instruct-v0.1</b></summary>

- Developer: Mistral AI
- Context Length: 4,096


Provider | Input Pricing ($/1M Tokens) | Output Pricing ($/1M Tokens) |
|:------:|:------:|:------:|
|  [Groq](https://wow.groq.com)          |     &#x2715;    | &#x2715;    | 
|  [Anyscale](https://www.anyscale.com)  |     $0.15       | $0.15       | 
|  [Together AI](https://www.together.ai)|     $0.2        | $0.2        | 
|  [Replicate](https://replicate.com)    |     $0.05       | $0.25       |  
|  [Fireworks](https://fireworks.ai)     |     $0.2        | $0.2        |  
|  [Deepinfra](https://deepinfra.com)    |     &#x2715;    | &#x2715;    |   

</details>