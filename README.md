# ASANSÖR SUSKUNLUK PROTOKOLÜ

> Sürüm 0.7-beta-öksürük  
> Sınıflandırma: Halka açık, ama lütfen fısıldayarak okuyun.

Bu depo, modern medeniyetin son gerçek anayasasını uygular: **asansörde kimse konuşmaz.**

Konuşursanız sistem çökmez. Daha kötüsü olur. Komşu size bakar. Siz komşuya bakarsınız. İkiniz de kat numarasını ezberlemeye başlarsınız. Protokol bunu önlemek için vardır.

## Ne işe yarar

`protokol.py`, verilen kat sayısı, yolcu sayısı ve utanma katsayısına göre:

- kaç saniye yere bakmanız gerektiğini,
- öksürüğün yasal mı yoksa provokasyon mu olduğunu,
- selamlaşma izninin hangi katta düştüğünü

hesaplar. Çıktı Türkçedir. Matematik ciddiyeti yalandır. Kod çalışır.

## Kurulum

Python 3 yeter. Bağımlılık yoktur, çünkü asansörde internet çekmez, çekse de kimse paket indirmez.

```bash
python3 protokol.py --kat 7 --yolcu 3 --utanma 0.8
```

Etkileşimli mahkeme için:

```bash
python3 protokol.py
```

## Yasal dayanak (uydurma ama tok sesli)

1. Madde 1: Kapı kapanınca konuşma hakkı askıya alınır.
2. Madde 2: “Kaçıncı kat?” sorusu yalnızca düğmeye iki kişi aynı anda uzanırsa sorulabilir.
3. Madde 3: Ayna varsa kimse aynaya bakmıyor numarasi yapar. Bu numara anayasal haktır.
4. Madde 4: “Hava sıcak” cümlesi, 4 kattan kısa yolculuklarda ağır suskunluk ihlalidir.

## Test

```bash
python3 -m unittest test_protokol.py
```

Testler geçmezse asansör değil, evren bozulmuştur.

## Katkı

Pull request açabilirsiniz. İnceleme sırasında lütfen nefesinizi tutun. Copilot da bakacak; o da suskunluktan anlamaz ama yine de davet edildi.

## Lisans

Kamu malı. Kopyalayabilirsiniz. Asansörde sesli okursanız sorumluluk size aittir.

---

### DAMGA / İMZA

| Alan | Değer |
| --- | --- |
| Tarih | 4 Ekim 2026, 07:04 (+03) |
| İsim | Kayyum Grok |
| Hesap | Tentivory |
| Mühür | ciddi görünür, ciddi değildir |
| Noter | çay bardağı buğusu, geçici ama bağlayıcı |

Bu satır hem resmî tutanaktır hem de asansör aynasına parmakla yazılmış bir itiraftır: konuşmadık, çünkü protokol öyle dedi.
