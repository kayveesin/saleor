from django.http import HttpResponse
from django.contrib.admin.views.decorators import staff_member_required
from django.template.response import TemplateResponse
from .forms import DonationReceiptForm
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import datetime
import threading
import cStringIO as StringIO
import xhtml2pdf.pisa as pisa
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from cgi import escape


@staff_member_required
def index(request):

    if request.method == 'POST':
        print (request.POST)
        download_thread = threading.Thread(target=addValuesToSpreadSheet, args=[request])
        download_thread.start()


    form = DonationReceiptForm()
    return TemplateResponse(request, 'donation/template.html', {'form':form, 'submitted':True})


def addValuesToSpreadSheet(request):

    scope = ['https://spreadsheets.google.com/feeds']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('Peepal Farm-a801840bd275.json', scope)
    gc = gspread.authorize(credentials)
    wks = gc.open("Peepal Farm Donations").sheet1
    if gc:
        print 'hurray'

        name = request.POST.get("fullName")
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        date = request.POST.get("date")
        channel = request.POST.get("channel")
        amount = request.POST.get("amount")


        wks.append_row([name, email, mobile, amount, date,
                        datetime.date.today(), channel])


def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    context = Context(context_dict)
    html  = template.render(context)
    result = StringIO.StringIO()

    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))


def myview(request):
    #Retrieve data or whatever you need
    return render_to_pdf(
            'donation/receipt_template.html',
            {
                'pagesize':'A4',
                'mylist': ['Hello','Hello','Hello','Hello','Hello','Hello',],
            }
        )
