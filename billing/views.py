from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.utils import timezone
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from .models import CallRecord
from .serializers import CallRecordSerializer
from django.db.models import Q
from collections import defaultdict
from decimal import Decimal

class CallRecordViewSet(viewsets.ModelViewSet):
    queryset = CallRecord.objects.all()
    serializer_class = CallRecordSerializer

    @action(detail=False, methods=['get'])
    def billing(self, request):
        phone_number = request.query_params.get('phone_number')
        period = request.query_params.get('period')

        if not phone_number:
            return Response({"error": "Número de telefone é obrigatório."}, status=400)

        if period:
            try:
                reference_date = datetime.strptime(period, "%Y-%m")
            except ValueError:
                return Response({"error": "Formato do período inválido. Use 'AAAA-MM'."}, status=400)
        else:
            today = timezone.now()
            reference_date = today.replace(day=1) - relativedelta(months=1)

        start_period = reference_date
        end_period = (reference_date + relativedelta(months=1)).replace(day=1)

        call_records = CallRecord.objects.filter(
            Q(source=phone_number) & 
            Q(type='end') & 
            Q(timestamp__gte=start_period) & 
            Q(timestamp__lt=end_period)
        ).select_related('source', 'destination')

        call_data = defaultdict(lambda: {"start": None, "end": None})
        for record in CallRecord.objects.filter(call_id__in=[call.call_id for call in call_records]):
            if record.type == "start":
                call_data[record.call_id]["start"] = record.timestamp
            elif record.type == "end":
                call_data[record.call_id]["end"] = record.timestamp

        total_amount = Decimal("0.00")
        call_details = []
        for call_id, timestamps in call_data.items():
            start_time = timestamps.get("start")
            end_time = timestamps.get("end")

            if start_time and end_time:
                duration = end_time - start_time
                duration_minutes = (duration.total_seconds() // 60)

                call_price = Decimal("0.36") 
                current_time = start_time
                while current_time < end_time:
                    if current_time.time() >= datetime.strptime("06:00", "%H:%M").time() and current_time.time() < datetime.strptime("22:00", "%H:%M").time():
                        call_price += Decimal("0.09") 
                    current_time += timedelta(minutes=1)

                call_details.append({
                    "destination": record.destination,
                    "start_date": start_time.date(),
                    "start_time": start_time.time(),
                    "duration": f"{int(duration.seconds // 3600)}h{int((duration.seconds % 3600) // 60)}m{int(duration.seconds % 60)}s",
                    "price": f"R$ {call_price:.2f}"
                })
                total_amount += call_price

        billing_data = {
            "phone_number": phone_number,
            "period": start_period.strftime("%Y-%m"),
            "total": f"R$ {total_amount:.2f}",
            "calls": call_details
        }
        return Response(billing_data)
