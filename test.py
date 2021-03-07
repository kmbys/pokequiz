import unittest
from lib import Stage, Level, get_from_zukan, get_distinct_random_nums

class Test(unittest.TestCase):
    def test_stage_init_normal_int(self):
        actual = Stage(5)
        self.assertEqual(actual.current, 5)
        self.assertEqual(actual.next, 6)

    def test_stage_init_normal_none(self):
        actual = Stage(None)
        self.assertEqual(actual.current, 1)
        self.assertEqual(actual.next, 2)

    def test_stage_init_error_float(self):
        with self.assertRaises(ValueError):
            Stage(6.4)

    def test_stage_init_error_negative(self):
        with self.assertRaises(ValueError):
            Stage(-1)

    def test_stage_init_error_zero(self):
        with self.assertRaises(ValueError):
            Stage(0)

    def test_stage_init_error_markup(self):
        with self.assertRaises(ValueError):
            Stage("<h1>big</h1>")

    def test_level_init(self):
        actual = Level.VERY_EASY
        self.assertEqual(actual.key, 0)
        self.assertEqual(actual.label, "ベリーイージー")
        self.assertEqual(actual.max_no, 151)

    def test_level_from_key_normal(self):
        actual = Level.from_key(1)
        self.assertEqual(actual.key, 1)
        self.assertEqual(actual.label, "イージー")
        self.assertEqual(actual.max_no, 251)

    def test_level_from_key_error(self):
        with self.assertRaises(ValueError):
            Level.from_key(6)

    def test_level_next_normal(self):
        actual = Level.NORMAL.next()
        self.assertEqual(actual, Level.HARD)

    def test_level_next_error(self):
        with self.assertRaises(ValueError):
            Level.ULTRA_HARD.next()

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
