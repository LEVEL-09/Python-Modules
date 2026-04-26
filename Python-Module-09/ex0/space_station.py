from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from typing import Optional


# Define the SpaceStation model with validation rules
class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime = Field(...)
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(max_length=200)


# Example usage and validation
def main() -> None:
    try:
        print("Space Station Data Validation")
        print("========================================")
        space_station_instance = SpaceStation(station_id="ISS001",
                                              name="International Space "
                                              "Station",
                                              crew_size=6, power_level=85.5,
                                              oxygen_level=92.3,
                                              last_maintenance=datetime.now(),
                                              is_operational=False,
                                              notes="qwerty")
        print("Valid station created:")
        print("ID:", space_station_instance.station_id)
        print("Name:", space_station_instance.name)
        print("Crew:", space_station_instance.crew_size, "people")
        print("Power: ", space_station_instance.power_level, "%", sep="")
        print("Oxygen: ", space_station_instance.oxygen_level, "%", sep="")
        print("Status", space_station_instance.is_operational)

        print("\n========================================")
        print("Expected validation error:")
        space_station_instance = SpaceStation(station_id="ISS001",
                                              name="International Space "
                                              "Station",
                                              crew_size=999, power_level=85.5,
                                              oxygen_level=92.3,
                                              last_maintenance=datetime.now(),
                                              is_operational=False,
                                              notes="qwerty")
    except ValidationError as e:
        for error in e.errors():
            print(error["msg"])


if __name__ == "__main__":
    main()
