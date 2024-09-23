print ("Olá, Paulino")
nota1=float(input("Informe a primeira nota do aluno: "))
nota2=float(input("Informe a segunda nota do aluno: "))
nota3=float(input("Informe a terceira nota do aluno: "))
media=(nota1+nota2+nota3)/3
if media>=9:
    print(f"Você foi aprovado com distinção, a média é {media:,.2f}")
elif media>=7:
    print(f"Você foi aprovado, a média é {media:,.2f}")
else:
    print(f"Você foi reprovado, a média é {media:,.2f} ")
