
def asbool(val):
    if val is None:
        return False
    if isinstance(val, bool):
        return val
    val = str(val).strip().lower()
    return val in ('t', 'true', 'y', 'yes', 'on', '1')

def asint(val, minimum=None, maximum=None):
    if val is None:
        val = 0
    val = int(val)
    val = min(val, maximum if maximum else val)
    val = max(val, minimum if minimum else val)
    return val


def aslist(val):
    if val is None:
        return []
    if isinstance(val, list):
        return val
    return str(val).replace(' ', '').split(',')

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4