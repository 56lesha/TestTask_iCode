from CRM.models import session, Contract


class ManagerMixins:
    @staticmethod
    def print_menu(menu_items, space=30):
        for item in menu_items:
            print(item.ljust(space), end='')
        print()

    @staticmethod
    def __read_contracts_back():
        return session.query(Contract).all()

    @classmethod
    def read_contracts(cls):
        data = cls.__read_contracts_back()
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