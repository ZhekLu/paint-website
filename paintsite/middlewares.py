from .models import SubTag


def picture_board_context_processor(request):
    context = {'tags': SubTag.objects.all()}
    return context
