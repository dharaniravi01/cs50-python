from twttr import shorten

def main():
    test_shorten()


def test_shorten():
    assert shorten("and") == 'nd'
    assert shorten("And") == 'nd'
    assert shorten("1") == "1"
    assert shorten("hi, its me") == "h, ts m"


if __name__ == "__main__":
    main()
