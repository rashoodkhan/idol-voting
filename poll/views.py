from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from models import Participant,UserProfile
from django.views.decorators.csrf import csrf_exempt

def index(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/vote')
	return render(request,'poll/index.html',{})

@login_required
def vote(request):
	user = request.user
	user_profile,created = UserProfile.objects.get_or_create(user=user)

	if created:
		participants = Participant.objects.all()
		return render(request,'poll/vote.html',{'participants':participants,'user':user.first_name})
	if user_profile.voted():
		return render(request,'poll/thanks.html',{'user':user.first_name})
	elif request.method == 'POST':
		checked = request.POST.getlist('checked')
		for id in checked:
			participant = Participant.objects.all().filter(id=id)[0]
			current_vote = int(participant.vote_count)
			participant.vote_count = current_vote+1
			participant.save()
		user_profile.has_voted = True
		user_profile.save()
		return render(request,'poll/thanks.html',{'user':user.username})
	else:
		participants = Participant.objects.all()
		return render(request,'poll/vote.html',{'participants':participants,'user':user})

@csrf_exempt
def authentication(request):
	if request.method == 'POST':
		email = request.POST['inputEmail']
		name = request.POST['inputName']

		user,created = User.objects.get_or_create(username=email)

		if created:
			user.first_name = name
			user.set_password('F!V35')
			user.email = email
			user.save()

		user.backend = 'django.contrib.auth.backends.ModelBackend'
		user_new = authenticate(username=email,password='F!V35')

		if user_new is not None:
			login(request,user_new)

		return HttpResponseRedirect('/vote')
	else:
		return render(request,'poll/index.html',{'error':'There has been some error in logging you in.'})

def results(request):
	participants = Participant.objects.order_by('-vote_count')
	return render(request,'poll/result.html',{'participants':participants})


