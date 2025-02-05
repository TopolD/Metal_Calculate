from pony.orm import db_session, TransactionError
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

    def __init__(self, name_db: str, incoming_data=None, value_for_update=None):
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

    def _check_uniqueness(self):
        if self.value_for_update:
            self.get_record_by_criteria()

            with db_session:

                if self.incoming_data:
                    if self.initial.get(Tcn=self.incoming_data.get('Fuse').get('Tcn')) is not None:
                        return f"Запись  {self.incoming_data['Fuse']['Tcn']} уже существует."
                    if self.initial.get(Name=self.incoming_data.get('Name')) is not None:
                        return f"Запись  {self.incoming_data['Name']} уже существует."
                if self.value_for_update:
                    self._delete_entity()

        return None

    def _create_entity(self):
        uniqueness_error = self._check_uniqueness()
        if uniqueness_error:
            return uniqueness_error

        try:
            with db_session:
                if self.incoming_data.get('Fuse') is not None:

                    self.name_db = 'FuseTarget'
                    fuse_target = self.initial_entity()
                    self.incoming_data['FuseTarget']['Fuse'] = self.initial(**self.incoming_data['Fuse'])
                    fuse_target(**self.incoming_data['FuseTarget'])
                else:
                    self.initial(**self.incoming_data)
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
                if self.initial.get(Name=self.value_for_update.get('search_criteria').get('Name')) is not None:
                    return self.get_record_by_criteria().delete()

        except AttributeError as e:
            print("Ошибка доступа к атрибуту:", e)
        except TypeError as e:
            print("Ошибка типа данных:", e)
        except Exception as e:
            print("Произошла ошибка:", e)
        return False


