def reservation_slug_generator(sender, instance, *args, **kwargs):
    instance.slug = '{}_{}_{}'.format(instance.room.sign, str(instance.date), str(instance.time))
