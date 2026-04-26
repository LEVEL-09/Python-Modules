from pydantic import BaseModel, Field, model_validator, ValidationError
from typing_extensions import Self
from typing import Optional
from enum import Enum
from datetime import datetime
from pydantic_core import PydanticCustomError


class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


# This model represents an alien contact report with various
# fields and custom validation rules.
class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime = Field(...)
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType = Field(...)
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=0, le=100)
    message_received: Optional[str] = Field(max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode="after")
    def custom_validation(self) -> Self:
        if not self.contact_id.startswith("AC"):
            raise PydanticCustomError("ID error",
                                      "Contact ID must start with \"AC\"")
        elif (self.contact_type == ContactType.PHYSICAL
              and not self.is_verified):
            raise PydanticCustomError("Physical error",
                                      "Physical contact reports must be "
                                      "verified")
        elif (self.contact_type == ContactType.TELEPATHIC
              and self.witness_count < 3):
            raise PydanticCustomError("Telepathic error",
                                      "Telepathic contact requires at "
                                      "least 3 witnesses")
        elif self.signal_strength > 7.0 and not self.message_received:
            raise PydanticCustomError("Strong signals error",
                                      "Strong signals (> 7.0) should "
                                      "include received messages")
        return self


# This function demonstrates the creation
# of valid and invalid alien contact reports,
# showing how the custom validation rules work in practice.
def main() -> None:
    print("Alien Contact Log Validation")
    try:
        print("======================================")
        contact_alien = AlienContact(contact_id="AC-chabl3rbi",
                                     timestamp=datetime.now(),
                                     location="1337",
                                     contact_type=ContactType.RADIO,
                                     signal_strength=7.12,
                                     duration_minutes=45, witness_count=99,
                                     message_received="bobo boo bo",
                                     is_verified=True)
        print("Valid contact report:")
        print("ID:", contact_alien.contact_id)
        print("Type:", contact_alien.contact_type.value)
        print("Location:", contact_alien.location)
        print("Signal: ", contact_alien.signal_strength, "/10", sep="")
        print("Duration:", contact_alien.duration_minutes, "minutes")
        print("Witnesses:", contact_alien.witness_count)
        print("Message:", contact_alien.message_received)

        print("\n======================================")
        print("Expected validation error:")
        contact_alien = AlienContact(contact_id="AC-chabl3rbi",
                                     timestamp=datetime.now(),
                                     location="1337",
                                     contact_type=ContactType.TELEPATHIC,
                                     signal_strength=7.12,
                                     duration_minutes=45, witness_count=2,
                                     message_received="bobo boo bo",
                                     is_verified=True)
    except ValidationError as e:
        for error in e.errors():
            print(error["msg"])


if __name__ == "__main__":
    main()
