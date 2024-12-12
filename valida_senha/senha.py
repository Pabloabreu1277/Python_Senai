#Realizar a função da verificação da senha

import string

# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
# print(string.punctuation)
# print(string.digits)

def  Valida_Senha( Senha: str) -> bool:
    minusculas = string.ascii_lowercase
    maiusculas = string.ascii_uppercase
    especiais = string.punctuation
    numeros = string.digits
    lminuscula = False
    lmaiuscula = False
    lespecial = False
    lnumero = False
    lRetorno = False

    # lminuscula, lmaiuscula, lespecial, lnumero = False, False, False, False

    for caracter in Senha:
        if caracter in minusculas:
            lminuscula = True
        elif caracter in maiusculas:
            lmaiuscula = True
        elif caracter in especiais:
            lespecial = True
        elif caracter in numeros:
            lnumero = True
        # print(caracter)

    lRetorno = lminuscula and lmaiuscula and lespecial and lnumero and len(Senha) >= 8

    return lRetorno


print(Valida_Senha('senhaManeira123&'))