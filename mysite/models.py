class Language(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False)
    language_name = models.TextField()
    language_code = models.CharField(max_length=10)
