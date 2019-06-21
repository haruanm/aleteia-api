""" This modules contains the services to handle the core.models.News """
import numpy as np
from django.db.models import Case, CharField, Value, When
from core.models import News


class NewsService:

    @staticmethod
    def get_labeled_news():
        """
        Get all labeled news
        :return: a list with 2 lists one with news texts and another with labels
        """
        news = News.objects.exclude(is_fake__isnull=True) \
                          .annotate(
                               label=Case(
                                   When(is_fake=True, then=Value('Fake')),
                                   When(is_fake=False, then=Value('True')),
                                   output_field=CharField(),
                               )
                           ) \
                          .values_list('text', 'label')

        return np.array(news).T.tolist()
