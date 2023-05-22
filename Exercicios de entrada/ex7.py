dias_total = int(input("Dias: "));

anos = dias_total/365;
meses = (dias_total%365)/30
dias = (dias_total%365)%30

print(f"{anos:.0f} ano(s)");
print(f"{meses:.0f} mes(es)");
print(f"{dias} dia(s)");

