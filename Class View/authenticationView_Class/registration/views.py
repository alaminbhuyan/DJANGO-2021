from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.
## comment: This is the third way
@method_decorator(decorator=login_required, name='dispatch')
class ProfileTemplateView(TemplateView):
    template_name = 'registration/profile.html'

    # ## comment:  The second way
    # @method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)

## comment: This is the third way
@method_decorator(decorator=login_required, name='dispatch')
class AboutTemplateView(TemplateView):
    template_name = 'registration/about.html'

    # ## comment:  The second way
    # @method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)


## comment: This is the third way
@method_decorator(decorator=staff_member_required, name='dispatch')
class ConfidentialTemplateView(TemplateView):
    template_name = 'registration/confidential.html'

    # ## comment:  The second way
    # @method_decorator(staff_member_required)
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)