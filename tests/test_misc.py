from utils.generate_init import init_file, main


def test_generate_init_has_been_run():
    """Verify that carta/__init__.py is up-to-date with code generation."""
    existing_init = init_file.read_text()
    main()
    regenerated_init = init_file.read_text()

    assert (
        existing_init == regenerated_init
    ), "`generate_init.py` has changed without being run. Run `generate_init.py` manually"