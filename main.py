from huggingface_hub import login
from smolagents import CodeAgent, DuckDuckGoSearchTool, tool, InferenceClientModel, LiteLLMModel
HF_TOKEN=''
OPENAI_API_KEY=''

login(HF_TOKEN)

# Tool to suggest a menu based on the occasion
@tool
def suggest_menu(occasion: str) -> str:
    """
    Suggests a menu based on the occasion.
    Args:
        occasion (str): The type of occasion for the party. Allowed values are:
                        - "casual": Menu for casual party.
                        - "formal": Menu for formal party.
                        - "superhero": Menu for superhero party.
                        - "custom": Custom menu.
    """
    if occasion == "casual":
        return "Pizza, snacks, and drinks."
    elif occasion == "formal":
        return "3-course dinner with wine and dessert."
    elif occasion == "superhero":
        return "Buffet with high-energy and healthy food."
    else:
        return "Custom menu for the butler."


model = LiteLLMModel(
        model_id="ollama_chat/qwen2:7b",  # Or try other Ollama-supported models
        api_base="http://127.0.0.1:1234",  # Default Ollama local server
        num_ctx=8192,
    )


# model = InferenceClientModel(model_id="Qwen/Qwen2.5-Coder-32B-Instruct")

# Using OpenAI/Anthropic (requires smolagents[litellm])
# model = LiteLLMModel(model_id="gpt-3.5",api_key=OPENAI_API_KEY)


# Alfred, the butler, preparing the menu for the party
agent = CodeAgent(tools=[suggest_menu, DuckDuckGoSearchTool()], model=model)

# Preparing the menu for the party
agent.run("Prepare a formal menu for the party")
