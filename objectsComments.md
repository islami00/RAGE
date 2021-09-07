# customising the character class

1. Instead of being an image, render a circle, with a rounded stroke for body and two rounded strokes for arms.
2. Positioning will be flimsy.
3. Remove image, and generate dynamically based on the character rectangle (enable scaling).
4. An ellipse the size of the head,
5. A line that is rounded at both ends , or that extends from the center of the head to the chin + how long the torso should be
   1. I just imagined that as the spinal cord, and a very brutal despining
6. from the end of the torso line, two more lines for the legs. Positioning might be difficult.
7. The legs are the only ones that seem like they may actually need rounding at the end, if everyone else is well-positioned.
8. Group everything together as an entity and create a wrapper rect for monitoring
9. We could also use a canvas-like stock image and dev on that

# Main docs.

1. `clock.tick()` takes an argument of framerate, allowing us to lock fps so easily.  
   As quoted from [pygame](https://www.pygame.org/docs/ref/time.html):  
   `tick()`  
   update the clock  
   `tick(framerate=0) -> milliseconds`  
   This method should be called once per frame. It will compute how many milliseconds have passed since the previous call.

If you pass the optional framerate argument the function will delay to keep the game running slower than the given ticks per second. This can be used to help limit the runtime speed of a game. By calling `Clock.tick(40)` once per frame, the program will never run at more than 40 frames per second.

Note that this function uses `SDL_Delay` function which is not accurate on every platform, but does not use much CPU. Use `tick_busy_loop` if you want an accurate timer, and don't mind chewing CPU.

2. [blits and surfaces.](https://www.pygame.org/docs/ref/surface.html#pygame.Surface.blit)

# Vids

1. [Pygame playlist](https://www.youtube.com/playlist?list=PL6gx4Cwl9DGAjkwJocj7vlc_mFU-4wXJq)
