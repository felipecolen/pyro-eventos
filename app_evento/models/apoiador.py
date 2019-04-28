from django.db import models

from app_evento.functions import gerar_codigo_alfanumerico, obter_extensao_arquivo


class Apoiador(models.Model):

    def local_logo(self, filename):
        return '{}/{}_{}{}'.format('apoiadores', self.id, gerar_codigo_alfanumerico(6), obter_extensao_arquivo(filename))

    nome = models.CharField('Nome', max_length=100)
    link = models.CharField('Link', max_length=200, null=True, blank=True, default='http://',
                            help_text='Inclua o http:// antes do www')
    logo = models.ImageField('Logo', upload_to=local_logo)

    def mostrar_miniatura(self):
        return f"<img src='{self.logo.url}' width='30px' heigth='30px' class='materialboxed' />"
    mostrar_miniatura.allow_tags = True
    mostrar_miniatura.short_description = 'Logo'

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']
        verbose_name = 'Apoiador(a)'
        verbose_name_plural = 'Apoiadorxs'
