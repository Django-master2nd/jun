from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["username"] = "横山順"
        return ctxt

class AboutView(TemplateView):
    template_name = "about.html"
    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["num_services"] = "9999999999999"
        ctxt["skills"] =[
            "おっpython",
            "C#",
            "javascript",
            "Rust",
            "GOGOchance!"
        ]
        return ctxt
