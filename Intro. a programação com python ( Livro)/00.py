string_codificada = "\u2153"
string_decodificada = string_codificada.encode().decode("unicode-escape")
print(string_decodificada)

"Teste de decodificação de unicode"