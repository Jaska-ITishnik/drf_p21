from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomPageNumberPagination(PageNumberPagination):
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        return Response({
            'soni': self.page.paginator.count,
            'keyingisi': self.get_next_link(),
            'oldingise': self.get_previous_link(),
            'natija': data,
        })