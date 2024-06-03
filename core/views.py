from django.views.generic import FormView
from django.urls import reverse_lazy
from .models import Servico, Funcionario, Recurso
from .forms import ContatoForm
from django.contrib import messages


class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        pesq_recurso = list(Recurso.objects.order_by('?').all())
        qtd = (len(pesq_recurso) / 2)
        recursos_direita = []
        recursos_esquerda = []

        for i in range(len(pesq_recurso)):
            if qtd % 2 == 1:
                if i <= qtd:
                    recursos_esquerda.append(pesq_recurso[i])
                else:
                    recursos_direita.append(pesq_recurso[i])

            else:
                if i < qtd:
                    recursos_esquerda.append(pesq_recurso[i])
                else:
                    recursos_direita.append(pesq_recurso[i])

        context = super(IndexView, self).get_context_data(**kwargs)
        context['servicos'] = Servico.objects.order_by('?').all()
        context['funcionarios'] = Funcionario.objects.order_by('?').all()
        context['recursos_direita'] = recursos_direita
        context['recursos_esquerda'] = recursos_esquerda
        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'Email enviado com sucesso.')
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao enviar e-mail.')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)

