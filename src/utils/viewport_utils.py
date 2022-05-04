def debug_pixel_per_unit(viewport):
    screen_width = viewport.screen_width
    screen_height = viewport.screen_height

    world_width = viewport.world_width
    world_height = viewport.world_height

    x_ppu = screen_width/world_width
    y_ppu = screen_height/world_height

    print(f"xPPU={x_ppu} yPPU={y_ppu}")


def draw_grid(viewport, renderer):
    cell_size = 1
    old_color = renderer.color

    world_width = int(viewport.world_width)
    world_height = int(viewport.world_height)

    double_world_width = viewport.world_width * 2
    double_world_height = viewport.world_height * 2

    camera = viewport.camera
    renderer.sync(*camera.combined())
    renderer.begin()

    renderer.set_color((255, 255, 255))

    # verticval lines
    for x in range(-double_world_width, double_world_width + 1, cell_size):
        renderer.line(x, -double_world_height, x, double_world_width)

    # horizontal lines
    for y in range(-double_world_height, double_world_height + 1, cell_size):
        renderer.line(-double_world_width, y, double_world_width, y)

    # draw 0/0 lines
    renderer.set_color((255, 0, 0))
    renderer.line(0, -double_world_height, 0, double_world_height)
    renderer.line(-double_world_width, world_height,
                  double_world_width, world_height)

    # draw world bounds
    renderer.set_color((0, 255, 0))
    renderer.line(0, 0, world_width, 0)
    renderer.line(world_width, 0, world_width, world_height)

    renderer.set_color(old_color)

    renderer.end()
