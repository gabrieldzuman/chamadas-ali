from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import CallRecord

class CallRecordTests(TestCase):

    def test_call_record_creation_start(self):
        record = CallRecord.objects.create(
            type="start",
            timestamp="2024-01-01T12:00:00Z",
            call_id="12345",
            source="12345678901",
            destination="10987654321"
        )
        self.assertEqual(record.type, "start")
        self.assertEqual(record.call_id, "12345")
        self.assertEqual(record.source, "12345678901")
        self.assertEqual(record.destination, "10987654321")

    def test_call_record_creation_end(self):
        record = CallRecord.objects.create(
            type="end",
            timestamp="2024-01-01T12:30:00Z",
            call_id="12345"
        )
        self.assertEqual(record.type, "end")
        self.assertEqual(record.call_id, "12345")

    def test_phone_number_format(self):
        valid_number = "12345678901" 
        invalid_number = "123456789" 

        record = CallRecord(
            type="start",
            timestamp="2024-01-01T12:00:00Z",
            call_id="12345",
            source=valid_number,
            destination="10987654321"
        )
        try:
            record.full_clean() 
        except ValidationError:
            self.fail("O formato do número de telefone válido foi rejeitado.")

        record_invalid = CallRecord(
            type="start",
            timestamp="2024-01-01T12:00:00Z",
            call_id="12345",
            source=invalid_number,
            destination="10987654321"
        )
        with self.assertRaises(ValidationError):
            record_invalid.full_clean()

    def test_call_record_pair(self):
        start_record = CallRecord.objects.create(
            type="start",
            timestamp="2024-01-01T12:00:00Z",
            call_id="12345",
            source="12345678901",
            destination="10987654321"
        )
        end_record = CallRecord.objects.create(
            type="end",
            timestamp="2024-01-01T12:30:00Z",
            call_id="12345"
        )

        self.assertEqual(start_record.call_id, end_record.call_id)
        self.assertNotEqual(start_record.type, end_record.type)
