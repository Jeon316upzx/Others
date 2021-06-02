#from .models import Journal
#from .models import Publications
#from .models import Hit


def get_journal_statistics():

    # Construct summary dict in the form {journal_id -> (total_views, total_downloads)}

    PAGEVIEW = 'PV'
    DOWNLOAD = 'DL'
    ACTIONS = (
        (PAGEVIEW, 'Article web page view'),
        (DOWNLOAD, 'Article download'),
    )

    # get all journal instances
    journals_qs = Journal.objects.all()

    # for each instance of the journal get all hit instances that have the journal id
    # and actionis either PAGEVIEW OR DOWNLOAD and use queryset count to get their number of instances
    for journal in journals_qs:
        # summary dictionary
        summary = dict()
        hitpageView = Hit.objects.filter(
            journal_id=journal.pk, action=PAGEVIEW).count()
        hitdownload = Hit.objects.filter(
            journal_id=journal.pk, action=DOWNLOAD).count()

        summary[journal_id] = (hitpageView, hitdownload,)

    return summary
