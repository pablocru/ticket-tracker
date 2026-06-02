from dataclasses import fields

import pandas as pd

from app.integrations.service_now.story_dto import ServiceNowStoryDTO


class ServiceNowStoryMapper:
    def to_dtos(self, df: pd.DataFrame) -> list[ServiceNowStoryDTO]:
        self._validate_schema(df)

        dtos: list[ServiceNowStoryDTO] = []

        for row in df.to_dict(orient="records"):
            dto = ServiceNowStoryDTO(
                product=row["product"],
                number=row["number"],
                short_description=row["short_description"],
                assigned_to=row["assigned_to"],
                state=row["state"],
                opened_at=row["opened_at"],
            )
            dtos.append(dto)

        return dtos

    def _validate_schema(self, df: pd.DataFrame) -> None:
        expected = {f.name for f in fields(ServiceNowStoryDTO)}
        missing = expected - set(df.columns)

        if missing:
            raise ValueError(f"Missing columns: {', '.join(sorted(missing))}")
