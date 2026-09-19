from django import template

register = template.Library()

@register.inclusion_tag('posts/components/avatar.html')
def user_avatar(user, size_class="w-11 h-11 text-base"):
    if user and user.username:
        initial = user.username.upper()
    else:
        initial = "?"

    return {
        'initial': initial,
        'size_class': size_class,
        'username': user.username if user else "Unknown"
    }
