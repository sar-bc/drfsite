from django.contrib import admin
from .models import Category, Women
from django import forms
from django.urls import path
from django.contrib import messages
from django.shortcuts import render, redirect


class CsvImportForm(forms.Form):
    csv_uploader = forms.FileField()


class CategoryAdmin(admin.ModelAdmin):
    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path("upload-csv-category/", self.upload_csv)]
        return new_urls + urls

    def upload_csv(self, request):
        if request.method == "POST":
            csv_file = request.FILES['csv_uploader']

            if not csv_file.name.endswith('.csv'):
                messages.warning(request, 'Ошибочный тип файла')
                return redirect('.')

            file_data = csv_file.read().decode("utf-8")
            csv_data = file_data.split("\n")
            print(csv_data)
            for x in csv_data:
                fields = x.split(",")
                if len(fields) > 1:
                    created = Category.objects.update_or_create(
                        id=fields[0],
                        name=fields[1]
                    )
                else:
                    print("Недостаточно полей в строке:", x)
            messages.success(request, "Файл успешно импортирован")
            return redirect('admin:index')

        form = CsvImportForm()
        data = {"form": form}
        return render(request, "admin/csv_uploader.html", data)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Women)
