from django.shortcuts import render
from googletrans import Translator

# Create your views here.
def index(request):
    in_txt = request.GET.get("in_txt","")
    in_lang = request.GET.get("in_lang","")
    out_lang = request.GET.get("out_lang","")

    context = {}

    if in_txt:
        if in_lang:
            if out_lang:
                text1 = in_txt
                translator = Translator()
                out_txt = translator.translate(text1,src=in_lang,dest=out_lang).text

                context = {
                    "in_txt" : in_txt,
                    "in_lang" : in_lang,
                    "out_txt" : out_txt,
                    "out_lang" : out_lang,
                }
                return render(request,"trans/index.html",context)

    return render(request,"trans/index.html")