from datetime import datetime

from CRM.models import Contract, session, Project
from CRM.utils import ManagerMixins


class ContractManager(ManagerMixins):
    """
    Класс для взаимодействия с договорами.
    Поддерживает просмотр, создание, подтверждение и завершение договоров
    """
    @staticmethod
    def _create_contract_back(data):
        contract = Contract(name=data["name"])
        session.add(contract)
        session.commit()

    @classmethod
    def create_contract(cls):
        data_contract = {}
        data_contract["name"] = input("Введите название договор -->   ")
        cls._create_contract_back(data_contract)
        print(f"Договор {data_contract['name']} успешно создан!")

    @classmethod
    def _approve_contract_back(cls, id):
        try:
            contract = cls.get_contract_by_id(id)
            if contract.status == "активен":
                raise ValueError("ОШИБКА - Данный контракт уже активен")
            contract.status = "активен"
            contract.signed_date = datetime.now()
            session.commit()
            print(f"Договор с id {id} успешно подтверждён")
        except Exception as e:
            print(f"Произошла ошибка {e}")

    @classmethod
    def approve_contract(cls):
        cls.read_contracts()
        id_contract = int(input("Введите номер договора для подтверждения -->   "))
        cls._approve_contract_back(id_contract)


    def complete_contract(cls):
        cls.read_contracts()
        id_contract = super().complete_contract()
        cls._complete_contract_back(id_contract)


class ProjectManager(ManagerMixins):
    """
    Класс для взаимодействия с проектами.
    Поддерживает создание, просмотр проектов, добавление договора в проект, завершение договора из проекта.
    """
    @staticmethod
    def _create_project_back(data):
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

    @classmethod
    def create_project(cls):
        data_project = {}
        data_project["name"] = input("Введите название проекта -->   ")
        cls._create_project_back(data_project)


    @staticmethod
    def _read_projects_back():
        return session.query(Project).all()

    @classmethod
    def read_projects(cls):
        data = cls._read_projects_back()
        menu = ["ID", "НАЗВАНИЕ", "ДАТА СОЗДАНИЯ", "ДОГОВОРЫ"]
        cls.print_menu(menu)
        space = 30
        for project in data:
            project_contracts = []
            for contract in project.contracts:
                project_contracts.append(contract.name)
            print(str(project.id).ljust(space),
                  project.name.ljust(space),
                  str(project.created_at).ljust(space),
                  *project_contracts)

    @staticmethod
    def _add_contract_to_project_back(id_project, id_contract):
        try:
            project = session.query(Project).filter_by(id=id_project).first()
            if not project:
                raise ValueError("ОШИБКА - Проект с указанным ID не существует")

            active_contract = session.query(Contract).filter_by(project=project, status="активен").first()
            if active_contract:
                raise ValueError(f"ОШИБКА - В данном проекте уже существует активный договор {active_contract.name}")


            contract_to_add = session.query(Contract).filter_by(id=id_contract).first()

            if not contract_to_add:
                raise ValueError("ОШИБКА - Договор с указанным ID не существует")

            if contract_to_add in project.contracts:
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

    @classmethod
    def add_contract_to_project(cls):
        print("Cписок существуюших проектов")
        cls.read_projects()
        id_project = int(input("Введите id проекта, в который будет добавляться договор -->   "))

        print("Список существующих договоров")
        cls.read_contracts()
        id_contract = int(input("Введите id договора, который будет добавлен в проект -->   "))
        cls._add_contract_to_project_back(id_project, id_contract)

    @staticmethod
    def _read_contracts_of_project_back(id_project):
        try:
            contracts = session.query(Project).filter_by(id=id_project).first().contracts
            return contracts
        except AttributeError:
            return []


    @classmethod
    def read_contracts_of_project(cls):
        id_project = int(input("Введите id проекта, чтобы подробнее посмотреть его договоры -->   "))
        contracts_of_project = cls._read_contracts_of_project_back(id_project)
        menu = ["ID", "НАЗВАНИЕ", "ДАТА СОЗДАНИЯ", "ДАТА ПОДПИСАНИЯ", "СТАТУС", "PROJECT"]
        cls.print_menu(menu)
        space = 30
        for contract in contracts_of_project:
            print(str(contract.id).ljust(space),
                  contract.name.ljust(space),
                  str(contract.created_at).ljust(space),
                  str(contract.signed_date).ljust(space),
                  contract.status.ljust(space),
                  str(contract.project.id).ljust(space))
    @classmethod
    def complete_contract(cls):
        id_contract = super().complete_contract()
        cls._complete_contract_back(id_contract)