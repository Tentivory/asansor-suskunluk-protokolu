#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Asansör Suskunluk Protokolü.

Kapı kapanınca konuşma hakkı askıya alınır. Bu modül o askıyı saniye cinsinden yazar.
"""

from __future__ import annotations

import argparse
import math
import sys


def suskunluk_saniyesi(kat: int, yolcu: int, utanma: float) -> float:
    """Yere bakma süresini hesaplar.

    Formül bilerek abartılıdır. Sonuç yine de mantıklı bir aralıkta kalır.
    """
    if kat < 1:
        raise ValueError("Kat 1'den küçük olamaz. Zemin kat bile en az 1 saygının hak eder.")
    if yolcu < 1:
        raise ValueError("Yolcu yoksa protokol de yok. Asansör kendi kendine susar, buna yardım etmeyiz.")
    if not 0.0 <= utanma <= 1.0:
        raise ValueError("Utanma katsayısı 0 ile 1 arasında olmalı. 1.1 utanma henüz icat edilmedi.")

    taban = 1.4 * math.sqrt(kat)
    kalabalik = 0.85 * math.log1p(yolcu)
    utanc = 3.2 * (utanma ** 1.3)
    ayna_cezasi = 0.4 if yolcu >= 2 else 0.0
    return round(taban + kalabalik + utanc + ayna_cezasi, 2)


def oksuruk_hukmu(saniye: float, yolcu: int) -> str:
    if yolcu == 1:
        return "Yalnızsınız. Öksürebilirsiniz. Asansör sizi yargılamaz, sadece not alır."
    if saniye < 4:
        return "Öksürük serbest. Kısa yolculukta boğaz hakkı tanınır."
    if saniye < 8:
        return "Öksürük şartlı serbest. Tek sefer, kısa, özür dilemeden. Özür diliyorsanız konuşmuş olursunuz."
    return "Öksürük ertelendi. Boğazınız kat numarasına saygı duysun."


def selam_izni(kat: int, yolcu: int) -> str:
    if yolcu == 1:
        return "Selam yasak değil, anlamsız. Aynaya 'günaydın' derseniz tutanak tutulur."
    if kat <= 2:
        return "Selam izni düştü: yok. İki katta tanışıklık başlamaz, biter."
    if kat >= 9 and yolcu <= 2:
        return "Selam izni şartlı: yalnızca çıkışta, kapı açılırken, tek kelime."
    return "Selam izni: başla eğilme. Göz teması 0.3 saniyeyi geçerse protokol ihlali."


def rapor(kat: int, yolcu: int, utanma: float) -> str:
    saniye = suskunluk_saniyesi(kat, yolcu, utanma)
    satirlar = [
        "ASANSÖR SUSKUNLUK TUTANAĞI",
        "---------------------------",
        f"Kat: {kat}",
        f"Yolcu: {yolcu}",
        f"Utanma katsayısı: {utanma:.2f}",
        f"Zorunlu yere bakma: {saniye} saniye",
        f"Öksürük: {oksuruk_hukmu(saniye, yolcu)}",
        f"Selam: {selam_izni(kat, yolcu)}",
        "Hüküm: Konuşulmayacak. Konuşulursa kat değil, mahcubiyet inecektir.",
    ]
    return "\n".join(satirlar)


def etkilesimli() -> int:
    print("Asansör Suskunluk Protokolü — sözlü yoklama")
    print("Rakam girin. Cümle kurmayın. Alışkanlık olmasın.")
    try:
        kat = int(input("Kaçıncı kat? ").strip())
        yolcu = int(input("Kaç yolcu (siz dahil)? ").strip())
        utanma = float(input("Utanma katsayısı (0-1)? ").strip().replace(",", "."))
    except (ValueError, EOFError):
        print("Girdi bozuk. Protokol sizi yargılamadan kapıyı açtı.")
        return 2
    try:
        print()
        print(rapor(kat, yolcu, utanma))
    except ValueError as exc:
        print(f"Ret: {exc}")
        return 1
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Asansörde konuşmama süresini hesaplar.")
    parser.add_argument("--kat", type=int, help="Hedef kat")
    parser.add_argument("--yolcu", type=int, help="Kabin içindeki kişi sayısı")
    parser.add_argument("--utanma", type=float, help="0 ile 1 arası utanma katsayısı")
    args = parser.parse_args(argv)

    if args.kat is None and args.yolcu is None and args.utanma is None:
        return etkilesimli()
    if None in (args.kat, args.yolcu, args.utanma):
        parser.error("Ya hiç argüman vermeyin ya da üçünü birden verin. Yarım protokol olmaz.")
    try:
        print(rapor(args.kat, args.yolcu, args.utanma))
    except ValueError as exc:
        print(f"Ret: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
