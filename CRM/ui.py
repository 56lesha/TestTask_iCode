from CRM.bl import create_contract_back, approve_contract_back, complete_contract_back, \
    read_contracts_back, read_projects_back, create_project_back, add_contract_to_project_back


def create_contract():
    data_contract = {}
    data_contract["name"] = input("Введите название контракта -->   ")
    create_contract_back(data_contract)
    print(f"Контракт {data_contract['name']} успешно создан!")

def read_contracts():
    data = read_contracts_back()
    menu = ["ID", "НАЗВАНИЕ", "ДАТА СОЗДАНИЯ", "ДАТА ПОДПИСАНИЯ", "СТАТУС", "PROJECT"]
    space = 30
    for m in menu:
        print(m.ljust(space), end='')
    print()
    for contract in data:
        print(str(contract.id).ljust(space),
              contract.name.ljust(space),
              str(contract.created_at).ljust(space),
              str(contract.signed_date).ljust(space),
              contract.status.ljust(space),
              str(contract.project).ljust(space))


def approve_contract():
    id_contract = int(input("Введите номер договора для подтверждения -->   "))
    approve_contract_back(id_contract)
    print(f"Договор с id {id_contract} успешно подтверждён")

def complete_contract():
    id_contract = int(input("Введите номер договора для завершения -->   "))
    complete_contract_back(id_contract)
    print(f"Договор с id {id_contract} успешно завершён")



def read_projects():
    data = read_projects_back()
    menu = ["ID", "НАЗВАНИЕ", "ДАТА СОЗДАНИЯ", "ДОГОВОРЫ"]
    space = 30
    for m in menu:
        print(m.ljust(space), end='')
    print()

    for project in data:
        project_contracts = []
        for contract in project.contracts:
            project_contracts.append(contract.name)
        print(str(project.id).ljust(space),
              project.name.ljust(space),
              str(project.created_at).ljust(space),
              project_contracts)



def create_project():
    data_project = {}
    data_project["name"] = input("Введите название проекта -->   ")
    create_project_back(data_project)
    print(f"Проект {data_project['name']} успешно создан")


def add_contract_to_project():
    print("Cписок существуюших проектов")
    read_projects()
    id_project = int(input("Введите id проекта, в который будет добавляться договор -->   "))

    print("Список существующих договоров")
    read_contracts()
    id_contract = int(input("Введите id договора, который будет добавлен в проект -->   "))
    add_contract_to_project_back(id_project, id_contract)


def complete_contract_from_project():
    pass