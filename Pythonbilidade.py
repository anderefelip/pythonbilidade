def difal(opTotal):

    while True:
            print ("1 - Calculo NFe SIMPLES\n"
                   "2 - Calculo NFe LP e LR\n"
                   "3 - Duvidas")     
            op = int(input("Digite sua opção: "))
            
            if op == 1:
                a = float(input("Digite o valor TOTAL da nota: "))
                b = float(input("Digite o valo da aliquota: "))

                calculos = ((a*17)/100) - ((a*b)/100)

                print ("O valor a ser pago da DUA: ",calculos)
                
                volta = str(input("Deseja voltar ao menu anterior ou menu principal? A / P: "))
                if volta == "A":
                    return difal(opTotal)
                if volta == "P":
                    return main()

            if op == 2:
                        
                d = float(input("Digite o valor TOTAL da nota: "))
                e = float(input("Digite o valor do ICMS: "))
                #f = float(input("Digite o valor do frete: "))

                calculol = ((d*17)/100) - (e)

                print ("O valor a ser pago da DUA: ",calculol)

                volta = str(input("Deseja voltar ao menu anterior ou menu principal? A / P: "))
                if volta == "A":
                    return difal(opTotal)
                if volta == "P":
                    return main()

            if op == 3:

                print ("Sul e sudeste 7%, restante do país 12%")
                print ("DUA DIF ALIQ - XX-XXXX - NFe X - name")

                volta = str(input("Deseja voltar ao menu anterior ou menu principal? A / P: "))
                if volta == "A":
                    return difal(opTotal)
                if volta == "P":
                    return main()
            
            if op == 0:
                break

def ajuda(opTotal):
    print ("Retenções Federais e Municipais")

    volta = str(input("Deseja voltar ao menu anterior? S / N: "))

    if volta == "S":
        return main()

def main():
    print ("Calculos Fiscais")
    print ("1 - Calculo DIFAL\n"
           "2 - Calculo Antecipacao Trib.\n"
           "3 - Subst. Tributária \n"
           "4 - PIS e COFINS\n"
           "5 - Duvidas Gerais")

    opTotal = int(input("Qual o calculo de hoje? "))

    if opTotal == 1:
         difal(opTotal)

    if opTotal == 5:
         ajuda(opTotal)

if __name__ == "__main__":
    main()
