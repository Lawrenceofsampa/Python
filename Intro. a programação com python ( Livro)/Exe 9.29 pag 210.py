filmes = {
    'drama': ['cidadao kane' , 'o poderoso chefão'],
    'comedia': ['tempos modernos', 'American pie' , 'Dr. Dolittle'],
    'policia': ['Chuva negra', 'Desejo de matar', ' Dificíl de matar'],
    'Guerra': ['Rambo' , 'Platoon', 'Dunkirk']
}

with open ('filmes.html' , 'w', encoding='utf-8') as pagina:
    pagina.write('''
    <!DOCTYPE html>
    <html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    ''')
    for c, v in filmes.items():
        pagina.write(f'<h1>{c}</h1>\n')
        for e in v:
            pagina.write(f'''
            <ul>
                <li>
                <p>{e}</p>
                </li>
            </ul>
            ''')
    pagina.write('</body></html>')
