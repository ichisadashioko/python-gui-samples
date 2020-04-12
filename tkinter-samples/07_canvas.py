import tkinter as tk
import skimage.io as ski_io
import numpy as np
import cv2
import matplotlib.pyplot as plt
import io
from PIL import Image

if __name__ == "__main__":

    app = tk.Tk()

    CANVAS_WIDTH = 200
    CANVAS_HEIGHT = 200

    canvas = tk.Canvas(
        app,
        width=CANVAS_WIDTH,
        height=CANVAS_HEIGHT,
    )

    canvas.pack()

    def key_release(event):
        print(event)
        # print(event.char)

        if event.char == 's':
            ps = canvas.postscript(colormode='color')
            img = Image.open(io.BytesIO(ps.encode('utf-8')))
            np_img = np.array(img)
            print(np_img.shape)
            
            # script_filename = 'temp_canvas.eps'
            # # save canvs to .eps (postscript) file
            # canvas.postscript(
            #     file=script_filename,
            #     colormode='color',
            #     width=CANVAS_WIDTH,
            #     height=CANVAS_HEIGHT,
            #     pagewidth=CANVAS_WIDTH-1,
            #     pageheight=CANVAS_HEIGHT-1,
            # )
            # # read the poscript data
            # print(f'script_filename: {script_filename}')
            # # data = ski_io.imread(script_filename)
            # data = ski_io.imread(fname=script_filename)

            # # write a rasterized png file
            # img_filename = 'canvas-image.png'
            # ski_io.imsave(img_filename, data)
            # np_img = cv2.imread(img_filename, 0)
            # plt.imshow(np_img)
            # plt.colorbar()
            # plt.show()

        pass

    canvas.create_line(0, 0, 200, 200)
    canvas.create_rectangle(0, 0, 50, 50, fill='black')

    app.bind('<KeyRelease>', key_release)
    app.mainloop()
