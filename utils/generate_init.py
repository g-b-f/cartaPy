from pathlib import Path

tab = " "*4
tab2 = tab*2

init_file = Path(__file__).parent.parent / "carta" / "__init__.py"
formats = {
    "markdown": "markdown",
    # "md": "markdown",
    "html": "html"
}

preamble ="""# generated programmatically. Do not edit.

from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from carta import _rust_wrapper # type: ignore[reportMissingModuleSource]
else:
    import _rust_wrapper

"""

convert_func ="""
def convert(input: str|Path):
    if isinstance(input, Path):
        input = input.read_text()
    return Text(input)
"""

from_class = [
"""
@dataclass
class From:
    _text: str
    from_fmt: str

    def _convert(self, to:str) -> str:
        return _rust_wrapper.convert_text(self.from_fmt, to, self._text)
"""
]

text_class = [
"""
@dataclass
class Text:
    _text: str
"""
]

def main():

    for friendly_name, internal_name in formats.items():
        from_class.append(f"{tab}@property")
        from_class.append(f"{tab}def to_{friendly_name}(self):")
        from_class.append(f'{tab2}return self._convert("{internal_name}")')
        from_class.append("")

        text_class.append(f"{tab}@property")
        text_class.append(f"{tab}def from_{friendly_name}(self):")
        text_class.append(f'{tab2}return From(self._text, "{internal_name}")')
        text_class.append("")
        


    with open(init_file, "w") as f:
        f.write(preamble)
        f.write("\n".join(from_class))
        f.write("\n".join(text_class))
        f.write(convert_func)

    print(f"Generated {init_file} with formats: {', '.join(formats.keys())}")


if __name__ == "__main__":
    main()