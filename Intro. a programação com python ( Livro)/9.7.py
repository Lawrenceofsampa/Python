with open ('pagina.html' , 'w', encoding='utf-8') as pagina:
    pagina.write('<!DOCTYPE html>\n')
    pagina.write('<html lang=\'pt-BR\'>\n')
    pagina.write('<head>\n')
    pagina.write('<meta chartset=\'utf-8\'>\n')
    pagina.write('<title>Titulo da pagina</title>\n')
    pagina.write('</head>\n')
    pagina.write('<body>\n')
    pagina.write('olá')
    for l in range(100):
        pagina.write(f'<p>{l}<p>\n')
    pagina.write('</body>\n')
    pagina.write('</html>\n')