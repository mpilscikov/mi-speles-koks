# Spēles koks

## Papildu prasības programmatūrai

Spēles sākumā spēles programmatūra gadījuma ceļā saģenerē 5 skaitļus diapazonā no 30000 līdz
Cilvēks-spēlētājs izvēlas, ar kuru no saģenerētajiem skaitļiem viņš vēlas sākt spēli.

## Spēles apraksts

Spēles sākumā ir dots cilvēka-spēlētāja izvēlētais skaitlis. Kopīgs punktu skaits ir vienāds ar 0 (punkti
netiek skaitīti katram spēlētājam atsevišķi). Turklāt spēlē tiek izmantota spēles banka, kura sākotnēji
ir vienāda ar 0. Spēlētāji izdara gājienus pēc kārtas, katrā gājienā dalot pašreizējā brīdī esošu skaitli ar
2,3,4 vai 5. Skaitli ir iespējams sadalīt tikai tajā gadījumā, ja rezultātā veidojas vesels skaitlis. Ja
dalīšanas rezultātā veidojas nepāra skaitlis, tad kopīgajam punktu skaitam tiek pieskaitīts 1 punkts, ja
pāra skaitlis, tad no kopīgā punktu skaita tiek atņemts viens punkts. Savukārt, ja tiek iegūts skaitlis,
kas beidzas ar 0 vai 5, tad bankai tiek pieskaitīts 1 punkts. Spēle beidzas, kad iegūto skaitli vairs nav
iespējams sadalīt. Ja kopīgais punktu skaits ir nepāra skaitlis, tad no tā atņem bankā uzkrātos
punktus. Ja tas ir pāra skaitlis, tad tam pieskaita bankā uzkrātos punktus. Ja kopīgā punktu skaita gala
vērtība ir nepāra skaitlis, uzvar spēlētājs, kas uzsāka spēli. Ja pāra skaitlis, tad otrais spēlētājs.