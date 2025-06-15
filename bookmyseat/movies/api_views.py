from django.http import JsonResponse
from .models import Seat, Theater

def available_seats(request, theater_id):
    theater = Theater.objects.get(id=theater_id)
    seats = Seat.objects.filter(theater=theater, is_booked=False, is_seat_reserved=False)
    seat_data = [{"id": seat.id, "number": seat.seat_number} for seat in seats]
    return JsonResponse({"available_seats":seat_data})