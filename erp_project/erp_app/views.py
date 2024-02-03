import pdfkit
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string

from .forms import LetterForm, EditLetterForm, LetterDetailsForm
from .models import Letter, LetterDetails


@login_required
def home(request):
    user_letters = Letter.objects.filter(user=request.user)
    return render(request, 'home.html', {'user_letters': user_letters})


@login_required
def create_letter(request):
    if request.method == 'POST':
        form = LetterForm(request.POST)
        if form.is_valid():
            letter = form.save(commit=False)
            letter.user = request.user
            letter.save()
            return redirect('home')
    else:
        form = LetterForm()

    return render(request, 'create_letter.html', {'form': form})


@login_required
def tracking_code(request):
    user_letter = get_object_or_404(Letter, user=request.user)
    return render(request, 'tracking_code.html', {'user_letter': user_letter})


def tracking_code_entry(request):
    return render(request, 'tracking_code_entry.html')


def track_letter_condition(request):
    if request.method == 'POST':
        tracking_code = request.POST.get('tracking_code')
        try:
            letter = Letter.objects.get(tracking_code=tracking_code, user=request.user)
        except Letter.DoesNotExist:
            error_message = "Letter not found or you are not authorized to track this letter."
            return render(request, 'error_page.html', {'error_message': error_message})

        return render(request, 'track_condition.html', {'letter': letter})

    return render(request, 'track_condition.html')


def get_letter_details(tracking_code):
    letter = get_object_or_404(Letter, tracking_code=tracking_code)
    return letter


@login_required
def view_letter(request, tracking_code):
    letter = get_object_or_404(Letter, tracking_code=tracking_code)
    form = LetterDetailsForm(request.POST or None)


    if request.method == 'POST' and form.is_valid():
        additional_text = form.cleaned_data.get('additional_text')
        referred_to_group = form.cleaned_data.get('referred_to_group')
        is_done = form.cleaned_data.get('is_done')



        if additional_text:
            letter.additional_text = additional_text



        if referred_to_group:
            letter.referred_to_group = referred_to_group
            letter.recipient = referred_to_group
            letter.is_read = True
            letter.reci_get = letter.recipient


        if is_done :
            letter.referred_to_user = letter.user
            letter.progress = 'done'
            letter.status = 'Done'
            return render(request,'home.html')
        else:
            letter.status = 'In Progress'


        letter.save()


        if referred_to_group and additional_text:
            letter.add_reference(referred_to_group, additional_text)


    references = LetterDetails.objects.filter(letter=letter, referred_to_group__isnull=False)
    additionals = LetterDetails.objects.filter(letter=letter, additional_text__isnull=False)


    return render(request, 'view_letter.html', {'letter': letter, 'form': form, 'references': references, 'additionals': additionals})


@login_required
def edit_letter(request, tracking_code):
    letter = get_object_or_404(Letter, tracking_code=tracking_code, user=request.user)

    if request.method == 'POST':
        form = EditLetterForm(request.POST, instance=letter)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EditLetterForm(instance=letter)

    return render(request, 'edit_letter.html', {'form': form, 'letter': letter})


def download_pdf(request, tracking_code):
    letter = get_object_or_404(Letter, tracking_code=tracking_code)

    html_content = render_to_string('track_condition.html', {'letter': letter})

    pdf_file = pdfkit.from_string(html_content, False)

    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="letter_{letter.tracking_code}.pdf"'

    return response


