from django.shortcuts import render, reverse



DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },

}
def home_view(request):
    pages = {
        'Список ингредиентов для омлета': reverse('omlet'),
        'Список ингредиентов для пасты': reverse('pasta'),
        'Список ингредиентов для бутерброда': reverse('buter')
    }

    context = {
        'pages': pages
    }
    return render(request, 'calculator/home.html', context)

def ingredient(request):
    servings = int(request.GET.get('servings', 1))
    ingredients = {}
    for keys in DATA.keys():
        if keys in request.path:
            ingredients = DATA.get(keys)

    for key in ingredients.keys():
        ingredients[key] = ingredients.get(key) * servings
    context = {
        'ingredients': ingredients,
         }
    return render(request, 'calculator/index.html', context)


# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
