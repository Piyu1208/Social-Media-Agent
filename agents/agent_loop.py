import json
from tools.schemas import TOOLS_SCHEMAS
from tools.registry import TOOL_REGISTRY


def run_agent(client, model, messages):

    while True:

        response = client.chat.completions.create(
            model = model,
            messages=messages,
            tools=TOOLS_SCHEMAS,
            tool_choice="auto"
        )

        msg = response.choices[0].message

        # If LLM wants to call a tool
        if msg.tool_calls:

            tool_call = msg.tool_calls[0]
            tool_name = tool_call.function.name
            args = json.loads(tool_call.function.arguments)

            print(f"[Tool Call] {tool_name}({args})")

            tool = TOOL_REGISTRY[tool_name]
            result = tool.run(**args)

            print(f"[Tool Result] {result[:200]}")

            messages.append({
                "role": msg.role,
                "content": msg.content,
                "tool_calls": [
                    {
                        "id": tc.id,
                        "type": tc.type,
                        "function": {
                            "name": tc.function.name,
                            "arguments": tc.function.arguments
                        }
                    }
                    for tc in msg.tool_calls
                ]
            })

            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "name": tool_name,
                "content": result
            })

        else:
            return msg.content