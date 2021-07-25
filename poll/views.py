from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Poll
from .forms import CreatePollForm


# Create your views here.
def Home(request):
    polls   = Poll.objects.all()
    context = {
                'polls' : polls,
    }
    return render(request,'poll/home.html',context)

def Create(request):
    form    = CreatePollForm()
    if request.method == 'POST':
        form    = CreatePollForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data['question'])
            form.save()
            return redirect('home')
            
    context = {
                'form' : form
    }
    return render(request,'poll/create.html',context)

def Vote(request,pk):
    poll    = Poll.objects.get(id=pk)
    if request.method == 'POST':

        if request.POST['poll'] == 'option1':
            poll.option_one_count  += 1
            
        elif request.POST['poll'] == 'option2':
            poll.option_two_count  += 1
            
        elif request.POST['poll'] == 'option3':
            poll.option_three_count  += 1
        else:
            return HttpResponse(400, 'Invalid form')
        
        poll.save()
        return redirect('result',poll.id)
        
    context = {
                'poll' : poll
    }
    
    return render(request,'poll/vote.html',context)
    

def Result(request,pk):
    poll = Poll.objects.get(id=pk)
    total = poll.option_one_count + poll.option_two_count + poll.option_three_count
    print("total is ",total)
    context = {'poll' : poll,
               'total' : total}
    return render(request,'poll/result.html',context)