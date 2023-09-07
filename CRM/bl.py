from datetime import datetime

from CRM.models import Contract, session, Project


def create_contract_back(data):
    contract = Contract(name=data["name"])
    session.add(contract)
    session.commit()


def read_contracts_back():
    return session.query(Contract).all()

def get_contract_by_id(id):
    contract = session.query(Contract).filter_by(id=id).first()
    if not contract:
        raise ValueError("ОШИБКА - Контракт с указанным ID не существует")
    return contract

def approve_contract_back(id):
    try:
        contract = get_contract_by_id(id)
        if contract.status == "активен":
            raise ValueError("ОШИБКА - Данный контракт уже активен")
        contract.status = "активен"
        contract.signed_date = datetime.now()
        session.commit()
        print(f"Договор с id {id} успешно подтверждён")
    except Exception as e:
        print(f"Произошла ошибка {e}")


def complete_contract_back(id):
    try:
        contract = get_contract_by_id(id)
        if contract.status == "завершён":
            raise ValueError("ОШИБКА - Данный контракт уже завершён")
        contract.status = "завершён"
        session.commit()
        print(f"Договор с id {id} успешно завершён")
    except Exception as e:
        print(f"Произошла ошибка {e}")


def create_project_back(data):
    try:
        active_contract = session.query(Contract).filter_by(status="активен").all()
        if not data["name"]:
            raise ValueError("ОШИБКА - название проекта должно иметь хотя бы один символ")
        if not active_contract:
            raise ValueError("ОШИБКА - запрещено создавать проект, если в базе не существует активных контрактов")
        project = Project(name=data["name"])
        session.add(project)
        session.commit()
        print(f"Проект {data['name']} успешно создан")
    except Exception as e:
        print(f"Произошла ошибка {e}")


def read_projects_back():
    return session.query(Project).all()


def add_contract_to_project_back(id_project, id_contract):
    try:
        project = session.query(Project).filter_by(id=id_project).first()
        if not project:
            raise ValueError("ОШИБКА - Проект с указанным ID не существует")

        active_contract = session.query(Contract).filter_by(project=project, status="активен").first()
        if active_contract:
            raise ValueError(f"ОШИБКА - В данном проекте уже существует активный договор {active_contract.name}")

        project_contracts = project.contracts
        contract_to_add = session.query(Contract).filter_by(id=id_contract).first()

        if not contract_to_add:
            raise ValueError("ОШИБКА - Договор с указанным ID не существует")

        if contract_to_add in project_contracts:
            raise ValueError("ОШИБКА - Нельзя добавить один и тот же договор")

        if contract_to_add.status != "активен":
            raise ValueError("ОШИБКА - В проект можно добавлять только активные договоры")

        if contract_to_add.project_id:
            raise ValueError(f"ОШИБКА - Данный договор уже используется в проекте {contract_to_add.project_id}")

        contract_to_add.project_id = id_project
        session.commit()
        print(f"Договор №{id_contract} успешно добавлен в проект №{id_project}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


def read_contracts_of_project_back(id_project):
    contracts = session.query(Project).filter_by(id=id_project).first().contracts
    return contracts
