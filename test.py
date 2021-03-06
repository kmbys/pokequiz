import unittest
from lib import get_from_zukan, get_distinct_random_nums

class Test(unittest.TestCase):
    def test_get_from_zukan(self):
        actual = get_from_zukan("004")
        self.assertEqual("ヒトカゲ", actual.name)
        self.assertEqual("あついものを　このむ　せいかく。　あめにぬれると　しっぽの　さきから　けむりが　でるという。　（『ポケモン ソード』より）", actual.description)
        self.assertEqual("https://zukan.pokemon.co.jp/zukan-api/up/images/index/8c45cf85becf84af9de3df62bb84a767.png", actual.image_uri)

    def test_get_distinct_random_nums(self):
        actual = get_distinct_random_nums(151, 30)
        self.assertEqual(len(actual), 30)
        self.assertEqual(len(set(actual)), 30)

if __name__ == "__main__":
    unittest.main()
