from django.shortcuts import render, HttpResponse,redirect
from .models import TodoItem
from .models import Memory
from .forms import MemoryForm

# Create your views here.
def home(request):
    return render(request, "home.html")

def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos": items})


def memories(request):
    if request.method == 'POST':
        form = MemoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('memories')  # Redirect back to the memories page
    else:
        form = MemoryForm()

    memories = Memory.objects.all()  # Fetch all memories to display
    return render(request, 'memories.html', {'form': form, 'memories': memories})