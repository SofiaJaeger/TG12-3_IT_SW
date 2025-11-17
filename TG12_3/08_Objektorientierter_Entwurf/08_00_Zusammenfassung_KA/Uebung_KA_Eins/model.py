from pydantic import BaseModel, Field, field_validator, ValidationError

class Auto(BaseModel):
    Marke: str = Field(default="", min_length=1, max_length=10)
    Modell: str = Field(default="", min_length=1, max_length=10)
    PS: int = Field(default=10, ge=20, lt=500)
    Verbrauch: int = Field(default=10, ge=20, lt=500)

model_config = {"validate_assignment": True}