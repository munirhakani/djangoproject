from django.core.paginator import Paginator, EmptyPage


class SafePaginator(Paginator):
    def validate_number(self, number):
        try:
            return super().validate_number(number)
        except EmptyPage:
            if int(number) > 1:
                return self.num_pages
            elif int(number) < 1:
                return 1
            else:
                raise


class SuccessUrlMixin:
    def get_success_url(self):
        return self.model.get_object_list_url() \
            + '?page=' + self.request.POST.get('pagenumber') \
            + '&sortby=' + self.request.POST.get('sortby') \
            + '&find=' + self.request.POST.get('find')