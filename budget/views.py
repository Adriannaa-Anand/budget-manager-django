from django.shortcuts import render, get_object_or_404, redirect
from .models import Budget, Category
from .forms import BudgetForm

def budget_list(request):
    budgets = Budget.objects.all()
    return render(request, 'budget_list.html', {'budgets': budgets})

def budget_detail(request, pk):
    budget = get_object_or_404(Budget, pk=pk)
    return render(request, 'budget_detail.html', {'budget': budget})

def budget_create(request):
    if request.method == 'POST':
        form = BudgetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('budget_list')
    else:
        form = BudgetForm()
    return render(request, 'budget_form.html', {'form': form})

def budget_update(request, pk):
    budget = get_object_or_404(Budget, pk=pk)
    if request.method == 'POST':
        form = BudgetForm(request.POST, instance=budget)
        if form.is_valid():
            form.save()
            return redirect('budget_detail', pk=budget.pk)
    else:
        form = BudgetForm(instance=budget)
    return render(request, 'budget_form.html', {'form': form})
def budget_delete(request, pk):
    budget = get_object_or_404(Budget, pk=pk)
    if request.method == 'POST':
        budget.delete()
        return redirect('budget_list')
    return render(request, 'budget_confirm_delete.html', {'budget': budget})

