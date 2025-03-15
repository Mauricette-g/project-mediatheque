from django.contrib import admin
from .models import CD
from .models import Livre
from .models import Membre
from .models import DVD
from .models import Media
from .models import JeuDePlateau
from .models import Emprunt
# Register your models here.
admin.site.register(CD)
admin.site.register(Livre)
admin.site.register(Membre)
admin.site.register(DVD)
admin.site.register(JeuDePlateau)
admin.site.register(Emprunt)
#admin.site.register(Media)