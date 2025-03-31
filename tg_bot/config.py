import json
from pathlib import Path
from typing import List, Union
from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    BOT_TOKEN: str
    ADMIN_IDS: list[int]
    FRONT_SITE: str
    BACK_SITE: str
    model_config = SettingsConfigDict(
        env_file=Path(__file__).resolve().parent.parent / "infra/.env.dev",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    @field_validator("ADMIN_IDS", mode="before")
    @classmethod
    def parse_json_ids(cls, v: Union[str, List[int]]) -> List[int]:
        if isinstance(v, str):
            try:
                return json.loads(v)
            except json.JSONDecodeError:
                return [int(x.strip()) for x in v.strip("[]").split(",")]
        return v


settings = Settings()

if __name__ == "__main__":
    print(settings.model_dump())
