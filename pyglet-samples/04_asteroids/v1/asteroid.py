import pyglet

game_window = pyglet.window.Window()
pyglet.resource.path = ['../resources']
pyglet.resource.reindex()

player_image = pyglet.resource.image('ship.png')
bullet_image = pyglet.resource.image('bullet.png')
asteroid_image = pyglet.resource.image('asteroid3.png')

def center_image(image):
    '''Sets an image's anchor point to its center'''
    image.anchor_x = image.width // 2
    image.anchor_y = image.height // 2

center_image(player_image)
center_image(bullet_image)
center_image(asteroid_image)

if __name__ == "__main__":
    pyglet.app.run()
