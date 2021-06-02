# from .models import Journal
#from .models import Publications


def get_journal_statistics():
    # Construct summary dict in the form {journal_id -> (total_views, total_downloads)}
    journals_qs = Journal.objects.all()
    publications_qs = Publications.objects.filter(journals_qs.pk)
