import json
from openai import OpenAI
from config import GROQ_API_KEY, MODEL
from tools import TOOLS, TOOL_FUNCTIONS

client = OpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1"
)

SYSTEM_PROMPT = (
    "You are a college fee assistant. "
    "Never guess a fee: always use get_course_fee. "
    "Use calculator for arithmetic calculations. "
    "Available course codes: CS101, AI202, DS303. "
    "If no tool is needed, answer directly."
)

def agent(question, max_steps=6):
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": question}
    ]

    for step in range(1, max_steps + 1):

        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=TOOLS,
            temperature=0
        )

        message = response.choices[0].message

        if not message.tool_calls:
            return message.content.strip()

        messages.append({
            "role": "assistant",
            "content": message.content or "",
            "tool_calls": [
                {
                    "id": call.id,
                    "type": "function",
                    "function": {
                        "name": call.function.name,
                        "arguments": call.function.arguments
                    }
                }
                for call in message.tool_calls
            ]
        })

        for call in message.tool_calls:
            name = call.function.name
            name = name.split("<|channel|>")[0]
            arguments = json.loads(call.function.arguments or "{}")

            function = TOOL_FUNCTIONS.get(name)

            if function:
                result = function(**arguments)
            else:
                result = f"Unknown tool: {name}"

            print(f"step {step}: {name}({arguments}) -> {result}")

            messages.append({
                "role": "tool",
                "tool_call_id": call.id,
                "content": result
            })

    return "Stopped: maximum steps reached."


if __name__ == "__main__":
    question = input("You: ")
    print("Agent:", agent(question))