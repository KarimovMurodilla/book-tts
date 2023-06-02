import io
import fitz

from django.db import models
from django.urls import reverse
from django.core.files import File

from users.models import CustomUser
from .utils import Muxlisa


class Book(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    book = models.FileField(upload_to='books/')
    pdf_text = models.TextField(blank=True)

    def get_absolute_url(self):
        return reverse('result', args=[str(self.id)])

    def process_pdf(self):
        if self.pdf_text:
            return

        with fitz.open(self.book.file) as doc:
            text = ''
            for page in doc:
                text += page.getText()

        # сохранить извлеченный текст в модели
        self.pdf_text = text
        self.save()

        return self.pdf_text

    def process_audio(self):
        m = Muxlisa()
        all_text = self.pdf_text.split('.')
        index = 5 if len(all_text) > 5 else -1
        for num, text in enumerate(all_text[:index]):
            audio_bytes = m.text_to_speech(text)
            audio_file = io.BytesIO(audio_bytes)
            audio_name = f"{self.book.name[6:]}_{num}.mp3"
            audio_file = (audio_name, audio_file)
            a = Audio(book=self, text=text)
            a.audio.save(*audio_file)
            a.save()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.process_pdf()
        self.process_audio()


class Audio(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    text = models.TextField(max_length=500)
    audio = models.FileField(upload_to='audios/')
