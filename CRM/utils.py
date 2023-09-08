from CRM.models import session, Contract


class ManagerMixins:
    """
    Миксин для использования функций по чтению данных и отображению заголовка меню
     в ProjectManager и ContractManager
    """

    @staticmethod
    def print_menu(menu_items, space=30):
        for item in menu_items:
            print(item.ljust(space), end='')
        print()

    @staticmethod
    def _read_contracts_back():
        return session.query(Contract).all()

    @classmethod
    def read_contracts(cls):
        data = cls._read_contracts_back()
        menu = ["ID", "НАЗВАНИЕ", "ДАТА СОЗДАНИЯ", "ДАТА ПОДПИСАНИЯ", "СТАТУС", "PROJECT"]
        cls.print_menu(menu)
        space = 30
        for contract in data:  # как contract сделать итерируемым объектом
            print(str(contract.id).ljust(space),
                  contract.name.ljust(space),
                  str(contract.created_at).ljust(space),
                  str(contract.signed_date).ljust(space),
                  contract.status.ljust(space),
                  str(getattr(contract.project, "id", "N/A")).ljust(space))

    @staticmethod
    def get_contract_by_id(id):
        contract = session.query(Contract).filter_by(id=id).first()
        if not contract:
            raise ValueError("ОШИБКА - Договор с указанным ID не существует")
        return contract

    @classmethod
    def _complete_contract_back(cls, id):
        try:
            contract = cls.get_contract_by_id(id)
            if contract.status == "завершён":
                raise ValueError("ОШИБКА - Данный контракт уже завершён")
            contract.status = "завершён"
            session.commit()
            print(f"Договор с id {id} успешно завершён")
        except Exception as e:
            print(f"Произошла ошибка {e}")

    @classmethod
    def complete_contract(cls):
        id_contract = int(input("Введите номер договора для завершения -->   "))
        return id_contract