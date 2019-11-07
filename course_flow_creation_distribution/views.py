from .models import (
    Course,
    Preparation,
    Activity,
    Assesment,
    Artifact,
    Strategy,
    Node,
    NodeStrategy,
    StrategyActivity,
    ComponentWeek,
    WeekCourse,
)
from .serializers import (
    ActivitySerializer,
    CourseSerializer,
    StrategySerializer,
)
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.db.models import Q
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io
from django.http import JsonResponse


class CourseDetailView(DetailView):
    model = Course
    template_name = "course_flow_creation_distribution/course_detail.html"

    def get_context_data(self, **kwargs):
        context = super(DetaileView, self).get_context_data(**kwargs)
        context["week_course_links"] = WeekCourse.objects.filter(
            course=self.get_object()
        )
        context["component_week_links"] = []
        for week in self.get_object().weeks.all():
            context["component_week_links"].append(
                ComponentWeek.objects.filter(week=week)
            )
        return context


class CourseUpdateView(UpdateView):
    model = Course
    template_name = "course_flow_creation_distribution/course_update.html"
    fields = ["title", "description", "author"]

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context["week_course_links"] = WeekCourse.objects.filter(
            course=self.get_object()
        ).order_by("-rank")
        context["component_week_links"] = ComponentWeek.objects.filter(
            week__in=self.get_object().weeks.all()
        ).order_by("-rank")
        context["preparations"] = Preparation.objects.all()
        context["activities"] = Activity.objects.all()
        context["assesments"] = Assesment.objects.all()
        context["artifacts"] = Artifact.objects.all()
        return context

    def get_success_url(self):
        return reverse("course-detail", kwargs={"pk": self.object.pk})


class CourseDeleteView(DeleteView):
    model = Course
    template_name = "course_flow_creation_distribution/course_delete.html"


class ActivityDetailView(DetailView):
    model = Strategy
    template_name = "course_flow_creation_distribution/activity_detail.html"

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context["activity_json"] = JSONRenderer().render(StrategySerializer(self.object).data).decode("utf-8")
        return context


class ActivityUpdateView(UpdateView):
    model = Activity
    fields = ["title", "description", "author"]
    template_name = "course_flow_creation_distribution/activity_update.html"

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context["nodes"] = Node.objects.all()
        """
        context["strategies"] = Strategy.objects.filter(default_strat=False)
        context["default_strategies"] = Strategy.objects.filter(
            default_strat=True
        )
        """
        context["left_node_icons"] = LeftNodeIcon.objects.all()
        context["right_node_icons"] = RightNodeIcon.objects.all()
        context["strategy_activity_links"] = StrategyActivity.objects.filter(
            activity=self.get_object()
        ).order_by("-rank")
        context["node_strategy_links"] = NodeStrategy.objects.filter(
            strategy__in=self.get_object().strategies.all()
        ).order_by("-rank")
        return context

    def get_success_url(self):
        return reverse("activity-detail", kwargs={"pk": self.object.pk})


class ActivityDeleteView(DeleteView):
    model = Activity
    template_name = "course_flow_creation_distribution/activity_delete.html"

def update_strategy_json(request):
    json = request.POST.get("json")
    byte_data = io.BytesIO(json.encode())
    data = JSONParser().parse(byte_data)
    serializer = StrategySerializer(Strategy.objects.get(id=data['id']), data=data)
    serializer.is_valid()
    serializer.save()
    return JsonResponse({"action": "updated"})
