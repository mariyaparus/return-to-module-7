from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from materials.models import Material


# Create your views here.
class MaterialCreateView(CreateView):
    model = Material
    fields = ('title', 'body',)
    success_url = reverse_lazy('materials:list')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'title': 'Создание материала'})
        return context


class MaterialUpdateView(UpdateView):
    model = Material
    fields = ('title', 'body',)
    # success_url = reverse_lazy('materials:list')

    def form_valid(self, form):
        """
        Динамически формировать slug
        """
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()

        return super().form_valid(form)

    def get_success_url(self):
        """
        После успешного редактирования перенаправляет на просмотр материала
        """
        return reverse('materials:view', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'title': 'Редактирование материала'})
        return context


class MaterialListView(ListView):
    model = Material

    def get_queryset(self, *args, **kwargs):
        """
        Выводить только опубликованные материалы
        """
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'title': 'Материалы'})
        return context


class MaterialDetailView(DetailView):
    model = Material

    def get_object(self, queryset=None):
        """
        Счетчик просмотров
        """
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()

        return self.object

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'title': 'Материал'})
        return context


class MaterialDeleteView(DeleteView):
    model = Material
    success_url = reverse_lazy('materials:list')
