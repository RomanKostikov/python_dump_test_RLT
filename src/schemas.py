from datetime import datetime

from pydantic import BaseModel


class InputDatasSchema(BaseModel):
    dt_from: datetime
    dt_upto: datetime
    group_type: str

    def __str__(self):
        return (
                f"dt_from: {self.dt_from}\n" +
                f"dt_upto: {self.dt_upto}\n" +
                f"group_type: {self.group_type}"
        )


class OutputDatasSchema(BaseModel):
    dataset: list[int]
    labels: list[str]

    def __str__(self):
        labels_str = ', '.join([label for label in self.labels])
        return (
                '{' +
                '"dataset": ' + self.dataset.__str__() + ', ' +
                '"labels": [' + labels_str + ']' +
                '}'
        )

