from typing import Any, List, Dict, Union, Optional
from abc import ABC, abstractmethod


class DataStream(ABC):
    def __init__(self, stream_id: str, type: str) -> None:
        self.stream_id = stream_id
        self.type = type

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "type": self.type
        }


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "Environmental Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        readings_processed = len(data_batch)
        self.average_value = 0.0
        try:
            filtered_data = self.filter_data(data_batch, "temp")
            value = 0.0
            for data in filtered_data:
                value += float(data.split(":")[1])
            if len(filtered_data) != 0:
                self.average_value = value / len(filtered_data)
        except Exception as e:
            print(f"Sensor Process Error: {e}")
        return f"{readings_processed} readings processed"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria is None:
            return super().filter_data(data_batch, criteria)
        try:
            new_list = []
            for data in data_batch:
                if data.split(":")[0] == criteria:
                    new_list += [data]
        except Exception as e:
            raise Exception(f"Filter Data: {e}")
        return new_list

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["average_value"] = self.average_value
        return stats


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "Financial Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        operations = len(data_batch)
        try:
            self.units = 0
            for value in data_batch:
                if value.split(":")[0] == "buy":
                    self.units += int(value.split(":")[1])
                elif value.split(":")[0] == "sell":
                    self.units -= int(value.split(":")[1])

        except Exception as e:
            print(f"Transaction Process Error: {e}")
        return f"{operations} operations"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        try:
            return [data for data in data_batch
                    if int(data.split(":")[1]) > 100]
        except Exception as e:
            print(f"Transaction filter error: {e}")
        return []

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["units"] = self.units
        return stats


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "System Events")

    def process_batch(self, data_batch: List[Any]) -> str:
        events = len(data_batch)
        try:
            self.error_detected = 0
            for data in data_batch:
                if data == "error":
                    self.error_detected += 1
        except Exception as e:
            print(f"Event Process Error: {e}")
        return f"{events} events"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        try:
            return [data for data in data_batch
                    if data == "login" or data == "logout"]
        except Exception as e:
            print(f"Event filter error: {e}")
        return []

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["error_detected"] = self.error_detected
        return stats


class StreamProcessor:
    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        if isinstance(stream, DataStream):
            self.streams.append(stream)

    def process_all(self, data: Dict[str, List[str]]) -> None:
        for stream in self.streams:
            if stream.stream_id in data:
                if isinstance(stream, SensorStream):
                    print(f"- Sensor data: "
                          f"{stream.process_batch(data[stream.stream_id])}")
                elif isinstance(stream, TransactionStream):
                    print(f"- Transaction data: "
                          f"{stream.process_batch(data[stream.stream_id])}")
                elif isinstance(stream, EventStream):
                    print(f"- Event data: "
                          f"{stream.process_batch(data[stream.stream_id])}")


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    print("Initializing Sensor Stream...")
    sensor_stream = SensorStream("SENSOR_001")
    data_batch = ["temp:22.5", "humidity:65", "pressure:1013"]
    sensor_analysis = sensor_stream.process_batch(data_batch)
    data_stats = sensor_stream.get_stats()

    print(f"Stream ID: {data_stats['stream_id']}, "
          f"Type: {data_stats['type']}")
    print(f"Processing sensor batch: {data_batch}")
    print(f"Sensor analysis: {sensor_analysis}, "
          f"avg temp: {data_stats['average_value']:.1f}°C")

    print("\nInitializing Transaction Stream...")
    transaction_stream = TransactionStream("TRANS_001")
    data_batch = ["buy:100", "sell:150", "buy:75"]
    transaction_analysis = transaction_stream.process_batch(data_batch)
    data_stats = transaction_stream.get_stats()

    print(f"Stream ID: {data_stats['stream_id']}, "
          f"Type: {data_stats['type']}")
    print(f"Processing transaction batch: {data_batch}")
    units = data_stats['units']
    sign = ""
    if isinstance(units, (int, float)) and units > 0:
        sign = "+"
    print(f"Transaction analysis: {transaction_analysis}, "
          f"net flow: {sign}{units} units")

    print("\nInitializing Event Stream...")
    event_stream = EventStream("EVENT_001")
    data_batch = ["login", "error", "logout"]
    event_analysis = event_stream.process_batch(data_batch)
    data_stats = event_stream.get_stats()
    print(f"Stream ID: {data_stats['stream_id']}, "
          f"Type: {data_stats['type']}")
    print(f"Processing event batch: {data_batch}")
    print(f"Event analysis: {event_analysis}, "
          f"{data_stats['error_detected']} error detected")

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...\n")

    stream_processor = StreamProcessor()

    all_data = {
        sensor_stream.stream_id: ["light:29", "wind:716"],
        transaction_stream.stream_id: ["buy:200", "sell:50", "buy:10",
                                       "sell:10"],
        event_stream.stream_id: ["error", "login", "logout"]
    }

    stream_processor.add_stream(sensor_stream)
    stream_processor.add_stream(transaction_stream)
    stream_processor.add_stream(event_stream)

    print("Batch 1 Results:")
    stream_processor.process_all(all_data)

    print("\nStream filtering active: High-priority data only")
    event_cont = len(
        event_stream.filter_data(all_data[event_stream.stream_id])
    )
    transaction_cont = len(
        transaction_stream.filter_data(all_data[transaction_stream.stream_id])
    )
    print(f"Filtered results: {event_cont} critical sensor alerts, "
          f"{transaction_cont} large transaction")

    print("\nAll streams processed successfully. Nexus throughput optimal.")
