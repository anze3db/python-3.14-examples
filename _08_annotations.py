class Conference:
    attendees: list[Attendee]


class Attendee:
    pass


from annotationlib import Format, get_annotations

print(get_annotations(Conference, format=Format.FORWARDREF))
