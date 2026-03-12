# from django.shortcuts import render, get_object_or_404, redirect
#
# from apps.admin import Course
# from apps.models import Student
#
#
# def student_list_page(request):
#     context = {
#         'students': Student.objects.all(),
#         'courses': Course.objects.all()
#
#     }
#
#     return render(request, 'apps/student_list.html', context)
#
#
# def student_detail_page(request, pk):
#     student = get_object_or_404(Student, pk=pk)
#
#     context = {
#         'student': student,
#     }
#
#     return render(request, 'apps/student_page.html', context)
#
#
# def update_student_page(request, pk):
#     if request.method == 'POST':
#         student = get_object_or_404(Student, pk=pk)
#
#         student.first_name = request.POST.get('first_name')
#         student.last_name = request.POST.get('last_name')
#         student.save()
#
#     return redirect('student_list')
#
#
# def delete_student_page(request, pk):
#     if request.method == 'POST':
#         student = get_object_or_404(Student, pk=pk)
#         student.delete()
#
#     return redirect('student_list')
#
#
# def add_student_page(request):
#     if request.method == 'POST':
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         university_id = request.POST.get('university_id')
#
#         Student.objects.create(first_name=first_name, last_name=last_name, university_id=university_id)
#
#         return redirect('student_list')
#
#     context = {
#         'universities': University.objects.all(),
#     }
#
#     return render(request, 'apps/add_student.html', context)
