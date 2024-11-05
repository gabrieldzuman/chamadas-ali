from django.db import models
from django.core.validators import RegexValidator

class CallRecord(models.Model):
    CALL_TYPE_CHOICES = [
        ('start', 'Início da Chamada'),
        ('end', 'Fim da Chamada')
    ]

    type = models.CharField(
        max_length=5,
        choices=CALL_TYPE_CHOICES,
        help_text="Indica se é um registro de início ou fim de chamada."
    )
    timestamp = models.DateTimeField(
        help_text="O timestamp de quando o evento ocorreu."
    )
    call_id = models.CharField(
        max_length=20,
        help_text="Identificador único para cada par de registros de chamada."
    )
    source = models.CharField(
        max_length=11,
        validators=[
            RegexValidator(
                regex=r'^\d{2}\d{8,9}$',
                message="O número de telefone de origem deve estar no formato AAXXXXXXXXX, onde AA é o código de área e XXXXXXXXX é o número de telefone de 8 ou 9 dígitos."
            )
        ],
        blank=True, null=True,
        help_text="Número de telefone do assinante que originou a chamada (somente no registro de início)."
    )
    destination = models.CharField(
        max_length=11,
        validators=[
            RegexValidator(
                regex=r'^\d{2}\d{8,9}$',
                message="O número de telefone de destino deve estar no formato AAXXXXXXXXX, onde AA é o código de área e XXXXXXXXX é o número de telefone de 8 ou 9 dígitos."
            )
        ],
        blank=True, null=True,
        help_text="Número de telefone que está recebendo a chamada (somente no registro de início)."
    )

    def __str__(self):
        return f"CallRecord {self.call_id} ({self.get_type_display()})"

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['call_id', 'type'], name='unique_call_record')
        ]
        ordering = ['timestamp']
        verbose_name = "Registro de Chamada"
        verbose_name_plural = "Registros de Chamadas"
