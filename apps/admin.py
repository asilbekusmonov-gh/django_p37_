from datetime import date, datetime

from django.contrib import admin
from django.db.models import Count
from django.utils import timezone

from apps.models import Course, Student, Document


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'custom_price', 'student_count',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        qs = qs.annotate(_student_count=Count('student'))
        return qs

    @admin.display(description='Student sonlari')
    def student_count(self, obj: Course):
        return obj._student_count

    @admin.display(description='Narxi')
    def custom_price(self, obj: Course):
        return obj.price

    # has_student.boolean = True

    # date_hierarchy = 'added_on'
    # readonly_fields = ('student_count', 'has_student')

    # def get_queryset(self, request):
    #     qs = super().get_queryset(request)
    #     qs = qs.annotate(_student_count=Count('student'))
    #     return qs
    #
    # def has_student(self, obj):
    #     return obj._student_count > 0
    #
    # def student_count(self, obj):
    #     return obj._student_count
    #
    # has_student.boolean = True
    # has_student.short_description = 'Student'
    # student_count.admin_order_field = '_student__count'


class DocsStackedInline(admin.StackedInline):
    model = Document
    extra = 2


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('phone', 'custom_birth_day', 'custom_passport', 'custom_courses',)
    search_fields = ('phone', 'first_name',)
    inlines = [DocsStackedInline]

    @admin.display(description='Courslari')
    def custom_courses(self, obj: Student):
        return ', '.join(obj.course.values_list('name', flat=True))

    @admin.display(description="Birth Date")
    def custom_birth_day(self, obj):
        today = datetime.now().date()
        birth = obj.birth_date

        next_birthday = birth.replace(year=today.year)
        if next_birthday < today:
            next_birthday = next_birthday.replace(year=today.year + 1)
        days_left = (next_birthday - today).days
        birth_str = birth.strftime("%Y.%m.%d")
        return f"{birth_str} ({days_left} kun qoldi)"

    @admin.display(description='Passporti')
    def custom_passport(self, obj: Student):
        return f'{obj.passport_series} {obj.passport_number}'

    # search_fields = ('first_name', 'category__name')

    # actions = ['export_students_csv']
    #
    # def export_students_csv(self, request, queryset):
    #     response = HttpResponse(content_type='text/csv')
    #     response['Content-Disposition'] = f'attachment; filename="students.csv"'
    #     writer = csv.writer(response)
    #
    #     writer.writerow(['ID', 'First Name', 'Full Name'])
    #
    #     for student in queryset:
    #         writer.writerow([student.id, student.first_name, student.full_name])
    #
    #     return response
    # export_students_csv.short_description = 'Export Students'

    # def has_add_permission(self, request):
    #     if self.model.objects.count() >= 3: # -----> restrict add
    #         return False
    #     return super().has_add_permission(request)

    # def get_actions(self, request):
    #     actions = super().get_actions(request)
    #     if 'delete_selected' in actions:        #  ---> remove delete selected
    #         del actions['delete_selected']
    #
    #     return actions

# admin.site.unregister(Group)
# admin.site.unregister(User)
