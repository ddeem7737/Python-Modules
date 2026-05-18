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


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===")

    print("\nTesting Numeric Processor...")
    num_proc = NumericProcessor()

    print(f" Trying to validate input '42': {num_proc.validate(42)}")
    print(f" Trying to validate input 'Hello': {num_proc.validate('Hello')}")

    print(" Test invalid ingestion of string 'foo' without prior validation:")
    try:
        num_proc.ingest("foo")
    except Exception as e:
        print(f" Got exception: {e}")

    data_num = [1, 2, 3, 4, 5]
    print(f" Processing data: {data_num}")
    num_proc.ingest(data_num)

    count = 3
    print(f" Extracting {count} values...")
    for _ in range(count):
        rank, value = num_proc.output()
        print(f" Numeric value {rank}: {value}")

    print("\nTesting Text Processor...")
    txt_proc = TextProcessor()

    print(f" Trying to validate input '42': {txt_proc.validate(42)}")

    data_txt = ["Hello", "Nexus", "World"]
    print(f" Processing data: {data_txt}")
    txt_proc.ingest(data_txt)

    count = 1
    print(f" Extracting {count} value...")
    for _ in range(count):
        rank, value = txt_proc.output()
        print(f" Text value {rank}: {value}")

    print("\nTesting Log Processor...")
    log_proc = LogProcessor()

    print(f" Trying to validate input 'Hello': {log_proc.validate('Hello')}")

    data_log = [
        {"log_level": "NOTICE", "log_message": "Connection to server"},
        {"log_level": "ERROR", "log_message": "Unauthorized access!!"},
    ]
    print(f" Processing data: {data_log}")
    log_proc.ingest(data_log)

    count = 2
    print(f" Extracting {count} values...")
    for _ in range(count):
        rank, value = log_proc.output()
        print(f" Log entry {rank}: {value}")
