from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Post


@receiver(post_save, sender=Post)
def product_created(instance, created, **kwargs):
    if not created:
        return

    emails = User.objects.filter(
        subscriptions__category=instance.post_category
    ).values_list('email', flat=True)

    subject = f'Новый пост в подсайте {instance.post_category}'

    text_content = (
        f'Заголовок: {instance.title}\n'
        f': {instance.text}\n\n'
        f'Ссылка на товар: http://127.0.0.1{instance.get_absolute_url()}'
    )
    html_content = (
        f'Заголовок: {instance.title}<br>'
        f': {instance.text}<br><br>'
        f'<a href="http://127.0.0.1{instance.get_absolute_url()}">'
        f'Ссылка на товар</a>'
    )
    for email in emails:
        msg = EmailMultiAlternatives(subject, text_content, None, [email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()