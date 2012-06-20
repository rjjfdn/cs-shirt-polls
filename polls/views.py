from django.shortcuts import render_to_response, get_object_or_404
from polls.models import Student, Choice
from django.template import RequestContext

def vote(request):
    if not request.POST:
        return render_to_response('index.html', {}, context_instance=RequestContext(request))
    if request.POST['id_number'] == 'admin' and request.POST['last_name'] == 'rktamplayo':
        choices = Choice.objects.order_by('-votes')
        return render_to_response('results.html', {'choices': choices,}, context_instance=RequestContext(request))
    try:
        student = Student.objects.get(id_number=request.POST['id_number'], last_name=request.POST['last_name'])
    except Student.DoesNotExist:
        return render_to_response('index.html', {'error_message': "Student not found!"}, context_instance=RequestContext(request))
    except ValueError:
        return render_to_response('index.html', {'error_message': "Number only on ID Number"}, context_instance=RequestContext(request))
    choices = Choice.objects.all()
    if student.voted == 0:
        return render_to_response('vote.html', {'student': student, 'choices': choices}, context_instance=RequestContext(request))
    else:
        return render_to_response('index.html', {'error_message': "You've already voted!"}, context_instance=RequestContext(request))

def index(request):
    return render_to_response('index.html', {}, context_instance=RequestContext(request))

def voted(request, sid):
    if not request.POST:
        return render_to_response('index.html', {}, context_instance=RequestContext(request))
    if int(request.POST['choices']) == 0:
        student = get_object_or_404(Student, pk=sid)
        choices = Choice.objects.all()
        return render_to_response('vote.html', {'error_message': "Please vote first!", 'student': student, 'choices': choices}, context_instance=RequestContext(request))
    choice = Choice.objects.get(pk=request.POST['choices'])
    student = get_object_or_404(Student, pk=sid)
    student.voted = choice.choice_number
    student.save()
    choice.votes += 1
    choice.save()
    return render_to_response('index.html', {'error_message': "Thanks!"}, context_instance=RequestContext(request))
