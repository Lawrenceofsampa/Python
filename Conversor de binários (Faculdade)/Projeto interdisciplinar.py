while True:
    
# -------------------------------------------------------------------------------------------------------------Menu
    a = int(input('''(1) Para coverter decimal a binario (2) Para converter
        Hexadecimal a binario e (3) Para converter octa para binario.
            Digite sua opção:'''))
# -------------------------------------------------------------------------------------------------------------Decimal para binário

    if a > 3 or a < 0:
        print('Comando inválido')
    if a == 1:
        def decimal_para_binario(decimal):
            binario = ''
            while decimal > 0:
                binario += str(decimal % 2)
                decimal //= 2
            return binario[::-1]


        if __name__ == '__main__':
            num = int(input('Entre com o Decimal:'))
            print('O número em binário é: ' + decimal_para_binario(num))
# ---------------------------------------------------------------------------------------------------------------Hexa. para binário
    if a == 2:
        print('Entre com o hexa. para converção : ', end='')
        hnum = input()

        bnum = ""
        chk = 0
        hlen = len(hnum)
        i = 0
        while i < hlen:
            if hnum[i] == '0':
                bnum += "0000"
            elif hnum[i] == '1':
                bnum += "0001"
            elif hnum[i] == '2':
                bnum += "0010"
            elif hnum[i] == '3':
                bnum += "0011"
            elif hnum[i] == '4':
                bnum += "0100"
            elif hnum[i] == '5':
                bnum += "0101"
            elif hnum[i] == '6':
                bnum += "0110"
            elif hnum[i] == '7':
                bnum += "0111"
            elif hnum[i] == '8':
                bnum += "1000"
            elif hnum[i] == '9':
                bnum += "1001"
            elif hnum[i] == 'a' or hnum[i] == 'A':
                bnum += "1010"
            elif hnum[i] == 'b' or hnum[i] == 'B':
                bnum += "1011"
            elif hnum[i] == 'c' or hnum[i] == 'C':
                bnum += "1100"
            elif hnum[i] == 'd' or hnum[i] == 'D':
                bnum += "1101"
            elif hnum[i] == 'e' or hnum[i] == 'E':
                bnum += "1110"
            elif hnum[i] == 'f' or hnum[i] == 'F':
                bnum += "1111"
            else:
                chk = 1
                break
            i = i + 1

        if chk == 0:
            print("\nEquivalente em Binário: ", bnum)
        else:
            print("\nComando inválido")
# -------------------------------------------------------------------------------------------------------------------octal a binário

    if a == 3:
        print("Entre com o octal: ")
        octnum = int(input())
        rev = 0
        chk = 0
        while octnum != 0:
            rem = octnum % 10
            if rem > 7:
                chk = 1
                break
                rev = rem + (rev * 10)
                octnum = int(octnum / 10)
            if chk == 0:
                octnum = rev
                binnum = ""
        while octnum != 0:
            rem = octnum % 10
        if rem == 0:
                binnum = binnum + "000"
        elif rem == 1:
                binnum = binnum + "001"
        elif rem == 2:
                binnum = binnum + "010"
        elif rem == 3:
                binnum = "{0}011".format(binnum)
        elif rem == 4:
                binnum = binnum + "100"
        elif rem == 5:
                binnum = binnum + "101"
        elif rem == 6:
                binnum = binnum + "110"
        elif rem == 7:
                binnum = binnum + "111"

                octnum = int(octnum / 10)
        print("\nEquivalente a numero binário = ", binnum)

    




