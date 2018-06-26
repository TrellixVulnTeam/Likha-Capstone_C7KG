
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from friends.datamining import correlations, forecast as f
from datainput.models import NutritionalStatus, Barangay, Sex, ChildCare, Tuberculosis, Malaria, Immunization, \
    MaternalCare, Schistosomiasis, Leprosy, Flariasis, STISurveillance
from friends.datapreprocessing import checkers
from django.shortcuts import render, redirect
from core.models import Profile, Notification
from friends import datapoints


# Create your views here.

@login_required
def index(request):

    if checkers.is_updated():

        nutritional_statuses = NutritionalStatus.objects.all()

        scores = []

        # # # # # # # # # # # # #
        # FEMALE
        sex = Sex.objects.get(name='Female')
        sex2 = Sex.objects.get(name='Male')

        correlations.display(
            datapoints.get_child_care_fields(),
            scores,
            ChildCare,
            sex
        )

        correlations.display(
            datapoints.get_tb_fields(),
            scores,
            Tuberculosis,
            sex
        )

        correlations.display(
            Malaria._meta.get_fields()[1:6],
            scores,
            Malaria,
            sex
        )

        correlations.display(
            Immunization._meta.get_fields()[1:11],
            scores,
            Immunization,
            sex
        )

        correlations.display(
            Schistosomiasis._meta.get_fields()[1:3],
            scores,
            Schistosomiasis,
            sex
        )

        correlations.display(
            Leprosy._meta.get_fields()[1:3],
            scores,
            Leprosy,
            sex
        )

        correlations.display(
            Flariasis._meta.get_fields()[1:4],
            scores,
            Flariasis,
            sex
        )

        correlations.display_no_sex(
            MaternalCare._meta.get_fields()[1:10],
            scores,
            MaternalCare,
            sex
        )

        correlations.display_no_sex(
            STISurveillance._meta.get_fields()[2:5],
            scores,
            STISurveillance,
            sex
        )

        correlations.display(
            datapoints.get_child_care_fields(),
            scores,
            ChildCare,
            sex2
        )

        correlations.display(
            datapoints.get_tb_fields(),
            scores,
            Tuberculosis,
            sex2
        )

        correlations.display(
            Malaria._meta.get_fields()[1:6],
            scores,
            Malaria,
            sex2
        )

        correlations.display(
            Immunization._meta.get_fields()[1:11],
            scores,
            Immunization,
            sex2
        )

        correlations.display(
            Schistosomiasis._meta.get_fields()[1:3],
            scores,
            Schistosomiasis,
            sex2
        )

        correlations.display(
            Leprosy._meta.get_fields()[1:3],
            scores,
            Leprosy,
            sex2
        )

        correlations.display(
            Flariasis._meta.get_fields()[1:4],
            scores,
            Flariasis,
            sex2
        )

        correlations.display_no_sex(
            MaternalCare._meta.get_fields()[1:10],
            scores,
            MaternalCare,
            sex2
        )

        correlations.display_no_sex(
            STISurveillance._meta.get_fields()[2:5],
            scores,
            STISurveillance,
            sex2
        )

        correlations.display_informal_settlers(scores)

        request.session['scores'] = scores
        profile = Profile.objects.get(user=request.user)

        context = {
            'profile': profile,
            'active': 'ct',
            'statuses': nutritional_statuses,
            'scores': scores
        }

        return render(request, 'datamining/index.html', context)

    messages.error(request, 'Data is not up to date')
    return redirect('core:nutritionist')


@login_required
def get_positive(request):

    correlations = request.session['scores']
    profile = Profile.objects.get(user=request.user)

    scores = [x for x in correlations if x['score'] > 0]

    context = {
        'profile': profile,
        'active': 'ct',
        'scores': scores
    }

    return render(request, 'datamining/index.html', context)


# predictive modeling page
@login_required
def forecast(request, id):

    correlation = request.session['scores']

    cr_line = correlation[id]
    score = cr_line['score']
    variables = cr_line['variables']
    equation = f.get_equation_string(score, variables)

    context = {
        'cr': cr_line,
        'equation': equation,
        'variables': variables,
        'line': f.get_line(score, variables),
        'equation_variables': f.get_variables(score, variables)
    }

    return render(request, 'datamining/forecast.html', context)
