from django.shortcuts import render
from django.http import HttpResponse
from lifelines import KaplanMeierFitter
from lifelines.plotting import plot_lifetimes
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import pandas as pd





# Create your views here.
def survival_analysis_graphic():
    # Оновлені тестові дані для демонстрації збільшення ймовірності поломки
    duration = np.array([2, 3, 4, 5, 6, 7])  # Час до поломки (дні)
    event_observed = np.array([1, 1, 1, 1, 1, 1])  # Поломка сталася

    # Створюємо об'єкт KaplanMeierFitter і фітуємо дані
    kmf = KaplanMeierFitter()
    kmf.fit(duration, event_observed)

    # Створюємо графік
    plt.figure(figsize=(10, 4))
    kmf.plot_survival_function()
    plt.title('Функція виживання при проблемах з інтернет-мережею')
    plt.ylabel('Ймовірність коректної роботи')
    plt.xlabel('Час (дні)')

    # Зберігаємо та конвертуємо графік
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')

    return graphic

def time_series_analysis():
    # Створюємо DataFrame з тестовими даними
    data = {
        'date': pd.date_range(start='2023-01-01', periods=7, freq='D'),
        'issues': [2, 3, 5, 4, 6, 8, 5]
    }
    df = pd.DataFrame(data)

    # Встановлюємо колонку дати як індекс DataFrame
    df.set_index('date', inplace=True)

    # Створюємо графік часових рядів
    plt.figure(figsize=(10, 4))
    plt.plot(df.index, df['issues'], marker='o', linestyle='-', color='b')
    plt.title('Аналіз часових рядів мережевих проблем')
    plt.xlabel('Дата')
    plt.ylabel('Кількість заяв')
    plt.grid(True)

    # Зберігаємо графік в PNG та конвертуємо в base64 для передачі у HTML
    buffer = BytesIO()
    plt.savefig(buffer, format='png', dpi=100)
    plt.close()
    buffer.seek(0)
    image_png = buffer.getvalue()
    graphic = base64.b64encode(image_png).decode('utf-8')

    return graphic
def index(request):
    return render(request, 'main/index.html')

def Time_series(request):
    graphic = time_series_analysis()
    context = {'graphic': graphic}
    return render(request, 'main/Time_series.html', context)

def Survival_analysis(request):
    graphic = survival_analysis_graphic()
    context = {'graphic': graphic}
    return render(request, 'main/Survival_analysis.html', context)

