from datetime import datetime
import re

CALL_TYPE_CHOICES = {
    'start': 'Início da Chamada',
    'end': 'Fim da Chamada'
}

PHONE_REGEX = r'^\d{2}\d{8,9}$'
PHONE_VALIDATION_MESSAGE = (
    "O número de telefone deve estar no formato AAXXXXXXXXX, onde AA é o código "
    "de área e XXXXXXXXX é o número de telefone de 8 ou 9 dígitos."
)

class CallRecordDTO:
    def __init__(self, type: str, timestamp: datetime, call_id: str, source: str = None, destination: str = None):
        self.type = type
        self.timestamp = timestamp
        self.call_id = call_id
        self.source = source
        self.destination = destination

        self.validate()

    def validate(self):
        if self.type not in CALL_TYPE_CHOICES:
            raise ValueError("Tipo de chamada inválido. Escolha entre 'start' ou 'end'.")

        if not isinstance(self.timestamp, datetime):
            raise ValueError("Timestamp deve ser uma instância de datetime.")

        if not self.call_id:
            raise ValueError("call_id não pode estar vazio.")

        if self.source and not re.match(PHONE_REGEX, self.source):
            raise ValueError(f"Source inválido. {PHONE_VALIDATION_MESSAGE}")

        if self.destination and not re.match(PHONE_REGEX, self.destination):
            raise ValueError(f"Destination inválido. {PHONE_VALIDATION_MESSAGE}")

    def __str__(self):
        return f"CallRecord {self.call_id} ({CALL_TYPE_CHOICES.get(self.type, 'Unknown')})"
