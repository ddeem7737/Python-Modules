from abc import abstractmethod, ABC
from typing import Any, Protocol


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


class ExportPlugin(Protocol):

    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


class CSVExportPlugin:

    def process_output(self, data: list[tuple[int, str]]) -> None:
        if not data:
            return
        csv_line = ",".join(value for _, value in data)
        print("CSV Output:")
        print(csv_line)


class JSONExportPlugin:

    def process_output(self, data: list[tuple[int, str]]) -> None:
        if not data:
            return
        pairs = ", ".join(
            f'"item_{rank}": "{value}"' for rank, value in data
        )
        print("JSON Output:")
        print("{" + pairs + "}")


class DataStream:
 
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for element in stream:
            handled = False
            for proc in self._processors:
                if proc.validate(element):
                    proc.ingest(element)
                    handled = True
                    break
            if not handled:
                print(
                    f"DataStream error - Can't process element"
                    f" in stream: {element}"
                )

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self._processors:
            print("No processor found, no data")
            return
        for proc in self._processors:
            remaining = len(proc._data)
            print(
                f"{proc.name}: total {proc._total} items processed,"
                f" remaining {remaining} on processor"
            )

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self._processors:
            collected: list[tuple[int, str]] = []
            for _ in range(nb):
                if not proc._data:
                    break
                collected.append(proc.output())
            if collected:
                plugin.process_output(collected)

 
if __name__ == "__main__":
    print("=== Code Nexus - Data Pipeline ===")

    print("\nInitialize Data Stream...")
    stream = DataStream()
    stream.print_processors_stats()

    print("\nRegistering Processors")
    stream.register_processor(NumericProcessor())
    stream.register_processor(TextProcessor())
    stream.register_processor(LogProcessor())

    batch1 = [
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
    print(f"Send first batch of data on stream: {batch1}")
    stream.process_stream(batch1)
    stream.print_processors_stats()
 
    csv_plugin = CSVExportPlugin()
    print("\nSend 3 processed data from each processor to a CSV plugin:")
    stream.output_pipeline(3, csv_plugin)
    stream.print_processors_stats()

    batch2 = [
        21,
        ["I love AI", "LLMs are wonderful", "Stay healthy"],
        [
            {"log_level": "ERROR",
             "log_message": "500 server crash"},
            {"log_level": "NOTICE",
             "log_message": "Certificate expires in 10 days"},
        ],
        [32, 42, 64, 84, 128, 168],
        "World hello",
    ]
    print(f"\nSend another batch of data: {batch2}")
    stream.process_stream(batch2)
    stream.print_processors_stats()

    json_plugin = JSONExportPlugin()
    print("\nSend 5 processed data from each processor to a JSON plugin:")
    stream.output_pipeline(5, json_plugin)
    stream.print_processors_stats()
