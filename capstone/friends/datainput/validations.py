from datetime import datetime

from datainput.models import Patient, MonthlyReweighing


def has_monthly_reweighing(barangay, month):

    patients = Patient.objects.filter(barangay=barangay)

    for patient in patients:

        try:
            mr = MonthlyReweighing.objects.get(patient=patient, date__month=month)
            print(mr)
        except MonthlyReweighing.DoesNotExist:
            return False

    return


def is_updated(patient):

    reweighs = MonthlyReweighing.objects.filter(patient=patient)

    if reweighs.count() == 0:
        return False

    for weighs in reweighs:

        if weighs.date.month == datetime.now().month and weighs.date.year == datetime.now().year:
            return True

    return False
