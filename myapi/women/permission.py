from rest_framework import permissions


class IsAdminReadOnly(permissions.BasePermission):
    # только для админа
    def has_permission(self, request, view):
        # проверяем безопасный ли метод
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    на уровне одного объекта
    Разрешение на уровне объекта, позволяющее редактировать объект только его владельцам.
Предполагается, что экземпляр модели имеет атрибут `user`.
    """

    def has_object_permission(self, request, view, obj):
        # Разрешения на чтение разрешены для любого запроса,
        # поэтому мы всегда будем разрешать запросы GET, HEAD или OPTIONS.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Экземпляр должен иметь атрибут с именем `user`.
        return obj.user == request.user