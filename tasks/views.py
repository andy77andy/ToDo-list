from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic, View

from tasks.models import Tag, Task


class TagListView(generic.ListView):
    model = Tag
    queryset = Tag.objects.all()
    template_name = "tasks/tag_list.html"
    context_object_name = "tag_list"


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tasks:tag-list")
    template_name = "tasks/tag_form.html"


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tasks:tag-list")
    template_name = "tasks/tag_form.html"


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("tasks:tag-list")
    template_name = "tasks/task_confirm_delete.html"


class TaskListView(generic.ListView):
    model = Task
    template_name = "tasks/task_list.html"
    context_object_name = "task_list"


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasks:index")
    template_name = "tasks/task_form.html"


class TaskUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tasks:index")
    template_name = "tasks/tag_form.html"


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("tasks:index")
    template_name = "tasks/task_confirm_delete.html"


class TaskStatusUpdateView(View):
    @staticmethod
    def post(request, pk):
        task = Task.objects.get(id=pk)
        task.is_done = not task.is_done
        task.save()

        return redirect(reverse("tasks:index"))
