import gzip
from pathlib import Path
import json

from pytest_benchmark.fixture import BenchmarkFixture
import pypandoc

from carta import convert

test_files = Path(__file__).parent / "test_files"

with gzip.open(test_files/ "benchmark_markdown.json.gz", "rt") as f:
    BENCHMARK_DATA = json.load(f)


def convert_text_carta():
    return [convert(d).from_markdown.to_html() for d in BENCHMARK_DATA]

def convert_text_pandoc():
    return [pypandoc.convert_text(d, "html", format="md") for d in BENCHMARK_DATA]

def test_benchmark_convert_text_carta(benchmark: BenchmarkFixture):
    result = benchmark(convert_text_carta)
    assert len(result) == len(BENCHMARK_DATA)

def test_benchmark_convert_text_pandoc(benchmark: BenchmarkFixture):
    result = benchmark(convert_text_pandoc)
    assert len(result) == len(BENCHMARK_DATA)
