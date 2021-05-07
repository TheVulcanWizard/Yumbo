from datetime import datetime, date
from django.utils import timezone
from calendar import day_name
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import MealForm
from .models import *

@login_required
def schedule(request):
    def get_date(req_day):
        if req_day:
            year, month = (int(x) for x in req_day.split('-'))
            return date(year, month, day=1)
        return timezone.now()

    d = get_date(request.GET.get('day', None)).isocalendar()
    year, week = d[0], d[1]
    if d[2] == 7:
        week = week + 1
    final_week = date(year, 12, 31).isocalendar()[1]
    weeks = []
    for n in range(week-3, week+5):
        new_week = []
        if n > final_week:
            n = n - final_week
        if n==1:
            sunday = timezone.make_aware(datetime.fromisocalendar(year, final_week, 7))
            year = year + 1
        else:
            sunday = timezone.make_aware(datetime.fromisocalendar(year, n-1, 7))
        new_week.append(sunday)
        for i in range(1, 7):
            day = timezone.make_aware(datetime.fromisocalendar(year, n, i))
            new_week.append(day)
        weeks.append(new_week)

    meals = Meal.objects.filter(user=request.user, date__range=[weeks[0][0], weeks[-1][-1]])

    context = {
        "weeks": weeks,
        "meals": meals,
        "today": timezone.make_aware(datetime.fromisocalendar(d[0], d[1], d[2]))
    }

    return render(request, 'schedule/calendar.html', context)

@login_required
def add_meal(request, year, week, day):
    if request.method == 'POST':
        meal_form = MealForm(request.user, request.POST)
        if meal_form.is_valid():
            meal = meal_form.save(False)
            meal.user = request.user
            meal.date = timezone.make_aware(datetime.fromisocalendar(year, week, day))
            meal.save()
        return redirect('calendar')
    else:
        meal_form = MealForm(request.user)
    
    context = {
        'meal_form': meal_form,
    }
    return render(request, 'schedule/add_meal.html', context)