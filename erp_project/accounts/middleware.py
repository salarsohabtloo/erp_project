from django.urls import reverse


class RedirectDashboardMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if request.user.is_authenticated:
            user_groups = request.user.groups.values_list('name', flat=True)

            if 'ceo' in user_groups:
                request.session['target_dashboard'] = reverse('ceo_dashboard')

            elif 'cto' in user_groups:
                request.session['target_dashboard'] = reverse('cto_dashboard')

            elif 'pm' in user_groups:
                request.session['target_dashboard'] = reverse('pm_dashboard')

        return response
