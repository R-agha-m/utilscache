from unittest import TestCase, main
from .dict_as_cache import DictAsCache


class TestDictAsCache(TestCase):
    def test_setitem_when_size_is_zero(self):
        dict_as_cache_obj = DictAsCache(size=0)
        number = 10000
        for i in range(number):
            dict_as_cache_obj[i] = i

        self.assertEqual(len(dict_as_cache_obj), number)

    def test_setitem_when_size_is_not_zero(self):
        size = 100
        dict_as_cache_obj = DictAsCache(size=size)
        number = 1000
        for i in range(number):
            print(i)
            dict_as_cache_obj[f"key {i}"] = f"value {i}"
            if i % 200 == 1:
                print(dict_as_cache_obj)

        self.assertEqual(len(dict_as_cache_obj), size)


if __name__ == "__main__":
    main()
