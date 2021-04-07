from django.shortcuts import render
from django.urls import reverse


class Video:
    def __init__(self, slug, titulo, vimeo_id):
        self.slug = slug
        self.titulo = titulo
        self.vimeo_id = vimeo_id

    def get_absolute_url(self):
        return reverse('aperitivos:video', args=(self.slug,))


videos = [
    Video('motivacao', 'Video Aperitivo: Motivação',  422595352),
    Video('instalacao-windows', 'Instalação Windows', 251497668),
]

"""
Lista com os vídeos mostrados no html, foi alterada para acessar de um objeto (Video) dentro do contexto de templates
videos = [
    {'slug': 'motivacao', 'titulo': 'Video Aperitivo: Motivação', 'vimeo_id': 422595352},
    {'slug': 'instalacao-windows', 'titulo': 'Instalação Windows', 'vimeo_id': 251497668},
]

videos_dct = {dct['slug']: dct for dct in videos}
"""

videos_dct = {v.slug: v for v in videos}


def indice(request):
    return render(request, 'aperitivos/indice.html', context={'videos': videos})


def video(request, slug):
    video = videos_dct[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
