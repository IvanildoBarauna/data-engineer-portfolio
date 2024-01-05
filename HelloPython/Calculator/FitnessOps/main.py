from Calculators.IMC import CALC

w = input("Informe seu peso: ")
h = input("Informe sua altura: ")

if w.isnumeric and h.isnumeric and w and h:
    w = float(w)
    h = float(h)
    CALC(w, h)
else:
    print(f"Os valores informados não são validos para cálculo de IMC.")
