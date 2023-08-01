from django.shortcuts import render


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
    # можете добавить свои рецепты ;)
}


class RecipeView:
    model = ''

    @classmethod
    def setmodel(cls, model):
        cls.model = model
        return cls.model

    @classmethod
    def getmodel(cls):
        return cls.model


def home_view(request):
    template_name = 'calculator/home.html'
    return render(request, template_name)


def give_recipe(request):
    url = request.path.strip('/')
    RecipeView.setmodel(url)
    recipe = RecipeView.getmodel()
    if count := request.GET.get('servings', default=1):
        items = DATA.get(recipe, {})
        for i in items and items:
            try:
                items[i] *= int(count)
            except ValueError:
                print('Invalid value "count"')
            finally:
                count = 1
                items[i] *= int(count)
        context = {'recipe': items}
    return render(request, 'calculator/index.html', context)
