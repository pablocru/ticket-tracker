from dataclasses import dataclass


@dataclass(slots=True)
class ServiceNowStoryDTO:
    product: str
    number: str
    short_description: str
    assigned_to: str
    state: str
    opened_at: str
