import datetime

from django.db.models import Count, Q
from django.shortcuts import get_object_or_404

from .forms import SuggestionForm
from .models import Suggestion, Comment, SuggestionAdminPage, PromotedFeatureSuggestion


def set_current_url_as_session_url(request):
    """
    Used to redirect to previous  url after making a purchase
    """
    request.session["session_url"] = str(request.build_absolute_uri())


def return_current_features(sorting="-upvotes"):
    """
    Returns all features  suggestions in the current
    voting cycle along with their upvote and comment count.
    Ordered by argument value
    """
    if sorting == "oldest":
        sorting = "date_time"
    elif sorting == "newest":
        sorting = "-date_time"
    elif sorting == "comments":
        sorting = "-comments"
    else:
        sorting = "-upvotes"

    return Suggestion.objects.filter(is_feature=True, suggestionadminpage__in_current_voting_cycle=True).annotate(
        upvotes=Count("upvote", distinct=True)).annotate(
        comments=Count("comment", distinct=True, filter=Q(comment__admin_page_comment=False))).order_by(sorting)


def return_all_current_bugs(sorting="newest"):
    """
    Returns all bugs in database that do not have a 
    status of 'done', along with their upvote and comment count. Ordered
    by argument value
    """
    if sorting == "oldest":
        sorting = "date_time"
    elif sorting == "newest":
        sorting = "-date_time"
    elif sorting == "comments":
        sorting = "-comments"
    else:
        sorting = "-upvotes"

    return Suggestion.objects.filter(~Q(suggestionadminpage__status=3), is_feature=False).annotate(
        upvotes=Count("upvote", distinct=True)).annotate(
        comments=Count("comment", distinct=True, filter=Q(comment__admin_page_comment=False))).order_by(sorting)


def return_public_suggestion_comments(suggestion, comment_sorting="oldest"):
    """
    Returns all non-admin comments for the argument suggestion,
    sorted by the argument value
    """
    if comment_sorting == "oldest":
        comment_sorting = "date_time"
    elif comment_sorting == "newest":
        comment_sorting = "-date_time"
    else:
        comment_sorting = "-upvotes"

    return Comment.objects.filter(suggestion=suggestion, admin_page_comment=False).annotate(
        upvotes=Count("upvote")).annotate(comments=Count("comment")).order_by(comment_sorting)


def return_admin_suggestion_comments(suggestion):
    """
    Returns all admin comments for the argument suggestion
    """
    return Comment.objects.filter(suggestion=suggestion, admin_page_comment=True).order_by("date_time").annotate(
        upvotes=Count("upvote"))


def update_suggestion_admin_page(form):
    """
    Updates a SuggestionAdminPage object using
    the values from the argument form
    """
    row = SuggestionAdminPage.objects.get(suggestion=form.cleaned_data["suggestion"])
    row.status = form.cleaned_data["status"]
    row.developer_assigned = form.cleaned_data["developer_assigned"]
    row.priority = form.cleaned_data["priority"]
    row.date_started = form.cleaned_data["date_started"]
    row.estimated_days_to_complete = form.cleaned_data["estimated_days_to_complete"]
    row.expected_completion_date = form.cleaned_data["expected_completion_date"]
    row.github_branch = form.cleaned_data["github_branch"]
    row.in_current_voting_cycle = form.cleaned_data["in_current_voting_cycle"]
    row.save()


def set_initial_session_form_title_as_false(request):
    """
    If there is no set form_title value in 
    the session, set it as False
    """
    # noinspection PyPep8
    try:
        x = request.session["form_title"]
    except:
        request.session["form_title"] = False


def return_previous_suggestion_form_values_or_empty_form(request):
    """
    If there are previous suggestion form values saved in the session,
    return a form prepopulated with these values. Otherwise return 
    an empty form.
    """
    if request.session["form_title"] != False:
        return SuggestionForm(
            initial={"user": request.user, "is_feature": True, "details": request.session["form_details"],
                     "title": request.session["form_title"]})

    else:
        # user value hidden using widget
        # therefore set as current user here
        return SuggestionForm(initial={"user": request.user})


def set_session_form_values_as_false(request):
    """
    For use in add_suggestion function. Allows these values
    to then be set as the user's current form values if they are redirected
    """
    request.session["form_title"] = False
    request.session["form_details"] = False


def submit_feature_promotion(request):
    """
    Create a PromotedFeatureSuggestion using the values
    submitted in the post request
    """
    user = request.user
    feature_id = request.POST.get("featureSuggestion")
    feature = get_object_or_404(Suggestion, id=int(feature_id))
    start_date_string = request.POST.get("startDate")
    start_date = datetime.datetime.strptime(start_date_string, "%Y-%m-%d")
    duration = int(request.POST.get("promotionDays"))
    end_date = (start_date + datetime.timedelta(days=duration))
    promoted_suggestion = PromotedFeatureSuggestion(user=user, suggestion=feature,
                                                    start_date=start_date, end_date=end_date)
    promoted_suggestion.save()


def get_promoted_features():
    """
    Returns all currently promoted features
    """
    current_date = datetime.date.today()
    promoted_feature_suggestions = PromotedFeatureSuggestion.objects.filter(end_date__gt=current_date,
                                                                            start_date__lte=current_date)
    return promoted_feature_suggestions
