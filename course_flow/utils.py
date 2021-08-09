import time

from django.contrib.contenttypes.models import ContentType
from django.db.models import Q

import course_flow.models as models

owned_throughmodels = [
    "node",
    "nodeweek",
    "week",
    "weekworkflow",
    "workflow",
    "workflowproject",
    "project",
    "columnworkflow",
    "workflow",
    "workflowproject",
    "project",
    "outcome",
    "outcomeoutcome",
    "outcome",
]


def get_model_from_str(model_str: str):
    return ContentType.objects.get(model=model_str).model_class()


def get_parent_model_str(model_str: str) -> str:

    return owned_throughmodels[owned_throughmodels.index(model_str) + 1]


def get_parent_model(model_str: str):

    return ContentType.objects.get(
        model=get_parent_model_str(model_str)
    ).model_class()


def linkIDMap(link):
    return link.id


def get_project_outcomes(project):
    # this should probably be replaced with a single recursive raw sql call...
    # but not by me
    outcomes = project.outcomes.all()
    for outcome in outcomes:
        outcomes = outcomes | get_descendant_outcomes(outcome)
    return outcomes


def get_descendant_outcomes(outcome):
    return models.Outcome.objects.filter(
        Q(parent_outcomes=outcome)
        | Q(parent_outcomes__parent_outcomes=outcome)
    )


def get_all_outcomes_for_outcome(outcome):
    outcomes = models.Outcome.objects.filter(
        Q(parent_outcomes=outcome)
        | Q(parent_outcomes__parent_outcomes=outcome)
    ).prefetch_related("outcome_horizontal_links", "child_outcome_links")
    outcomeoutcomes = models.OutcomeOutcome.objects.filter(
        Q(parent=outcome) | Q(parent__parent_outcomes=outcome)
    )
    return outcomes, outcomeoutcomes


def get_all_outcomes_for_workflow(workflow):
    outcomes = models.Outcome.objects.filter(
        Q(workflow=workflow)
        | Q(parent_outcomes__workflow=workflow)
        | Q(parent_outcomes__parent_outcomes__workflow=workflow)
    ).prefetch_related("outcome_horizontal_links", "child_outcome_links")
    outcomeoutcomes = models.OutcomeOutcome.objects.filter(
        Q(parent__workflow=workflow)
        | Q(parent__parent_outcomes__workflow=workflow)
    )
    return outcomes, outcomeoutcomes


def get_unique_outcomenodes(node):
    exclude_outcomes = models.Outcome.objects.filter(
        Q(parent_outcomes__node=node)
        | Q(parent_outcomes__parent_outcomes__node=node)
    )
    return node.outcomenode_set.exclude(outcome__in=exclude_outcomes).order_by(
        "rank"
    )


def get_unique_outcomehorizontallinks(outcome):
    exclude_outcomes = models.Outcome.objects.filter(
        Q(parent_outcomes__reverse_horizontal_outcomes=outcome)
        | Q(
            parent_outcomes__parent_outcomes__reverse_horizontal_outcomes=outcome
        )
    )
    return outcome.outcome_horizontal_links.exclude(
        parent_outcome__in=exclude_outcomes
    ).order_by("rank")


def benchmark(identifier, last_time):
    current_time = time.time()
    print("Completed " + identifier + " in " + str(current_time - last_time))
    return current_time
