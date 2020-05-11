
# graph of resources, alternates between "lane" and "intersection"

# If multiple robots are on a lane resource at the same
# time, they must all be travelling in the same direction,
# and they cannot overtake each other. The idea is that
# lane resources can be long enough to hold multiple
# robots, but not wide enough for two robots to drive
# side-by-side

# route-plan
# start resource, r
# start time, t
# end resource, r'
#
# d(r) > 0 is the minimum time for robot to traverse resource r
# c(r) = max # of robots that can simultaneously use resource r
#
# c(r) = 1 for all intersections
# c(r) >= 1 for all lanes
#
# n plan steps such that r1 = r, rn = r', t1 >= t and
# for all j in {1, ..., n}:  interval tau_j meets interval tau_(j+1), j<n
# and tau_j >= d(r_j) and (r_j, r_j+1) in E_R (successor relation)
# pi = ((r1, tau1), (r2, tau2), ..., (rn, tau_n)), tau_i = [t_i, t_i')

# resource loading function, lambda
# lambda(r,t)

def build_usage_sequence(resource):

    INFINITY = 999999999

    count_at_time = [(0, 0)]
    for usage in resource['loading']:
        previous_count = count_at_time[-1][1]
        count_at_time.append((usage['from'], previous_count+1))
        count_at_time.append((usage['to'], previous_count))

    count_at_time.append((INFINITY,0))

    print(count_at_time)

    return count_at_time

# free-time-window
# w = [t1, t2) such that:
# for all t in w, lambda(r,t) < c(r)
# AND
# (t2 - t1) >= d(r)
def find_free_time_windows(resource, duration):
    # look for gaps in usages
    # data structure
    # time count
    count_at_time = [(0, 0)]
    for usage in resource['loading']:
        previous_count = count_at_time[-1][1]
        count_at_time.append((usage['from'], previous_count+1))
        count_at_time.append((usage['to'], previous_count))

    count_at_time.append((INFINITY,0))

    print(count_at_time)

def find_count_at_time(count_at_time, t):
    count = 0
    for (time,loading) in count_at_time:
        if (time > t):
            break
        count = loading

    return count

def find_counts_in_window(count_at_time, window):
    counts = []
    start = window[0]
    end = window[1]
    for (time,loading) in count_at_time:
        if (time < start):
            continue

        if (time > end):
            break

        counts.append(loading)

    return counts

def find_windows_less_than(count_at_time, value):
    windows = []
    current_window = None
    for (time,loading) in count_at_time:
        if (loading < value and current_window is None):
            print("starting new window ...")
            current_window = (time, None)
        elif (loading < value and current_window is not None):
            print("updating current window ...")
            current_window = (current_window[0], time)
        elif (loading >= value and current_window is not None):
            print("closing window ...")
            windows.append((current_window[0],time))
            current_window = None

    if (current_window is not None):
        windows.append(current_window)
        
    return windows

def is_free(window, count_at_time, capacity):

    # find count at start
    start = window[0]
    end = window[1]
    count_at_start = find_count_at_time(count_at_time, start)





def test_ftw():
    # create a resource
    resource = {}
    resource['id'] = 'Lane1'
    resource['loading'] = []
    resource['capacity'] = 1

    # add some usages
    u1 = {}
    u1['by'] = 'Robot1'
    u1['from'] = 2
    u1['to'] = 8

    resource['loading'].append(u1)

    count_at_time = build_usage_sequence(resource)
    print(count_at_time)


    # find free=time-windows
    #free_windows = find_free_time_windows(resource, duration=5)
