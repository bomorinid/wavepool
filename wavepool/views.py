from django.template import loader
from django.http import HttpResponse

from wavepool.models import NewsPost
from wavepool.code_exercise_defs import code_exercise_defs


def front_page(request):
    """ View for the site's front page
        Returns all available newsposts, formatted like:
            cover_story: the newsposts with is_cover_story = True
            top_stories: the 3 most recent newsposts that are not cover story
            archive: the rest of the newsposts, sorted by most recent
    """
    template = loader.get_template('wavepool/frontpage.html')
    cover_story = None
    top_stories = []
    other_stories = []
    newsposts = NewsPost.objects.all().order_by('publish_date')

    i = 1
    for n in newsposts:
        if n.is_cover_story == True:
            cover_story = n
        if i < 3:
            top_stories.append(n)
            i = i + 1
        else:
            other_stories.append(n)

    context = {
        'cover_story': cover_story,
        'top_stories': top_stories,
        'archive': other_stories,
    }

    return HttpResponse(template.render(context, request))


def newspost(request):
    template = loader.get_template('wavepool/newspost.html')
    newspost = NewsPost.objects.all().order_by('?').first()
    context = {
        'newspost': newspost
    }

    return HttpResponse(template.render(context, request))


def instructions(request):
    template = loader.get_template('wavepool/instructions.html')
    context = {
        'code_exercise_defs': code_exercise_defs
    }
    return HttpResponse(template.render(context, request))