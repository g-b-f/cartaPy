import pytest

from tests.test_conversion import get_from_obj
from utils.generate_init import (
    from_format_mapping,
    to_format_mapping,
)


class TestAttributesExist:
    def test_from_format_mapping(self):
        for friendly_name, internal_name in from_format_mapping.items():
            from_obj = get_from_obj("sample", friendly_name)
            assert from_obj.from_format == internal_name, f"Expected from_format for {friendly_name} to be {internal_name}, but got {from_obj.from_format}"
            assert from_obj._document._data == "sample", f"Expected _document._data for {friendly_name} to be 'sample', but got {from_obj._document._data}"

    def test_format_mapping_attributes_exists(self):
        for from_name in from_format_mapping.keys():
            for to_name in to_format_mapping.keys():    
                from_obj = get_from_obj("sample", from_name)
                assert hasattr(from_obj, f"to_{to_name}"), f"Attribute 'to_{to_name}' does not exist for {from_name}"