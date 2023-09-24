import main

def difal(opTotal):
    while True:
            print ("1 - Simples\n"
                   "2 - Dupla")     
            
            op = int(input("Digite sua opção: "))
            
            if op == 1:
                a = float(input("Digite o valor da operação: "))
                b = float(input("Digite o valo da aliquota interna: "))
                c = float(input("Digite o valo da aliquota interestadual: "))

                difs = (a*((b/100)-(c/100)))

                print (f"O valor é R${difs:.2f}")
                
                volta = str(input("Deseja voltar ao menu anterior ou menu principal? A / P: "))
                if volta.lower() == "A":
                    return difal(opTotal)
                if volta.lower() == "P":
                    return main()

            if op == 2:
                        
                d = float(input("Digite o valor da operação: "))
                e = float(input("Digite o valo da aliquota interestadual: "))
                f = float(input("Digite o valo da aliquota interna: "))

                calc1 = d*(e/100)
                icms_inters = calc1
                BC1 = d - icms_inters
                BC2 = (BC1/(1-(f/100)))
                icms_int = (BC2*(f/100))
                
                difd = icms_int - icms_inters

                print (f"O valor é R${difd:.2f}")

                volta = str(input("Deseja voltar ao menu anterior ou menu principal? A / P: "))
                if volta.lower() == "A":
                    return difal(opTotal)
                if volta.lower() == "P":
                    return main()
            
            if op == 0:
                break

def icms(opTotal):
    vTprod = float(input("Digite a base de calculo do produto: "))
    red = float(input("Digite o calculo do imposto ou sua redução: "))
    alqinterna = float(input("Digite a aliquota interna: "))
    
    calc_icms = (vTprod*(red)/100)
    calc_final = ((calc_icms - vTprod)*(alqinterna/100))*-1
    print (f"O valor é R${calc_final:.2f}")
    

def cte(opTotal):
    frete = float(input("Digite o valor do frete: "))
    alqest = float(input("Digite o valo da aliquota: "))

    calculocte = (frete*(alqest)/100)

    print (f"O valor é R${calculocte:.2f}")

def ajuda(opTotal):
    print ("Retenções Federais e Municipais")

    volta = str(input("Deseja voltar ao menu anterior? S / N: "))

    if volta == "S":
        return main()
