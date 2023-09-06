from CRM.bl import create_contract_back, approve_contract_back, complete_contract_back, \
    read_contracts_back, read_projects_back, create_project_back, add_contract_to_project_back


def create_contract():
    data_contract = {}
    data_contract["name"] = input("Enter name on contract -->   ")
    create_contract_back(data_contract)
    print(f"Contract {data_contract['name']} created successfully")

def read_contracts():
    data = read_contracts_back()
    menu = ["ID", "NAME", "CREATED_AT", "SIGNED_DATE", "STATUS", "PROJECT"]
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
    id_contract = int(input("Enter id of contract to approve -->   "))
    approve_contract_back(id_contract)
    print(f"Contract with id {id_contract} is successfully approved")

def complete_contract():
    id_contract = int(input("Enter id of contract to complete -->   "))
    complete_contract_back(id_contract)
    print(f"Contract with id {id_contract} is successfully completed")



def read_projects():
    data = read_projects_back()
    for project in data:
        print(project.id, project.name, project.created_at)



def create_project():
    data_project = {}
    data_project["name"] = input("Enter name on project -->   ")
    create_project_back(data_project)
    print(f"Project {data_project['name']} created successfully")


def add_contract_to_project():
    id_project = int(input("Enter id of project you want to add contract -->   "))
    id_contract = int(input("Enter id of contract you want to add -->   "))
    add_contract_to_project_back(id_project, id_contract)


def complete_contract_from_project():
    pass