from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile


# Create your views here.

class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = "target_profile"
    form_class = ProfileCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'profileapp/create.html'

    def form_valid(self, form):
        # 커스터마이징 하고자 하는 내용 넣는 자리
        # 임시 데이터임
        temp_profile = form.save(commit=False)
        # 요청을 보낸 user 저장
        temp_profile.user = self.request.user
        temp_profile.save()
        return super().form_valid(form)

