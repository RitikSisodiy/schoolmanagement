from schoolmain.models import schoolifo
def alltimefunc(request):
    info = schoolifo.objects.all()[0]
    return {'schoolinfo':info}