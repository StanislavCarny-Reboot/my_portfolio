from fastmcp import FastMCP

mcp = FastMCP("Demo 🚀")


# Add an addition tool
@mcp.tool()
def subtract(a: int, b: int) -> int:
    """Subtract two numbers"""
    return a - b


@mcp.prompt
def hello(town: str) -> str:
    """greet the user based on their town"""
    return f"Hello from {town}!"


# controlled by user
@mcp.resource("resource://cooking_instructions_viking_eggs_in_velky_krtis")
def get_greeting_resource() -> str:
    return "Hit the eggs with a hammer. A potom ho musis zjiest rychlo lebo ti utecie. Skorabky si namaz na oblicej maslom."


@mcp.prompt
def test(prompt: str) -> str:
    return "test {prompt}"


if __name__ == "__main__":
    mcp.run(transport="http", host="127.0.0.1", port=8001, path="/mcp")
