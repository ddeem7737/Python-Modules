from abc import abstractmethod, ABC
from typing import Any


class DataProcessor(ABC):
    def __init__(self):
        self._data = []
        self._index = 0
        self._total = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._data:
            raise Exception("No data available in processor")
        return self._data.pop(0)

    def _store(self, value: str) -> None:
        self._data.append((self._index, value))
        self._index += 1
        self._total += 1


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            true_ints = 0
            for i in data:
                if isinstance(i, (int, float)):
                    true_ints += 1
            if true_ints == len(data):
                return True
            return False
        return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise Exception("Improper numeric data")

        if isinstance(data, (int, float)):
            self._store(str(data))
        else:
            for i in data:
                self._store(str(i))


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            true_str = 0
            for i in data:
                if isinstance(i, str):
                    true_str += 1
            if true_str == len(data):
                return True
            return False
        return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise Exception("Improper text data")

        if isinstance(data, str):
            self._store(data)
        else:
            for i in data:
                self._store(i)


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        def is_valid_dict(d):
            return (
                isinstance(d, dict)
                and all(isinstance(k, str) for k in d.keys())
                and all(isinstance(v, str) for v in d.values())
                and "log_level" in d
                and "log_message" in d
            )

        if is_valid_dict(data):
            return True

        if isinstance(data, list):
            return all(is_valid_dict(i) for i in data)

        return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise Exception("Improper log data")

        if isinstance(data, dict):
            text = f"{data['log_level']}: {data['log_message']}"
            self._store(text)

        else:
            for i in data:
                text = f"{i['log_level']}: {i['log_message']}"
                self._store(text)

