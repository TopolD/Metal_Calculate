from pony.orm import db_session, TransactionError, select
from abc import ABC, abstractmethod

from utils_db.Db_models import ConnDb


class AbstractService(ABC):
    @abstractmethod
    def _create_entity(self):
        pass

    def _update_entity(self):
        pass

    def _delete_entity(self):
        pass


class get_instance(AbstractService):

    def __init__(self, name_db, incoming_data, value_for_update=None):
        self.name_db = name_db
        self.db = ConnDb()
        self.incoming_data = incoming_data
        self.value_for_update = value_for_update

        self.initial = self.initial_entity()

    def initial_entity(self):
        try:
            with db_session:
                return getattr(self.db, self.name_db)
        except AttributeError:
            print("Атрибут не найден в объекте базы данных.")
        except TransactionError:
            print("Ошибка транзакции. Проверьте сессию базы данных.")
        except TypeError:
            print("Ошибка типа данных. Проверьте, является ли db объектом.")
        except Exception as e:
            print(f"Произошла непредвиденная ошибка: {e}")

    def get_record_by_criteria(self):
        with db_session:
            return self.initial.get(**self.value_for_update['search_criteria'])

    def _create_entity(self):
        try:
            with db_session:
                return self.initial(**self.incoming_data)
        except AttributeError as e:
            print("Ошибка доступа к атрибуту:", e)
        except TypeError as e:
            print("Ошибка типа данных:", e)
        except Exception as e:
            print("Произошла ошибка:", e)

        return None

    def _update_entity(self):
        try:
            with db_session:
                record = self.get_record_by_criteria()
                for attr_key, attr_value in self.value_for_update['update_data'].items():
                    setattr(record, attr_key, attr_value)
                print('Запись обновлена', record)
        except AttributeError as e:
            print("Ошибка доступа к атрибуту:", e)
        except TypeError as e:
            print("Ошибка типа данных:", e)
        except Exception as e:
            print("Произошла ошибка:", e)

        return None

    def _delete_entity(self):
        try:
            with db_session:
                return self.get_record_by_criteria().delete()
        except AttributeError as e:
            print("Ошибка доступа к атрибуту:", e)
        except TypeError as e:
            print("Ошибка типа данных:", e)
        except Exception as e:
            print("Произошла ошибка:", e)
        return False



