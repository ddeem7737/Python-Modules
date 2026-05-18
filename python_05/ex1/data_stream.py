from abc import abstractmethod, ABC
from typing import Any


class DataProcessor(ABC):

    name = "Data Processor"

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

    name = "Numeric Processor"

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

    name = "Text Processor"

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

    name = "LogProcessor"

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


class DataStream:
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for i in stream:
            done = False
            for j in self._processors:
                if j.validate(i):
                    j.ingest(i)
                    done = True
                    break
            if not done:
                print(f"DataStream error - Can't process element"
                      f" in stream: {i}")

    def print_processors_stats(self) -> None:
        print("=== Data Stream Statistics ===")
        if not self._processors:
            print("No processor found, no data")
            return
        for i in self._processors:
            all = len(i._data)
            print(
                f"{i.name}: total {i._total} items processed,"
                f" remaining {all} on processor"
                  )


if __name__ == "__main__":
    print("=== Code Nexus - Data Stream ===")

    print("\nInitialize Data Stream...")
    stream = DataStream()
    stream.print_processors_stats()

    print("\nRegistering Numeric Processor")
    stream.register_processor(NumericProcessor())

    batch = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {"log_level": "WARNING",
             "log_message": "Telnet access! Use ssh instead"},
            {"log_level": "INFO",
             "log_message": "User wil is connected"},
        ],
        42,
        ["Hi", "five"],
    ]
    print(f"Send first batch of data on stream: {batch}")
    stream.process_stream(batch)
    stream.print_processors_stats()

    print("\nRegistering other data processors")
    stream.register_processor(TextProcessor())
    stream.register_processor(LogProcessor())

    print("Send the same batch again")
    stream.process_stream(batch)
    stream.print_processors_stats()

    num_consume = 3
    txt_consume = 2
    log_consume = 1
    print(
        f"\nConsume some elements from the data processors:"
        f" Numeric {num_consume}, Text {txt_consume}, Log {log_consume}"
    )
    for proc in stream._processors:
        if proc.name == "Numeric Processor":
            for _ in range(num_consume):
                proc.output()
        elif proc.name == "Text Processor":
            for _ in range(txt_consume):
                proc.output()
        elif proc.name == "Log Processor":
            for _ in range(log_consume):
                proc.output()
    stream.print_processors_stats()
