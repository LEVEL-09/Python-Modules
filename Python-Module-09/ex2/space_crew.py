from pydantic import BaseModel, Field, model_validator, ValidationError
from enum import Enum
from datetime import datetime
from typing import List
from typing_extensions import Self
from pydantic_core import PydanticCustomError


class Rank(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


# This model represents a crew member of a space mission, with various
# fields and validation rules.
class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank = Field(...)
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


# This model represents a space mission, including its details and crew,
# with custom validation rules to ensure data integrity.
class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime = Field(...)
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def mission_validation(self) -> Self:
        member_rank = [member.rank for member in self.crew]
        if not self.mission_id.startswith("M"):
            raise PydanticCustomError("ID error",
                                      "Mission ID must start with \"M\"")
        elif (Rank.COMMANDER not in member_rank
              and Rank.CAPTAIN not in member_rank):
            raise PydanticCustomError("Rank error", "Must have at least one"
                                      "Commander or Captain")
        elif self.duration_days > 365:
            for member in self.crew:
                if member.years_experience < 5:
                    raise PydanticCustomError("Missions error", "Long "
                                              "missions (> 365 days) need 50% "
                                              "experienced crew (5+ years)")
        for member in self.crew:
            if not member.is_active:
                raise PydanticCustomError("Active error",
                                          "All crew members must be active")
        return self


# This function demonstrates the creation of valid and invalid space mission
# instances, showing how the custom validation rules work in practice.
def main() -> None:
    print("Space Mission Crew Validation")
    try:
        print("=========================================")
        crew_member = CrewMember(member_id="A51930", name="Neil Armstrong",
                                 rank=Rank.COMMANDER, age=38,
                                 specialization="aeronautical engineer",
                                 years_experience=5)
        crew_member2 = CrewMember(member_id="J201930", name="Buzz Aldrin",
                                  rank=Rank.OFFICER, age=39,
                                  specialization="mission planning",
                                  years_experience=18)

        moon_mission = SpaceMission(mission_id="M-APOLLO11",
                                    mission_name="Apollo",
                                    destination="Moon",
                                    launch_date=datetime(1969, 7, 16),
                                    duration_days=400,
                                    crew=[crew_member, crew_member2],
                                    mission_status="starting",
                                    budget_millions=355.10)

        print("Valid mission created:")
        print("Mission:", moon_mission.mission_name)
        print("ID:", moon_mission.mission_id)
        print("Destination:", moon_mission.destination)
        print("Duration:", moon_mission.duration_days, "days")
        print("Budget: ", "$", moon_mission.budget_millions, "M", sep="")
        print("Crew size: ", len(moon_mission.crew))
        print("Crew members:")
        for crew_member in moon_mission.crew:
            print(f"- {crew_member.name} ({crew_member.rank.value}) "
                  f"- {crew_member.specialization}")

        print("\n=========================================")
        print("Expected validation error:")
        crew_member = CrewMember(member_id="A51930", name="Neil Armstrong",
                                 rank=Rank.CADET, age=38,
                                 specialization="aeronautical engineer",
                                 years_experience=5)
        crew_member2 = CrewMember(member_id="J201930", name="Buzz Aldrin",
                                  rank=Rank.OFFICER, age=39,
                                  specialization="mission planning",
                                  years_experience=18)

        moon_mission = SpaceMission(mission_id="M-APOLLO11",
                                    mission_name="Apollo",
                                    destination="Moon",
                                    launch_date=datetime(1969, 7, 16),
                                    duration_days=400,
                                    crew=[crew_member, crew_member2],
                                    mission_status="starting",
                                    budget_millions=355.10)
    except ValidationError as e:
        for error in e.errors():
            print(error["msg"])


if __name__ == "__main__":
    main()
