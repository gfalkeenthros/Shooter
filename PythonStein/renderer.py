import pygame 
import math

TEXWIDTH = 64
TEXHEIGHT = 64


class Renderer:
    def __init__(self, width, height, textures):
        self.width = width
        self.height = height
        self.textures = textures

    def render(self, camera, grid, screen):
        for x in range(self.width):
            camera_x = 2 * x / self.width-1
            ray_dir_x = camera.dir[0] + camera.plane[0]*camera_x
            ray_dir_y = camera.dir[1] + camera.plane[1]*camera_x
            map_x = int(camera.pos[0])
            map_y = int(camera.pos[1])
            side_dist_x = 0
            side_dist_y = 0
            delta_dist_x = math.fabs(1/ray_dir_x)
            delta_dist_y = math.fabs(1/ray_dir_y)
            step_x = 0
            step_y = 0

            hit = 0

            if ray_dir_x < 0:
                step_x = -1
                side_dist_x = (camera.pos[0]-map_x) * delta_dist_x
            else:
                step_x = 1
                side_dist_x = (map_x + 1 - camera.pos[0]) * delta_dist_x

            if ray_dir_y < 0:
                step_y = -1
                side_dist_y = (camera.pos[1] - map_y) * delta_dist_y
            else:
                step_y = 1
                side_dist_y = (map_y + 1 - camera.pos[1]) * delta_dist_y

            while hit == 0:
                if side_dist_x < side_dist_y:
                    side_dist_x += delta_dist_x
                    map_x += step_x
                    side = 0
                else:
                    side_dist_y += delta_dist_y
                    map_y += step_y
                    side = 1

                if grid[map_y][map_x] > 0:
                    hit = 1

            if side == 0:
                perp_wall_dist = (
                    map_x - camera.pos[0] + (1-step_x) / 2) / ray_dir_x
            else:
                perp_wall_dist = (
                    map_y - camera.pos[1] + (1-step_y) / 2) / ray_dir_y

            line_height = int(self.height / perp_wall_dist)

            draw_start = -line_height / 2 + self.height/2
            draw_start = max(draw_start, 0)
            draw_end = line_height / 2 + self.height / 2
            draw_end = min(draw_end, self.height-1)

            tex_num = grid[map_y][map_x] - 1

            wall_x = 0

            if side == 0:
                wall_x = camera.pos[1] + perp_wall_dist * ray_dir_y
            else:
                wall_x = camera.pos[0] + perp_wall_dist * ray_dir_x
            
            wall_x -= math.floor(wall_x)

            tex_x = int(wall_x * float(64))

            if side == 0 and ray_dir_x > 0:
                tex_x = 64 - tex_x -1
            if side == 1 and ray_dir_y < 0:
                tex_x = 64 - tex_x -1
            
            step = float(TEXHEIGHT) / line_height

            tex_pos = (draw_start - self.height/2 + line_height / 2) *step

            for y in range(int(draw_start), int(draw_end)):
                tex_y = int(tex_pos) & (TEXHEIGHT-1)
                tex_pos += step
                color = (255,0,0) # self.textures[str(tex_num)].get_at((tex_x,tex_y))
                pygame.draw.rect(screen, color, (x,y,1,1),0)