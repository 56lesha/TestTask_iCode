from CRM.bl import ContractManager, ProjectManager


def main():
    menu = {
        1: {
            1: ProjectManager.read_projects,
            2: ProjectManager.create_project,
            3: ProjectManager.add_contract_to_project,
        },
        2: {
            1: ContractManager.read_contracts,
            2: ContractManager.create_contract,
            3: ContractManager.approve_contract,
            4: ContractManager.complete_contract,
        },
    }
    while True:
        choice_cat = int(input("Выберите раздел: \n"
                           "1 - ПРОЕКТ \n"
                           "2 - ДОГОВОР \n"
                           "0 - ЗАВЕРШИТЬ РАБОТУ\n"
                           "\n"
                           "ВВЕДИТЕ ВАШ ВЫБОР -->   " ))
        if choice_cat in menu:
            while True:
                choices = menu[choice_cat]
                choice = int(input(f"Выберите, что вы хотите сделать в меню {'ПРОЕКТ' if choice_cat==1 else 'ДОГОВОР'}: \n"
    
                                   f"1 - просмотреть {'проекты' if choice_cat==1 else 'договоры'} \n"
                                   f"2 - создать {'проект' if choice_cat==1 else 'договор'} \n"
                                   f"3 - {'добавить договор к проекту' if choice_cat==1 else 'подтвердить договор'} \n"
                                   f"{'' if choice_cat==1 else '4 - завершить договор'}  \n"
                                   "0 - НАЗАД\n"
                                   "\n"
                                   "ВВЕДИТЕ ВАШ ВЫБОР -->   " ))

                if choice in choices:
                    if choice == 1 and choice_cat == 1:
                        while True:
                            ProjectManager.read_projects()
                            ProjectManager.read_contracts_of_project()
                            choice = int(input(f"Выберите, что вы хотите сделать с отображёнными договорами \n" 
                                               "1 - Завершить договор \n"
                                               "0 - НАЗАД \n"
                                               ))
                            if choice == 1:
                                ContractManager.complete_contract()
                            elif choice == 0:
                                break

                    else:
                        choices[choice]()
                elif choice == 0:
                    break

        elif choice_cat == 0:
            print("Вы вышли из программы!")
            break




if __name__=="__main__":
    main()