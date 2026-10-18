import gzip
import json
from pathlib import Path
import requests
from typing import TypedDict
import base64
import pypandoc

test_files = Path(__file__).parent.resolve()
MAX_LINES = 100

url = "https://github.com/davidmyersdev/markdown-dataset/raw/70d94343d0efce6e6ae3658992fb747f735a1ea8/data/markdown.json"


class MarkdownJsonType(TypedDict):
    licenseKey: str
    licenseName: str
    licenseUrl: str
    markdownEncoded: str
    markdownEncoding: str
    repoId: int
    repoName: str
    repoUrl: str
    sha: str
    updatedAt: int


res = requests.get(url)
data: list[MarkdownJsonType] = json.loads(res.content)
markdown_files = []
skips = 0
for i, item in enumerate(data):
    if i >= MAX_LINES:
        break

    if item["markdownEncoding"] != "base64":
        continue

    markdown_encoded = item["markdownEncoded"]
    markdown_decoded = base64.b64decode(markdown_encoded).decode("utf-8")
    try:
        pypandoc.convert_text(markdown_decoded, "html", format="md")
    except Exception as e:
        skips +=1
        continue
    markdown_files.append(markdown_decoded)

with gzip.open(test_files/ "benchmark_markdown.json.gz", "wt") as f:
    json.dump(markdown_files, f)

print(f"skipped {skips} files")