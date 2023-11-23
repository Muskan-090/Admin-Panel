from django.shortcuts import render
from .forms import NewUserProfileForm
from django.http import HttpResponse
from django.shortcuts import redirect


# user_profiles/views.py
from django.shortcuts import render, get_object_or_404
from .models import UserProfile

def user_list(request):
    users = UserProfile.objects.all()

    form = SearchForm(request.GET or None)
    if request.method == 'GET' and form.is_valid():
        search_term = form.cleaned_data['search_term']
        users = UserProfile.objects.filter(name__icontains=search_term)
        return render(request, 'user_profiles/search_users.html', {'form': form, 'users': users})
    
    return render(request, 'user_profiles/user_list.html', {'users': users,'form': form})

from . Area_interest import nlp_area_of_interest
import re
def user_detail(request, user_id):
    user = get_object_or_404(UserProfile, pk=user_id)
    about = user.about 
    areas_of_interest = nlp_area_of_interest(about)
    # user.areas_of_interest = areas_of_interest
    # user.save()
    input_string = user.areas_of_interest
    match = re.match(r'\[(.*?)\]', input_string)
    result = match.group(1).strip("'") 
    user.areas_of_interest = result.split(',')
    return render(request, 'user_profiles/user_detail.html', {'user': user})


def create_profile(request):
    if request.method == 'POST':
        form = NewUserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            # Create a new user profile associated with the current user
            new_profile = form.save()
            new_profile.user = request.user
            new_profile.save()

            return redirect('/users/', user_id=request.user.id)
    else:
        form = NewUserProfileForm()
        return render(request, 'user_profiles/create_profile.html', {'form': form})


def delete_profile(request,user_id):
    # Retrieve the user profile associated with the current user
    user_profile = get_object_or_404(UserProfile, pk =user_id )
    print(user_profile)
    if request.method == 'POST':
        # Confirm deletion (you can add additional logic here)
        user_profile.delete()
        return HttpResponse("User deleted")
    else:
        return render(request, 'user_profiles/user_detail.html', {'user_profile': user_profile})
    


from .forms import SearchForm

def search_users(request):
    form = SearchForm(request.GET or None)

    if request.method == 'GET' and form.is_valid():
        search_term = form.cleaned_data['search_term']
        users = UserProfile.objects.filter(name__icontains=search_term)
    else:
        users = UserProfile.objects.all()

        return render(request, 'user_profiles/search_users.html', {'form': form, 'users': users})

