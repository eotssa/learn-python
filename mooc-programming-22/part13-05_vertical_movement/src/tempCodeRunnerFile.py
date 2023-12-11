    y += velocity
    if velocity > 0 and x+robot.get_height() >= 480:
        velocity = -velocity
    if velocity < 0 and x <= 0:
        velocity = -velocity