from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r"^conference-ticket-types$", views.get__get_conference_ticket_types),
    re_path(
        r"^conference-ticket-types/(?P<ticket_type_code>\w+)/check",
        views.get__check_conference_ticket_type_buyable,
    ),
    re_path(r"^conference-tickets", views.post__add_conference_ticket),
    re_path(r"^list$", views.temp),
    re_path(r"^{item_id}$", views.temp),
    re_path(r"^success$", views.temp),
    re_path(r"^failed$", views.temp),
    re_path(r"^{ticket_id}/refund$", views.temp),
]