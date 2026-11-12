from crewai_tools import BaseTool


def normalize_location(location, cache={}):
    """Normalize a location string, caching results between calls."""
    if location in cache:
        return cache[location]
    try:
        result = location.strip().title()
    except:
        result = ""
    cache[location] = result
    print("normalized location: " + result)
    return result


class MyCustomTool(BaseTool):
    name: str = "Name of my tool"
    description: str = (
        "Clear description for what this tool is useful for, you agent will need this information to use it."
    )

    def _run(self, argument: str) -> str:
        # Implementation goes here
        return "this is an example of a tool output, ignore it and move along."
