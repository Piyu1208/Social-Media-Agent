import json
from tools.schemas import TOOLS_SCHEMAS
from tools.registry import TOOL_REGISTRY


def run_agent(client, model, messages):

    while True:

        response = client.chat.completions.create(
            model = model,
            messages=messages,
            tools=TOOLS_SCHEMAS
        )

        msg = response.choices[0].message

        # If LLM wants to call a tool
        if msg.tool_calls:

            tool_call = msg.tool_calls[0]

            tool_name = tool_call.function.name
            args = json.loads(tool_call.function.arguments)

            tool = TOOL_REGISTRY(tool_name)

            result = tool.run(**args)

            messages.append(msg)

            messages.append({
                "role": "tool",
                "name": tool_name,
                "content": result
            })

        else:
            return msg.content