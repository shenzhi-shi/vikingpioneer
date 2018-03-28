from django.shortcuts import redirect
from django.views.generic import TemplateView
from vikinglab.forms import SimpleForm
from vikinglab.models import SomeOne

class HomePage(TemplateView):
    template_name = 'home.html'

class Pioneer(TemplateView):
    template_name = 'introduction.html'

    def get_context_data(self, user_id, **kwargs):
         context = super(Pioneer, self).get_context_data(**kwargs)
         try:
            context['name'] = SomeOne.objects.get(id=user_id).firstname if user_id else 'stranger'
         except SomeOne.DoesNotExist:
            context['name'] = 'hacker'
         return context

class SomeOneView(TemplateView):
    template_name = 'form.html'

    def post(self, request):
        formset = SimpleForm(request.POST)
        if formset.is_valid():
           user = formset.save()
           return redirect('viking_pioneer_with_id', user_id=user.id, message="Successful Submission!")
        return self.get(request, errors='There were errors!')

    def get_context_data(self, **kwargs):
        context = super(SomeOneView, self).get_context_data(**kwargs)
        context['someone_form'] = SimpleForm
        isViking = self.request.GET.get('viking', 'true')
        context['isViking'] = isViking
        return context


