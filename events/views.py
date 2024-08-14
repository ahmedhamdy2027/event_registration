from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Event, Registration
from .forms import RegistrationForm

def event_list(request):
    events = Event.objects.all()
    
    # Grouping events into pairs
    paired_events = [events[i:i + 2] for i in range(0, len(events), 2)]

    return render(request, 'events/event_list.html', {'paired_events': paired_events})

def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'events/event_detail.html', {'event': event})

def register_for_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            registration = form.save(commit=False)
            registration.event = event
            registration.user = request.user  # Ensure the user is set
            registration.save()
            messages.success(request, 'You have successfully registered for the event!')
            return redirect('event_detail', event_id=event.id)
    else:
        form = RegistrationForm()

    return render(request, 'events/register_for_event.html', {'event': event, 'form': form})