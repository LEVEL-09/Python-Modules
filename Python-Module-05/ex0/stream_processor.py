from typing import Any, List, Dict, Union, Optional
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        character_total = 0
        result = result.strip("\"")
        for _ in result:
            character_total += 1
        return f"Processed text: {character_total} characters, \
{len(result.split())} words"


class NumericProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if type(data) is int:
            data = [data]
        string_of_data = ', '.join([str(i) for i in data])
        return string_of_data

    def validate(self, data: Any) -> bool:
        if type(data) is int:
            data = [data]
        try:
            for i in data:
                int(i)
            return True
        except Exception:
            return False

    def format_output(self, result: str) -> str:
        arg = result.split(", ")
        sum = 0
        total_arg = len(arg)
        for total in arg:
            sum += int(total)
        return f"Processed {total_arg} numeric values, \
sum={sum}, avg={sum/int(total_arg)}"


class TextProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        result: str = "\"" + data + "\""
        return result

    def validate(self, data: Any) -> bool:
        try:
            for c in data:
                if c.isdigit():
                    return False
            return True
        except Exception:
            return False

    def format_output(self, result: str) -> str:
        return super().format_output(result)


class LogProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        log_process = f"{data[0]}: {data[1]}"
        return log_process

    def validate(self, data: Any) -> bool:
        if data not in ("ERROR", "INFO", "WARNING"):
            return False
        return True

    def format_output(self, result: str) -> str:
        output = result.split(":")
        if output[0] in ("ERROR", "WARNING"):
            return f"[ALERT] {output[0]} level detected: {output[1]}"
        elif output[0] == "INFO":
            return f"[INFO] {output[0]} level detected: {output[1]}"
        return ""


if __name__ == "__main__":
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    print("Initializing Numeric Processor...")
    numeric: Union[Optional[int], List[int]] = [1, 2, 3, 4, 5]
    numericprocessor1 = NumericProcessor()
    if numericprocessor1.validate(numeric):
        print(f"Processing data: {numeric}")
        result: str = numericprocessor1.process(numeric)
        print("Validation: Numeric data verified")
        print(f"Output: {numericprocessor1.format_output(result)}")
    else:
        print("Validation: Numeric data not verified")

    print("\nInitializing Text Processor...")
    text: str = "Hello Nexus World"
    textprocessor1 = TextProcessor()
    if textprocessor1.validate(text):
        result_text: str = textprocessor1.process(text)
        print(f"Processing data: {result_text}")
        print("Validation: Text data verified")
        print(f"Output: {textprocessor1.format_output(result_text)}")
    else:
        print("Validation: Text data not verified")

    print("\nInitializing Log Processor...")
    log: Dict[str, str] = {
        "ERROR": "Connection timeout"
    }
    logprocessor1 = LogProcessor()
    for key, value in log.items():
        if logprocessor1.validate(key) and type(value) is str:
            result = logprocessor1.process([key, value])
            print(f"Processing data: {result}")
            print("Validation: Log data verified")
            print(f"Output: {logprocessor1.format_output(result)}")
        else:
            print("Validation: Log data not verified")

    print("\n=== Polymorphic Processing Demo ===\n")

    print("Processing multiple data types through same interface...")
    numeric2: Union[Optional[int], List[int]] = [1, 2, 3]
    if numericprocessor1.validate(numeric2):
        num2_result: str = numericprocessor1.process(numeric2)
        print(f"Result 1: {numericprocessor1.format_output(num2_result)}")

    text2: str = "silver cloud"
    if textprocessor1.validate(text2):
        text2_result: str = textprocessor1.process(text2)
        print(f"Result 2: {textprocessor1.format_output(text2_result)}")

    log2: Dict[str, str] = {
        "INFO": "System ready"
    }
    for key, value in log2.items():
        if logprocessor1.validate(key) and type(value) is str:
            result = logprocessor1.process([key, value])
            print(f"Result 3: {logprocessor1.format_output(result)}")

    print("\nFoundation systems online. Nexus ready for advanced streams.")
