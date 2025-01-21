from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv
import os

load_dotenv()

def response_req(text: str) -> str:
    endpoint = "https://models.inference.ai.azure.com"
    model_name = os.getenv("MODEL_NAME")
    token = os.getenv("GITHUB_KEY")

    client = ChatCompletionsClient(endpoint=endpoint, credential=AzureKeyCredential(token),)
    response = client.complete(
        messages=[
        SystemMessage(content="You are a helpful multilanguage assistant bot in Discord, your response length limit is 4000 chars because of discord limitations"),
        UserMessage(content=text),
        ],
        model=model_name,
        temperature=1.0,
        max_tokens=1000,
        top_p=1.0
    )
    
    module_response = response.choices[0].message.content
    return module_response