

print("Här pratikera ni att skappa koder och lägger i Github")

print("konsert biljeter")

biljet = 200
ålder = int(input("Hur gammal är ni? "))
rabat = biljet * 0.9

if ålder < 18:
    print("Tyväar får ni inte delta på konsert. Bara för 18+ gammal ålder")
elif ålder > 65:
    print("biljet kostar ", rabat, "med 10% rabat. ")
else:
    print("Biljet kostar ", biljet)