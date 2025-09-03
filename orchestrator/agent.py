
import random
from google.adk.agents import Agent, LlmAgent
from .models import  model, sub_model # <--- Corrected import
from .tools import search, crear_archivo_py, run_code


model = model()
sub_model = sub_model()  # Assuming sub_model is a method of the model class

researcher = LlmAgent(
    name="researcher",
    model=sub_model,
    description="Agente con herramientas para buscar en internet",
    instruction="""Eres un agente investigador. Tu objetivo es investigar a fondo en internet para encontrar información sobre cualquier tema dado.
""",
    tools=[search],
)


programer = LlmAgent(
    name="programer",
    model=sub_model,
    description="Agente con herramientas para programar",
    instruction="""Eres un agente programador. Tu objetivo es ayudar a programar y resolver problemas de codificación.
Puedes ejecutar código Python usando la herramienta run_code.
""",
    tools=[run_code],
)

register = LlmAgent(
    name="register",
    model=sub_model,
    description="Agente con herramientas para registrar información.",
    instruction="""Eres un agente registrador. Tu objetivo es ayudar a registrar y organizar información.
""",
    tools = [crear_archivo_py],
)

def orchestrator() -> LlmAgent:
    return LlmAgent(
        name="orchestrator",
        model=model,
        description="Orchestrator that delegates tasks to sub-agents.",
        instruction="""You are an orchestrator. Your primary goal is to delegate tasks to your sub-agents.

You have the following sub-agents available:
- 'researcher': Expert at searching the internet using the 'search' tool
- 'programer': Expert at programming and can execute Python code using the 'run_code' tool
- 'register': Expert at registering and organizing information using the 'crear_archivo_py' tool

Based on the user's request, you MUST delegate the appropriate task to the relevant agent:
- For information searches, delegate to 'researcher'
- For programming tasks or code execution, delegate to 'programer'  
- For file creation or organization, delegate to 'register'

Construct clear instructions for the chosen agent to perform the task.
Do not try to answer directly or use any tools yourself. Your job is to delegate.
""",
        tools=[],
        sub_agents=[
            researcher,
            programer,
            register,
        ],
    )

root_agent = orchestrator() #Comment this line for a2a
