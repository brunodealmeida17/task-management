from task_manager.settings import APP_URLS


def injecAppsContextProcessor(request):
   app_urls_filtered = {app_name: pages for app_name, pages in APP_URLS.items() if app_name in request.user.groups.values_list("name", flat=True)}
   return {'app_urls': app_urls_filtered}
