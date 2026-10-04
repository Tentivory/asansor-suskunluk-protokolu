import unittest

from protokol import oksuruk_hukmu, selam_izni, suskunluk_saniyesi


class ProtokolTestleri(unittest.TestCase):
    def test_tek_yolcu_kisa_susar(self):
        sure = suskunluk_saniyesi(1, 1, 0.0)
        self.assertGreater(sure, 0)
        self.assertLess(sure, 3)

    def test_kalabalik_ve_utanma_sureyi_uzatir(self):
        sakin = suskunluk_saniyesi(5, 1, 0.1)
        mahcup = suskunluk_saniyesi(5, 4, 0.9)
        self.assertGreater(mahcup, sakin)

    def test_gecersiz_kat(self):
        with self.assertRaises(ValueError):
            suskunluk_saniyesi(0, 1, 0.2)

    def test_oksuruk_yalnizken_serbest(self):
        metin = oksuruk_hukmu(9, 1)
        self.assertIn("Yalnızsınız", metin)

    def test_iki_katta_selam_yok(self):
        self.assertIn("yok", selam_izni(2, 3))


if __name__ == "__main__":
    unittest.main()
