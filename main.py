def tégla_felszín(a: float, b: float, c: float) ->  float:
    felszín: float = 2 * (a * b + a * c + b * c)
    return felszín


def tégla_térfogat(a: float, b: float, c: float) ->  float:
    térfogat: float = a * b * c
    return térfogat


def main() -> None:
    print("Téglatest felszín, térfogat számítás")
    print("")
    print("Az adatokat cm-ben adja meg!")

    a = float(input("Adja meg a téglatest a élét: "))
    b = float(input("Adja meg a téglatest b élét: "))
    c = float(input("Adja meg a téglatest c élét: "))

    if a <= 0 or b <= 0 or c <= 0:
        print("Egyik érték sem lehet negatív szám vagy nulla")
    else:
        felszín: float = round(tégla_felszín(a, b, c), 2)
        térfogat: float = round(tégla_térfogat(a, b, c), 2)
        print(f"A téglatest felszíne: {felszín} cm²")
        print(f"A téglatest térfogata: {térfogat} cm³")



if __name__ == '__main__':
    main()