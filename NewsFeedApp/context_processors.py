from test1.models import user_preferences
from django.contrib.auth.models import User

def add_variable_to_context(request):
    try:
        a = user_preferences.objects.get(user = request.user)
        pref_1 = a.pref_1
        pref_2 = a.pref_2
        pref_3 = a.pref_3
    except:
        pref_1 = None
        pref_2 = None
        pref_3 = None

    return {
        'pref_1': pref_1,
        'pref_2': pref_2,
        'pref_3': pref_3
    }