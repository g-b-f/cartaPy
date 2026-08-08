import pytest

from tests.test_conversion import get_from_obj
from utils.generate_init import (
    from_format_mapping,
    to_format_mapping,
)


class TestAttributesExist:
    @pytest.mark.parametrize(("friendly_name", "internal_name"), from_format_mapping.items())
    def test_from_format_mapping(self, friendly_name:str, internal_name: str):
        from_obj = get_from_obj("sample", friendly_name)
        assert from_obj.from_format == internal_name
        assert from_obj._document._data == "sample"

    @pytest.mark.parametrize("from_name", from_format_mapping.keys())
    @pytest.mark.parametrize("to_name", to_format_mapping.keys())
    def test_format_mapping_attributes_exists(self, from_name: str, to_name:str):
        from_obj = get_from_obj("sample", from_name)
        assert hasattr(from_obj, f"to_{to_name}")