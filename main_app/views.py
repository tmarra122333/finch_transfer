from django.shortcuts import render
from django.views.generic.base import TemplateView # <- View class to handle requests
from .models import Guitar
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
class Home(TemplateView):
    template_name = "home.html"
class About(TemplateView):
    template_name = "about.html"


class GuitarList(TemplateView):
    template_name = "guitar_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["guitars"] = Guitar.objects.filter(name__icontains=name)
            # We add a header context that includes the search param
            context["header"] = f"Searching for {name}"
        else:
            context["guitars"] = Guitar.objects.all()
            # default header for not searching 
            context["header"] = "Trending Guitars"
        return context

class GuitarCreate(CreateView):
    model = Guitar
    fields = ['name', 'img', 'bio', 'verified_guitar']
    template_name = "guitar_create.html"
    success_url = "/guitars/"

class GuitarDetail(DetailView):
    model = Guitar
    template_name = "guitar_detail.html"

class GuitarUpdate(UpdateView):
    model = Guitar
    fields = ['name', 'img', 'bio', 'verified_guitar']
    template_name = "guitar_update.html"
    success_url = "/guitars/"

class GuitarDelete(DeleteView):
    model = Guitar
    template_name = "guitar_delete_confirmation.html"
    success_url = "/guitars/"

# adds artist class for mock database data
# class Guitar:
#     def __init__(self, name, image, bio):
#         self.name = name
#         self.image = image
#         self.bio = bio


# guitars = [
# Guitar("Taylor 214 Ce", 
# "https://media.guitarcenter.com/is/image/MMGS7/L69529000001000-00-1600x1600.jpg", "This guitar is as sweet as pie"),

# Guitar("Taylor K24 Ce",
# "https://i.ebayimg.com/images/g/7fYAAOSwq19XBhvo/s-l600.jpg", "Koa wood, hawaiin wood only harvestable upon natural fall."),

# Guitar("Gibson Hummingbird", 
# "https://max.guitars/media/catalog/product/cache/72269915de88ed6ece6209277c94ce43/m/a/maxguitar_art-12675_gibson_hummingbird-1.jpg", "This guitar is equivalent to the Sweet Nectar of Honey."),

# Guitar("Washburn D100 Dreadnought",
# "https://upload.wikimedia.org/wikipedia/commons/d/d1/Washburn_D100DL.jpg", "BloodMoney Tunes."),

# Guitar("Martin D28",
# "https://www.martinguitar.com/on/demandware.static/-/Sites-martin-master-catalog/default/dw77e28aa4/images/D-28/D-28_f.jpg", "I used to love when Neil Young played me, now I hate him."),

# Guitar("Ovation Celebrity",
# "https://media.sweetwater.com/api/i/q-82__ha-b8038e96949a29b7__hmac-cd8ead02e09c02602c236ea52c175ddd951e4a83/images/items/750/CE48PRG-large.jpg", "Come play me."),
# ]


#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["guitars"] = guitars # this is where we add the key into our context object for the view to use
#         return context