from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from .forms import NoteForm
from django.db.models import Q

# Create your views here.

def note_list(request):
    category = request.GET.get('category')
    query = request.GET.get('search')

    notes = Note.objects.all()

    if category:
        notes = notes.filter(category=category)

    if query:
        notes = notes.filter(title__icontains=query)

    return render(request, 'notes.html', {'notes': notes})

def note_create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm()
    return render(request, 'note_form.html', {'form': form})

def note_edit(request, pk):
    note = get_object_or_404(Note, pk=pk)
    form = NoteForm(request.POST or None, instance=note)
    if form.is_valid():
        form.save()
        return redirect('note_list')
    return render(request, 'note_form.html', {'form': form})

def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)
    note.delete()
    return redirect('note_list')
