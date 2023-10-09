import os, sys
for raiz, diretorios, arquivos in os.walk(sys.argv[1]):
    print('\n Caminho: ' , raiz)
    for d in diretorios:
        print(f' {d}/')
    for f in arquivos:
        print(f' {f}')
    print(f'{len(diretorios)} diretorios(s), {len(arquivos)} arquivos(s)')