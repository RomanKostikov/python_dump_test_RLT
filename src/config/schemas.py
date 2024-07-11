from dataclasses import dataclass


@dataclass
class DBSettings:
    db_connection_string: str
    db_name: str


@dataclass
class BotSettings:
    token: str
