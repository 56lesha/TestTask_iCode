from datetime import datetime

from CRM.models import Contract, session, Project


def create_contract_back(data):
    contract = Contract(name=data["name"])
    session.add(contract)
    session.commit()

def read_contracts_back():
    return session.query(Contract).all()


def approve_contract_back(id):
    try:
        contract = session.query(Contract).filter_by(id=id).first()
        if not contract:
            raise ValueError("ОШИБКА - Контракт с указанным ID не существует")
        contract.status = "активен"
        contract.signed_date = datetime.now()
        session.commit()
    except Exception as e:
        print(f"Произошла ошибка {e}")

def complete_contract_back(id):
    try:
        contract = session.query(Contract).filter_by(id=id).first()
        if not contract:
            raise ValueError("ОШИБКА - Контракт с указанным ID не существует")
        contract.status = "завершён"
        session.commit()
    except Exception as e:
        print(f"Произошла ошибка {e}")




def create_project_back(data):
    project = Project(name=data["name"])
    session.add(project)
    session.commit()

def read_projects_back():
    return session.query(Project).all()


def add_contract_to_project_back(id_project, id_contract):
    try:
        project = session.query(Project).filter_by(id=id_project).first()
        if not project:
            raise ValueError("ОШИБКА - Проект с указанным ID не существует")

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
    except Exception as e:
        print(f"Произошла ошибка: {e}")








