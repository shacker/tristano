def create_profile(sender, instance, signal, created, **kwargs):
    """When user is created also create a matching profile and list."""

    from profiles.models import Profile
    
    if created:
        Profile(user = instance).save()
