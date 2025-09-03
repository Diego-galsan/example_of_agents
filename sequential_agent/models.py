import os
from google.adk.models.lite_llm import LiteLlm


def sub_model():
    model = LiteLlm(
        model = "openrouter/google/gemini-2.5-pro",
        api_key = os.getenv("OPENROUTER_API_KEY"),
        temperature = 0.0
    )
    return model

def model():
    model = LiteLlm(
        model = "openrouter/google/gemini-2.5-pro",
        api_key = os.getenv("OPENROUTER_API_KEY"),
        temperature = 0.0
    )
    return model
