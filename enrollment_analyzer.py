def cadastro_aluno(alunos):
    alu = input('\nNome do Aluno: ')
    alunos[alu] = set()

def cadastro_disciplinas(alunos):
    alu = input('\nNome do aluno: ')

    if alu in alunos:
        i = 1
        ndisc = int(input('\nNumero de disciplinas: '))
        while (i <= ndisc):
            disc = input('\nDisciplina: ')
            alunos[alu].add(disc)
            i += 1
    else:
        print('\nAluno nao encontrado')

def listar_alunos(alunos):
    for i,alu in enumerate(alunos, start=1):
        print(f'\n{i} - {alu}')

def listar_disciplinas(alunos):
    alu = input('\nNome do aluno:')
    if alu in alunos:
        print('\nDISCIPLINAS:\n')
        for i,disc in enumerate(alunos[alu], start=1):
            print(f'{i} - {disc}')
    else:
        print('Aluno nao encontrado')
    
def comparar_disciplinas(alunos):
    alu1 = input('Nome do primeiro aluno: ')
    alu2 = input('Nome do segundo aluno: ')

    if alu1 in alunos and alu2 in alunos:
        print('\nDISCIPLINAS EM COMUM:\n')
        print(alunos[alu1] & alunos[alu2])
    
    else:
        print('\nAluno nao encontrado')

def todas_disciplinas(alunos):
    
    todas = set()

    for disciplinas in alunos.values():
        todas = todas.union(disciplinas)

    print(todas)

def disciplinas_exclusivas(alunos):

    exclu = set()

    for disciplinas in alunos.values():
        exclu = exclu.symmetric_difference(disciplinas)
    
    print(exclu)

alunos = {}
while True:
    print('\n[1] Cadastrar aluno\n[2] Adicionar disciplina\n[3] Listar alunos\n[4] Ver disciplinas de um aluno\n[5] Comparar disciplinas entre alunos\n[6] Ver todas disciplinas da turma\n[7] Sair\n')
    opcao = int(input('Escolha uma opcao: '))

    if opcao == 1:
        cadastro_aluno(alunos)

    elif opcao == 2:
        cadastro_disciplinas(alunos)

    elif opcao == 3:
        listar_alunos(alunos)

    elif opcao == 4:
        listar_disciplinas(alunos)
    
    elif opcao == 5:
        comparar_disciplinas(alunos)

    elif opcao == 6:
        todas_disciplinas(alunos) 
    
    elif opcao == 7:
        break

    else:
        print('\nOpcao invalida!')

print('\nPrograma encerrado')

