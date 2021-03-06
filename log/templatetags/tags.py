from django import template

register = template.Library()

@register.filter(name='format_pace')
def format_pace(duration):
    if duration == None:
        return '-'

    s = duration.seconds
    hours = s // 3600
    s = s - (hours * 3600)
    minutes = s // 60
    seconds = str(s - (minutes * 60))
    if len(seconds) == 1:
        seconds = '0' + seconds
    return '%s:%s' % (minutes, seconds)

@register.filter(name='format_units')
def format_units(unit):
    if unit == "Miles":
        return " mi"
    if unit == "Meters":
        return "m"
    return " k"

@register.filter(name='format_duration')
def format_duration(duration):
    text = str(duration)
    separated = text.split(':')
    seconds = separated[2]
    minutes = separated[1]
    if '.' in seconds:
        seconds = round(float(separated[2]), 2)
    else:
        seconds = int(seconds)
    if seconds < 10:
        seconds = '0'+str(seconds)

    if separated[0] == '0' and minutes < 10:
        minutes = '0'+str(minutes)

    return "{0}:{1}".format(minutes, seconds)

@register.filter(name='format_distance')
def format_distance(d):
    d = round(d, 2)
    lst = str(d).split('.')
    if len(lst) > 1:
        if lst[-1] == '0':
            return "{0}".format(lst[0])
    return d
