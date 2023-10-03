import cont_function

def main():
    print ("Calculos Fiscais")
    print ("1 - Calculo DIFAL\n"
           "2 - Calculo Antecipacao Trib.\n"
           "3 - Subst. Tributária \n"
           "4 - PIS e COFINS\n"
           "5 - ICMS Calculo\n"
           "6 - CTe\n"
           "7 - Duvidas Gerais")

    opTotal = int(input("Qual o calculo de hoje? "))

    if opTotal == 1:
        cont_function.difal(opTotal)
         
    if opTotal == 5:
        cont_function.icms(opTotal)

    if opTotal == 6:
        cont_function.cte(opTotal)
    
    if opTotal == 7:
        cont_function.ajuda(opTotal)

if __name__ == "__main__":
    main()
