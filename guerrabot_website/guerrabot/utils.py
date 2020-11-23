from django.http import HttpResponse
def read_file(request):
    print(request)
    import pathlib
    f = open('./guerrabot/static/TEMP_saves/state_'+request.GET.get("state")+'.geojson', 'r')
    file_content = f.read()
    f.close()
    return HttpResponse(file_content, content_type="text/plain")