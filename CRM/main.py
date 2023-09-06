from CRM.ui import read_contracts, create_contract, approve_contract, complete_contract, read_projects, create_project, \
    add_contract_to_project, complete_contract_from_project


def main():
    choices = {
        1: read_projects,
        2: create_project,
        3: add_contract_to_project,
        4: complete_contract_from_project,
        5: read_contracts,
        6: create_contract,
        7: approve_contract,
        8: complete_contract,
    }

    while True:
        choice = int(input("Enter what do you want to do: \n"
                           
                           "PROJECT \n"
                           "1 - read projects \n"
                           "2 - create project \n"
                           "3 - add_contract_to_project \n"
                           "4 - complete_contract_from_project  \n"
                           "\n"
                           
                           "CONTRACT \n"
                           "5 - read contracts \n"
                           "6 - create contract \n"
                           "7 - approve contract \n"
                           "8 - complete contract \n"
                           "\n"
                           "0 - EXIT\n"
                           
                            "ENTER YOUR CHOICE HERE -->  "


                           ))
        if choice in choices:
            choices[choice]()
        elif choice == 0:
            print("Changing is finished")
            break

if __name__=="__main__":
    main()