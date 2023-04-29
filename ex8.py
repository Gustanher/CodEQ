a = float(input("Digite A: "));
b = float(input("Digite B: "));
c = float(input("Digite C: "));

delta = b ** 2 - 4 * a * c;

if(delta < 0 or (2 * a == 0) ):
    print("Impossivel calcular");
else:
    R1 = (-b + (delta ** 0.5))/(2 * a);
    R2 = (-b - (delta ** 0.5))/(2 * a);
    print(f"R1 = {R1:.5f}");
    print(f"R2 = {R2:.5f}");