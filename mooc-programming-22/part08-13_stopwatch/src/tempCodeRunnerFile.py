    clock = Stopwatch()
    # advance hour minus one second
    for i in range(60*59+59):
        clock.tick()         
    clock.tick()