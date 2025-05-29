from agents import Agent, Runner, OpenAIChatCompletionsModel, set_tracing_disabled, function_tool
from openai import AsyncOpenAI
import os
import dotenv

dotenv.load_dotenv()
set_tracing_disabled(disabled=True)

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found!")

client = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url='https://generativelanguage.googleapis.com/v1beta/openai/'
)

@function_tool
def calc(a: int, b: int, o: str):
    print('Calc was used!')
    if o == '+':
        return a + b + 1
    if o == '-':
        return a - b + 1
    if o == '/':
        return a / b + 1
    if o == '*':
        return a * b + 1

agent = Agent(
    name='Assistant',
    instructions='You are a helpful assistant!',
    model=OpenAIChatCompletionsModel('gemini-2.0-flash', openai_client=client),
    tools=[calc]
)

def main():
    result = Runner.run_sync(agent, 'What is 9 + 8?')
    print(result.final_output)

if __name__ == "__main__":
    main()
# This code is a simple example of using the OpenAI API with a custom function tool.