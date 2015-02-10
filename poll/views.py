from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from models import Participant,UserProfile


def index(request):
	return render(request,'poll/index.html',{})

@login_required
def vote(request):
	user = request.user
	user_profile,created = UserProfile.objects.get_or_create(user=user)

	if created:
		participants = Participant.objects.all()
		return render(request,'poll/vote.html',{'participants':participants,'user':user})
	if user_profile.voted():
		return render(request,'poll/thanks.html',{'user':user.username})
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

