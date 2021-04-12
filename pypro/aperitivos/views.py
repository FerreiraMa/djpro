from django.shortcuts import render, get_object_or_404
from pypro.aperitivos.models import Video


"""
videos = [
    Video(slug='motivacao', titulo='Video Aperitivo: Motivação', vimeo_id=422595352),
    Video(slug='instalacao-windows', titulo='Instalação Windows', vimeo_id=251497668),
]


Lista com os vídeos mostrados no html, foi alterada para acessar de um objeto (Video) dentro do contexto de templates
videos = [
    {'slug': 'motivacao', 'titulo': 'Video Aperitivo: Motivação', 'vimeo_id': 422595352},
    {'slug': 'instalacao-windows', 'titulo': 'Instalação Windows', 'vimeo_id': 251497668},
]

videos_dct = {dct['slug']: dct for dct in videos}

videos_dct = {v.slug: v for v in videos}
"""


def indice(request):
    videos = Video.objects.order_by('creation').all()
    return render(request, 'aperitivos/indice.html', context={'videos': videos})


def video(request, slug):
    video = get_object_or_404(Video, slug=slug)
    return render(request, 'aperitivos/video.html', context={'video': video})


"""
Função utilizada para carregar os dados da lista videos_dct.
def video(request, slug):
    video = videos_dct[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})

Foi inserido o get_object_or_404 para casos onde o vídeo não é encontrado
def video(request, slug):
    video = Video.objects.get(slug=slug)
    return render(request, 'aperitivos/video.html', context={'video': video})
"""
