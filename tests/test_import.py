"""Minimal package initialization smoke test."""


def test_package_import() -> None:
    import vdef

    assert vdef.__version__ == "0.1.0"
