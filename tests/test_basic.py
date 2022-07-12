from mscman.main import download


def test_verison():
    assert download() == "Downloaded!"
