print()
print("NAMA : FADILA FAJRINI")
print("NIM  : 2310432011")
print("TUGAS MODUL 6")
print("SHIFT 4")
print("=======================")
print()

n = int(input("Masukkan nilai n : "))
glbb= []

for i in range(n):
    v0 = float(input(f"Masukkan nilai v0 ({i+1}): "))
    a = float(input(f"Masukkan nilali a ({i+1}): "))
    t = float(input(f"Masukkan nilai t ({i+1}): "))
    glbb.append((v0, a, t))
    
def hitung_glbb(v0, a, t):
    vt = v0 + a * t
    s = v0 * t + 0.5 * a * t**2
    return vt, s

def tabel (glbb):
    print("-----------------------------------------------------------------------")
    print("| n | kecepatan awal | percepatan | waktu | kecepatan akhir | jarak   |")
    print("-----------------------------------------------------------------------")
    for i, (v0, a, t) in enumerate (glbb):
        vt, s = hitung_glbb (v0, a, t)
        print(f"| {i+1} | {v0:<14} | {a:<10} | {t:<5} | {vt:>15} | {s:>7} |")
        print("-----------------------------------------------------------------------")
    return glbb

print()
hasil = tabel(glbb)
print(hasil)

