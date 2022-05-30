from .models import SubTag


def picture_board_context_processor(request):
    context = {'tags': SubTag.objects.all(), 'keyword': '', 'all': ''}

    all_tags = SubTag.objects.all()
    current_tag = None
    tags = {}
    for tag in all_tags:
        if tag.super_tag != current_tag:
            tags[tag.super_tag.name] = []
            current_tag = tag.super_tag
        tags[tag.super_tag.name].append(tag)

    context['tags_dict'] = tags

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            context['keyword'] = '?keyword=' + keyword
            context['all'] = context['keyword']
    if 'page' in request.GET:
        page = request.GET['page']
        if page != '1':
            if context['all']:
                context['all'] += '&page=' + page
            else:
                context['all'] = '?page=' + page
    return context
