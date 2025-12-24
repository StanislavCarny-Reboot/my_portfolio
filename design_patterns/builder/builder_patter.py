from dataclasses import dataclass
from typing_extensions import Self

# PROS
# create for build complex object with a lot of parameters
# separate construction from logic
# 5 + optional fields and you expect more 

# CONS
# boiler plate, overkill for simple functions where you just need a couple of parameters

@dataclass(frozen=True)
class HTMLPage:
    title: str
    body: str

    def render(self) -> str:
        return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{self.title}</title>
</head>
<body>
    {self.body}
</body>
</html>"""


class HTMLBuilder:
    def __init__(self):
        self.title = ""
        self.body_content = []

    def add_title(self, title: str) -> Self:
        self.title = title
        return self

    def add_heading(self, text: str, level: int = 1) -> Self:
        self.body_content.append(f"<h{level}>{text}</h{level}>")
        return self

    def add_paragraph(self, text: str) -> Self:
        self.body_content.append(f"<p>{text}</p>")
        return self

    def build(self) -> str:
        body = "\n".join(self.body_content)
        return HTMLPage(title=self.title, body=body).render()


builder = HTMLBuilder()
# chain functions
page = (
    builder.add_heading("My new heading").add_paragraph("This is my paragraph").build()
)

# or add then one by one
# builder.add_heading("My new heading")
# builder.add_paragraph("This is my paragraph")

print(page)
