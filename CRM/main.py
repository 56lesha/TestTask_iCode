from CRM.ui import read_contracts, create_contract, approve_contract, complete_contract, read_projects, create_project, \
    add_contract_to_project, complete_contract_from_project


def main():

    while True:
        choice_cat = int(input("Выберите раздел: \n"
                           "1 - ПРОЕКТ \n"
                           "2 - ДОГОВОР \n"
                           "0 - ЗАВЕРШИТЬ РАБОТУ\n"
                           "\n"
                           "ВВЕДИТЕ ВАШ ВЫБОР -->   " ))
        if choice_cat == 1:
            while True:
                choices = {
                    1: read_projects,
                    2: create_project,
                    3: add_contract_to_project,
                    4: complete_contract_from_project,
                }
                choice = int(input("Выберите, что вы хотите сделать в меню ПРОЕКТ: \n"
    
                                   "1 - просмотреть проекты \n"
                                   "2 - создать проект \n"
                                   "3 - добавить договор к проекту \n"
                                   "4 - завершить договор  \n"
                                   "0 - НАЗАД\n"
                                   "\n"
                                   "ВВЕДИТЕ ВАШ ВЫБОР -->   " ))

                if choice in choices:
                    choices[choice]()
                elif choice == 0:
                    break

        elif choice_cat == 2:
            while True:
                choices = {
                    1: read_contracts,
                    2: create_contract,
                    3: approve_contract,
                    4: complete_contract,
                }
                choice = int(input("Выберите, что вы хотите сделать в меню ДОГОВОР: \n"
                                   "1 - просмотреть договоры \n"
                                   "2 - создать договор \n"
                                   "3 - подтвердить договор \n"
                                   "4 - завершить договор \n"
                                   "0 - НАЗАД\n"
                                   "\n"
                                   "ВВЕДИТЕ ВАШ ВЫБОР -->  "))

                if choice in choices:
                    choices[choice]()
                elif choice == 0:
                    break

        elif choice_cat == 0:
            print("Вы вышли из программы!")
            break




if __name__=="__main__":
    main()