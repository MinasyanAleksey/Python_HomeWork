def user_choice():
    print ('Для работы с рациональными числами нажмите - 1')
    print ('Для работы с комплексными числами нажмите - 2')
    print ('Для завершения работы калькулятора нажмите - 3')
    print()
    try:
        player_choice = int(input('Ваш выбор: '))
        print()
    except ValueError as ex:
        print('Неправильный ввод! Введите число 1 или 2 чтобы выбрать режим работы калькулятора.')
        exit(ex)
            
    return player_choice

