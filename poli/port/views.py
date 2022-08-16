from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
import random
from .models import *


def magic_square(request):
    
    SIZE = 100
    STEP = 9
    arr_square = [0] * SIZE
    # arr_item = [0] * SIZE
    # set_endl = {9, 19, 29, 39, 49, 59, 69, 79, 89, 99}
    set_endl = {5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95}

    symbol = chr(random.randint(65, 122))

    for item in range(SIZE):
        arr_square[item] = chr(random.randint(65, 122))

    for item in range(0, 100, STEP):
        arr_square[item] = symbol

    # for item in range(SIZE):
    #     arr_item[item] = item

    context = {
        'title': 'Magic Square',
        # 'arr_item': arr_item,
        'arr_square': arr_square,
        'set_endl': set_endl,
        'symbol': symbol,

    }

    return render(request, 'port/magic_square.html', context=context)


def student_statistics(request):
    students = Students.objects.all()
    context = {
        'title': 'Student Statistics',
        'students': students,
    }
    return render(request, 'port/student_statistics.html', context=context)


def progress(request):
    students = Students.objects.all()
    for item in students:
        
        temp = list(map(int, item.math))
        item.math_score = sum(temp)/len(temp) * 100 / 5
        item.math_score = float('{:.2f}'.format(item.math_score))

        temp = list(map(int, item.physics))
        item.physics_score = sum(temp)/len(temp) * 100 / 5
        item.physics_score = float('{:.2f}'.format(item.physics_score))

        temp = list(map(int, item.history))
        item.history_score = sum(temp)/len(temp) * 100 / 5
        item.history_score = float('{:.2f}'.format(item.history_score))

        temp = list(map(int, item.biology))
        item.biology_score = sum(temp)/len(temp) * 100 / 5
        item.biology_score = float('{:.2f}'.format(item.biology_score))

        temp = list(map(int, item.geography))
        item.geography_score = sum(temp)/len(temp) * 100 / 5
        item.geography_score = float('{:.2f}'.format(item.geography_score))

        item.all_score = (item.math_score + item.physics_score + item.history_score + item.biology_score + item.geography_score) / 5
        item.all_score = float('{:.2f}'.format(item.all_score))




    context = {
        'title': 'Progress',
        'students': students,
    }
    return render(request, 'port/progress.html', context=context)


