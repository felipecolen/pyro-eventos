from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models

from app_evento.functions import gerar_codigo_alfanumerico, obter_extensao_arquivo
from app_evento.models.choices import ESTADOS, SEXO


class Participante(User):
    nome_cracha = models.CharField('Nome pro Crachá', max_length=20)
    data_nascimento = models.DateField('Data de Nascimento', null=True, blank=True)
    sexo = models.CharField('Sexo', max_length=1, choices=SEXO, null=True, blank=True)
    telegram = models.CharField('Telegram', max_length=15, null=True, blank=True, help_text='Username ou número')
    whatsapp = models.CharField('Whatsapp', max_length=15, null=True, blank=True)

    cidade = models.CharField('Cidade', max_length=50, null=True, blank=True)
    estado = models.CharField('Estado', max_length=2, choices=ESTADOS, default='RO')

    # cpf = models.CharField('CPF', max_length=11, unique=True)
    # rg = models.CharField('RG', max_length=30, )
    # rg_emissor = models.CharField('Emissor', max_length=10, )
    # rg_emissor_uf = models.ForeignKey(Estado, verbose_name='UF')
    # instituicao = models.CharField('Instituição', max_length=100, null=True, blank=True)
    # cidade_uf = models.ForeignKey(Cidade, verbose_name='Cidade/UF', null=True, blank=True)

    def path_img(self, filename):
        return '{}/{}{}{}'.format('participantes', self.username, gerar_codigo_alfanumerico(3),
                                  obter_extensao_arquivo(filename))

    def valida_size_img(obj_foto):
        tam = obj_foto.img.size
        tam_max = 1.0 * 1024 * 1024
        if tam > tam_max:
            raise ValidationError(f'Imagem muito grande ({tam/1000/1000:10.2f}mb),  '
                                  f' o máx. permitido é {tam_max/1024/1024:10.2f}mb')

    img = models.ImageField('Foto', upload_to=path_img, null=True, blank=True, validators=[valida_size_img])

    def mostra_minuatura_img(self):
        return f"""
            <img src="{self.tem_img()}" width="30px" heigth="30px" class="materialboxed" />
               """
    mostra_minuatura_img.allow_tags = True
    mostra_minuatura_img.short_description = 'Imagem'

    def tem_img(self):
        return self.img.url if self.img else '/static/imgs/user_sem_img.png'

    def __str__(self):
        return f'{self.username} - {self.get_full_name()}'

    class Meta:
        ordering = ['first_name', 'last_name']
        verbose_name = 'Participante'
        verbose_name_plural = 'Participantes'
